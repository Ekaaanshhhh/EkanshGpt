"""
Vector Store Service
======================
Manages ChromaDB Cloud connection and embedding generation.

Architecture Decision: Why This Is a Dedicated Service
────────────────────────────────────────────────────────
This service is the ONLY module that talks to ChromaDB.
No other part of the application should import `chromadb` directly.

Why? Single Responsibility + Encapsulation:
- If you switch from ChromaDB to Pinecone tomorrow, you change ONE file.
- The embedding client is initialized ONCE and reused (no repeated setup).
- Connection management and error handling live in one place.

Embedding Model: BAAI/bge-small-en-v1.5 (via HuggingFace Inference API)
─────────────────────────────────────────────────────────────────────────
- Runs on HuggingFace's servers (NOT locally — no torch needed)
- 384-dimensional embeddings
- Uses your HUGGINGFACEHUB_API_TOKEN for authentication
- Free tier is sufficient for ingestion workloads

Why huggingface_hub directly instead of LangChain?
───────────────────────────────────────────────────
- huggingface_hub is already installed (chromadb dependency)
- Zero extra dependencies — no langchain, no torch, no sentence-transformers
- Direct API call, no abstraction layers that can break on version updates
- We can always add LangChain later for the chat pipeline if needed

ChromaDB Cloud
───────────────
- We use chromadb.CloudClient — NOT PersistentClient
- Credentials come from environment variables (never hardcoded)
- The collection is created on first use if it doesn't exist

Usage:
    from app.services.vector_store import store_chunks

    store_chunks(
        chunks=["text chunk 1", "text chunk 2"],
        metadatas=[{"source": "resume.pdf", ...}, ...],
        doc_id="doc_resume_abc123"
    )
"""

import hashlib
from typing import Any, Optional

import numpy as np
import chromadb
from huggingface_hub import InferenceClient

from app.config import settings
from app.utils.logger import logger


# ── Module-level singletons ─────────────────────────────────
# These are initialized once on first use and reused.
# In Python, module-level variables persist for the lifetime of the process.
# This is equivalent to a singleton pattern in Node.js.
_chroma_client: Optional[Any] = None     # chromadb CloudClient
_collection: Optional[Any] = None        # chromadb Collection
_hf_client: Optional[InferenceClient] = None


def _get_chroma_client() -> Any:
    """
    Get or create the ChromaDB Cloud client (singleton).

    The client is created once and reused for all requests.
    This avoids re-authenticating on every request.
    """
    global _chroma_client

    if _chroma_client is None:
        logger.info("Initializing ChromaDB Cloud client...")
        _chroma_client = chromadb.CloudClient(
            api_key=settings.CHROMA_API_KEY,
            tenant=settings.CHROMA_TENANT,
            database=settings.CHROMA_DATABASE,
        )
        logger.info(
            f"Connected to ChromaDB Cloud "
            f"(tenant={settings.CHROMA_TENANT}, db={settings.CHROMA_DATABASE})"
        )

    return _chroma_client


def get_collection() -> Any:
    """
    Get or create the ChromaDB collection (singleton).

    A collection in ChromaDB is like a table in a database.
    All document chunks go into one collection for this app.
    """
    global _collection

    if _collection is None:
        client = _get_chroma_client()
        _collection = client.get_or_create_collection(
            name=settings.CHROMA_COLLECTION_NAME,
            metadata={"description": "EkanshGPT document embeddings"},
        )
        logger.info(f"Using collection: '{settings.CHROMA_COLLECTION_NAME}'")

    return _collection


def _get_hf_client() -> InferenceClient:
    """
    Get or create the HuggingFace Inference client (singleton).

    Uses the HuggingFace Inference API to generate embeddings remotely.
    The model (BAAI/bge-small-en-v1.5) runs on HuggingFace's servers,
    NOT locally — no torch or sentence-transformers needed.
    """
    global _hf_client

    if _hf_client is None:
        logger.info("Initializing HuggingFace Inference client...")
        _hf_client = InferenceClient(
            token=settings.HUGGINGFACEHUB_API_TOKEN,
        )
        logger.info(
            f"HuggingFace client ready "
            f"(model={settings.EMBEDDING_MODEL_NAME})"
        )

    return _hf_client


def generate_embeddings(texts: list[str]) -> list[list[float]]:
    """
    Generate embeddings for a list of texts via HuggingFace Inference API.

    Uses feature_extraction endpoint to get embeddings from
    BAAI/bge-small-en-v1.5 running on HuggingFace servers.

    Args:
        texts: List of text strings to embed.

    Returns:
        List of embedding vectors (each is a list of 384 floats).
    """
    client = _get_hf_client()
    embeddings = []

    for text in texts:
        # feature_extraction returns a numpy array of shape (384,)
        result = client.feature_extraction(
            text,
            model=settings.EMBEDDING_MODEL_NAME,
        )
        # Convert numpy array to plain Python list for ChromaDB
        embedding = np.array(result).flatten().tolist()
        embeddings.append(embedding)

    logger.debug(
        f"Generated {len(embeddings)} embeddings "
        f"(dim={len(embeddings[0]) if embeddings else 0})"
    )
    return embeddings


def store_chunks(
    chunks: list[str],
    metadatas: list[dict[str, Any]],
    doc_id: str,
) -> int:
    """
    Store text chunks with their embeddings and metadata in ChromaDB.

    This is the final step of the ingestion pipeline:
    1. Generate embeddings via HuggingFace Inference API
    2. Create unique IDs based on content hash (deduplication)
    3. Upsert into ChromaDB Cloud (insert or update if ID exists)

    Args:
        chunks: List of text chunks to store.
        metadatas: List of metadata dicts, one per chunk.
        doc_id: Base document ID for generating chunk IDs.

    Returns:
        Number of chunks stored.
    """
    if not chunks:
        logger.warning("No chunks to store — skipping.")
        return 0

    collection = get_collection()

    # Generate embeddings for all chunks
    logger.info(f"Generating embeddings for {len(chunks)} chunks...")
    embeddings = generate_embeddings(chunks)

    # Generate unique IDs for each chunk using content hash
    # This prevents duplicate chunks if the same document is uploaded twice.
    ids = [
        f"{doc_id}_chunk_{i}_{_content_hash(chunk)}"
        for i, chunk in enumerate(chunks)
    ]

    # Upsert into ChromaDB Cloud
    # upsert = insert if new, update if ID already exists
    logger.info(f"Upserting {len(chunks)} chunks into ChromaDB Cloud...")
    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
    )

    logger.info(
        f"✅ Stored {len(chunks)} chunks in collection "
        f"'{settings.CHROMA_COLLECTION_NAME}'"
    )
    return len(chunks)


def _content_hash(text: str) -> str:
    """
    Generate a short hash of text content for deduplication.

    Using first 8 chars of SHA-256 — collision-resistant enough
    for our scale (thousands of chunks, not billions).
    """
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:8]
