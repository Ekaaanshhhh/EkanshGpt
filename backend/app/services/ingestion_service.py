"""
Ingestion Service (Orchestrator)
==================================
Orchestrates the entire document ingestion pipeline:

    parse → chunk → embed → store

Why an orchestrator?
─────────────────────
Without this, the route handler would coordinate 3 services manually:

    # BAD — route handler doing orchestration
    text = file_parser.parse(path)
    chunks = chunker.chunk_text(text)
    vector_store.store_chunks(chunks, metadata)

With this orchestrator, the route makes ONE call:

    # GOOD — route calls orchestrator
    result = ingestion_service.ingest_document(path, metadata)

Benefits:
1. The route stays thin (HTTP concerns only)
2. The pipeline logic is testable without HTTP
3. You can reuse this from CLI scripts, cron jobs, etc.
4. Error handling is centralized

This pattern is called "Service Layer" or "Application Service" —
it's the same concept as a "use case" in Clean Architecture.

Usage:
    from app.services.ingestion_service import ingest_document

    result = ingest_document(
        file_path=Path("uploads/resume.pdf"),
        source="resume.pdf",
        category="resume",
        document_name="Ekansh's Resume",
        document_type="pdf",
    )
"""

import uuid
from datetime import datetime, timezone
from pathlib import Path
from dataclasses import dataclass

from app.config import settings
from app.services import file_parser, chunker, vector_store
from app.utils.logger import logger


@dataclass
class IngestResult:
    """
    Result of a successful ingestion operation.

    Using a dataclass here instead of a Pydantic model because
    this is internal (not serialized to HTTP). Pydantic models
    are for request/response validation at the API boundary.
    """

    document_id: str
    chunks_stored: int
    source: str
    category: str


def ingest_document(
    file_path: Path,
    source: str,
    category: str,
    document_name: str,
    document_type: str,
) -> IngestResult:
    """
    Run the full ingestion pipeline for a single document.

    Pipeline steps:
    1. Parse — Extract plain text from the file
    2. Chunk — Split text into overlapping pieces
    3. Embed + Store — Generate embeddings and store in ChromaDB

    Args:
        file_path: Path to the uploaded file.
        source: Original filename (e.g., "resume.pdf").
        category: Document taxonomy category (e.g., "resume").
        document_name: Human-readable name (e.g., "Ekansh's Resume").
        document_type: File type (e.g., "pdf", "markdown", "text").

    Returns:
        IngestResult with document_id and chunk count.

    Raises:
        ValueError: If the file type is unsupported or text is empty.
        FileNotFoundError: If the file doesn't exist.
    """
    # Generate a unique document ID
    doc_id = f"doc_{category}_{uuid.uuid4().hex[:8]}"

    logger.info(f"Starting ingestion: {source} → {doc_id}")

    # ── Step 1: Parse ──────────────────────────────────────
    logger.info(f"[1/3] Parsing: {source}")
    text = file_parser.parse(file_path)

    if not text.strip():
        raise ValueError(f"No text could be extracted from '{source}'")

    logger.info(f"[1/3] Extracted {len(text)} characters")

    # ── Step 2: Chunk ──────────────────────────────────────
    logger.info(f"[2/3] Chunking text...")
    chunks = chunker.chunk_text(text)

    if not chunks:
        raise ValueError(f"Text from '{source}' produced no chunks")

    logger.info(f"[2/3] Created {len(chunks)} chunks")

    # ── Step 3: Embed + Store ──────────────────────────────
    logger.info(f"[3/3] Generating embeddings and storing in ChromaDB...")

    # Build metadata for each chunk
    # Every chunk gets the SAME document-level metadata
    # so we can filter by source, category, etc. during retrieval
    now = datetime.now(timezone.utc).isoformat()
    chunk_metadatas = [
        {
            "source": source,
            "category": category,
            "document_name": document_name,
            "document_type": document_type,
            "owner": settings.DOCUMENT_OWNER,
            "uploaded_at": now,
            "chunk_index": i,
            "total_chunks": len(chunks),
        }
        for i in range(len(chunks))
    ]

    chunks_stored = vector_store.store_chunks(
        chunks=chunks,
        metadatas=chunk_metadatas,
        doc_id=doc_id,
    )

    logger.info(
        f"✅ Ingestion complete: {source} → {chunks_stored} chunks "
        f"(doc_id={doc_id})"
    )

    return IngestResult(
        document_id=doc_id,
        chunks_stored=chunks_stored,
        source=source,
        category=category,
    )
