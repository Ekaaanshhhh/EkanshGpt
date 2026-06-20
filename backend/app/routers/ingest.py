"""
Ingestion Router
==================
HTTP endpoints for document upload and ingestion.

This is like an Express Router — it defines endpoints and delegates
all business logic to the ingestion service.

The route handler's job:
1. Accept and validate the HTTP request
2. Save the uploaded file temporarily
3. Call the ingestion service (ONE call)
4. Clean up the temp file
5. Return the response

It should NOT contain business logic (parsing, chunking, embedding).
That's the orchestrator's job.

Endpoints:
    POST /api/ingest/upload — Upload and ingest a document
"""

import shutil
import urllib.request
import urllib.error
from urllib.parse import urlparse
from pathlib import Path

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.config import settings
from app.models.schemas import DocumentCategory, ErrorResponse, IngestResponse, URLIngestRequest
from app.services import ingestion_service
from app.services.file_parser import SUPPORTED_EXTENSIONS
from app.utils.logger import logger


router = APIRouter()


@router.post(
    "/upload",
    response_model=IngestResponse,
    responses={
        400: {"model": ErrorResponse, "description": "Invalid file type"},
        500: {"model": ErrorResponse, "description": "Ingestion failed"},
    },
    summary="Upload and ingest a document",
    description=(
        "Upload a PDF, TXT, or Markdown file to be parsed, chunked, "
        "embedded, and stored in ChromaDB for RAG retrieval."
    ),
)
async def upload_document(
    file: UploadFile = File(
        ...,
        description="The document file to ingest (PDF, TXT, or MD)",
    ),
    category: DocumentCategory = Form(
        ...,
        description="Document taxonomy category",
    ),
    document_name: str = Form(
        ...,
        description="Human-readable name for the document",
    ),
):
    """
    Upload and ingest a document into the EkanshGPT knowledge base.

    This endpoint:
    1. Validates the file type
    2. Saves it temporarily
    3. Runs the full ingestion pipeline (parse → chunk → embed → store)
    4. Cleans up the temp file
    5. Returns the result

    Form fields:
    - **file**: The document to upload (.pdf, .txt, or .md)
    - **category**: One of: resume, project, achievement, experience, education, blog
    - **document_name**: A human-readable name (e.g., "Ekansh's Resume")
    """
    # ── Validate file type ──────────────────────────────────
    if not file.filename:
        raise HTTPException(status_code=400, detail="No filename provided")

    file_ext = Path(file.filename).suffix.lower()
    if file_ext not in SUPPORTED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Unsupported file type: '{file_ext}'. "
                f"Accepted: {', '.join(SUPPORTED_EXTENSIONS)}"
            ),
        )

    # ── Save file temporarily ───────────────────────────────
    # We save to disk because PyMuPDF needs a file path (not bytes).
    # The file is deleted after processing.
    upload_path = settings.upload_dir / file.filename

    try:
        logger.info(f"Saving uploaded file: {file.filename}")
        with open(upload_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # ── Determine document_type from extension ──────────
        doc_type_map = {
            ".pdf": "pdf",
            ".txt": "text",
            ".md": "markdown",
        }
        document_type = doc_type_map.get(file_ext, "unknown")

        # ── Run the ingestion pipeline ──────────────────────
        result = ingestion_service.ingest_document(
            file_path=upload_path,
            source=file.filename,
            category=category.value,
            document_name=document_name,
            document_type=document_type,
        )

        return IngestResponse(
            status="success",
            document_id=result.document_id,
            chunks_stored=result.chunks_stored,
            message=f"Document '{document_name}' ingested successfully",
        )

    except ValueError as e:
        # Parsing or chunking errors (bad file content)
        logger.error(f"Ingestion validation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        # Unexpected errors (ChromaDB down, model loading failed, etc.)
        logger.error(f"Ingestion failed: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Ingestion failed: {str(e)}",
        )

    finally:
        # ── Clean up temp file ──────────────────────────────
        # Always runs, even if an exception occurred.
        # This is like a try-finally in Node.js.
        if upload_path.exists():
            upload_path.unlink()
            logger.debug(f"Cleaned up temp file: {upload_path}")


@router.post(
    "/upload-url",
    response_model=IngestResponse,
    responses={
        400: {"model": ErrorResponse, "description": "Invalid URL or file type"},
        500: {"model": ErrorResponse, "description": "Ingestion failed"},
    },
    summary="Ingest a document from a URL",
    description="Download a document from a URL and ingest it into the knowledge base.",
)
async def upload_document_url(request: URLIngestRequest):
    """
    Download and ingest a document from a public URL.

    This endpoint:
    1. Downloads the file from the provided URL
    2. Validates the file type extension
    3. Runs the full ingestion pipeline (parse → chunk → embed → store)
    4. Cleans up the temp file
    5. Returns the result
    """
    # ── Validate URL and extension ──────────────────────────
    parsed_url = urlparse(request.url)
    filename = Path(parsed_url.path).name
    
    if not filename or "." not in filename:
        filename = "downloaded_document.pdf"  # Fallback if no extension in URL
        
    file_ext = Path(filename).suffix.lower()
    if file_ext not in SUPPORTED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Unsupported file type from URL: '{file_ext}'. "
                f"Accepted: {', '.join(SUPPORTED_EXTENSIONS)}"
            ),
        )

    # ── Save file temporarily ───────────────────────────────
    upload_path = settings.upload_dir / filename

    try:
        logger.info(f"Downloading file from URL: {request.url}")
        
        # Add a basic user agent so generic hosts don't block the request
        req = urllib.request.Request(
            request.url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        
        with urllib.request.urlopen(req) as response, open(upload_path, "wb") as out_file:
            shutil.copyfileobj(response, out_file)

        # ── Determine document_type from extension ──────────
        doc_type_map = {
            ".pdf": "pdf",
            ".txt": "text",
            ".md": "markdown",
        }
        document_type = doc_type_map.get(file_ext, "unknown")

        # ── Run the ingestion pipeline ──────────────────────
        result = ingestion_service.ingest_document(
            file_path=upload_path,
            source=request.url,
            category=request.category.value,
            document_name=request.document_name,
            document_type=document_type,
        )

        return IngestResponse(
            status="success",
            document_id=result.document_id,
            chunks_stored=result.chunks_stored,
            message=f"Document '{request.document_name}' ingested successfully from URL",
        )

    except urllib.error.URLError as e:
        logger.error(f"Failed to download URL: {e}")
        raise HTTPException(
            status_code=400, 
            detail=f"Failed to download file from URL: {str(e)}"
        )
    except ValueError as e:
        # Parsing or chunking errors (bad file content)
        logger.error(f"Ingestion validation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Unexpected errors (ChromaDB down, model loading failed, etc.)
        logger.error(f"Ingestion failed: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Ingestion failed: {str(e)}",
        )
    finally:
        # ── Clean up temp file ──────────────────────────────
        if upload_path.exists():
            upload_path.unlink()
            logger.debug(f"Cleaned up temp file: {upload_path}")
