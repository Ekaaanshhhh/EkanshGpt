"""
EkanshGPT Data Schemas
========================
Pydantic models for request/response validation.

These are like Zod or Joi schemas in Node.js — they define the
shape of data and FastAPI uses them to auto-validate requests
and auto-generate API docs.

Usage:
    from app.models.schemas import DocumentCategory, IngestResponse
"""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# ── Document Taxonomy ───────────────────────────────────────
# Predefined categories for filtering during retrieval.
# Using an Enum ensures only valid categories are accepted.
class DocumentCategory(str, Enum):
    """
    Document taxonomy for the EkanshGPT knowledge base.

    Each category maps to a type of content about Ekansh:
    - resume:      CV, resume documents
    - project:     Project descriptions (ReelOps, MediSaar, etc.)
    - achievement: Awards, hackathon wins, certifications
    - experience:  Work experience, internships
    - education:   Degrees, courses, academic records
    - blog:        Blog posts, articles, write-ups
    """

    RESUME = "resume"
    PROJECT = "project"
    ACHIEVEMENT = "achievement"
    EXPERIENCE = "experience"
    EDUCATION = "education"
    BLOG = "blog"


# ── Response Models ─────────────────────────────────────────
class HealthResponse(BaseModel):
    """Response schema for the /health endpoint."""

    status: str = Field(default="healthy", examples=["healthy"])
    service: str = Field(default="ekanshgpt-backend", examples=["ekanshgpt-backend"])
    version: str = Field(default="0.1.0", examples=["0.1.0"])
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class IngestResponse(BaseModel):
    """Response schema returned after a successful document ingestion."""

    status: str = Field(examples=["success"])
    document_id: str = Field(
        description="Unique identifier for the ingested document",
        examples=["doc_resume_2024abc"],
    )
    chunks_stored: int = Field(
        description="Number of text chunks created and stored",
        examples=[12],
    )
    message: str = Field(examples=["Document ingested successfully"])


class URLIngestRequest(BaseModel):
    """Request schema for ingesting a document from a URL."""

    url: str = Field(
        description="Publicly accessible URL to the PDF, TXT, or MD file",
        examples=["https://example.com/ekansh_resume.pdf"],
    )
    category: DocumentCategory = Field(
        description="Document taxonomy category",
        examples=["resume"],
    )
    document_name: str = Field(
        description="Human-readable name for the document",
        examples=["Ekansh's Resume"],
    )


class DocumentMetadata(BaseModel):
    """
    Metadata attached to each document during ingestion.

    This metadata is stored alongside every chunk in ChromaDB
    and enables filtered retrieval later.
    """

    source: str = Field(
        description="Original filename",
        examples=["resume.pdf"],
    )
    category: DocumentCategory = Field(
        description="Document taxonomy category",
        examples=["resume"],
    )
    document_name: str = Field(
        description="Human-readable document name",
        examples=["Ekansh's Resume"],
    )
    document_type: str = Field(
        description="Specific document type within the category",
        examples=["pdf", "markdown", "text"],
    )
    owner: str = Field(
        default="ekansh",
        description="Document owner identifier",
        examples=["ekansh"],
    )
    uploaded_at: Optional[datetime] = Field(
        default=None,
        description="Upload timestamp (auto-set if not provided)",
    )


class ErrorResponse(BaseModel):
    """Standard error response schema."""

    status: str = Field(default="error", examples=["error"])
    message: str = Field(examples=["File type not supported"])
    detail: Optional[str] = Field(
        default=None,
        examples=["Only .pdf, .txt, and .md files are accepted"],
    )


# ── Chat Models ─────────────────────────────────────────────
class ChatRequest(BaseModel):
    """Request schema for asking a question."""

    question: str = Field(
        description="The user's question about Ekansh",
        examples=["Tell me about ReelOps"],
    )


class ChatResponse(BaseModel):
    """Response schema for chat endpoint."""

    answer: str = Field(
        description="The generated answer from the LLM",
        examples=["ReelOps is a content operations platform..."],
    )
    sources: list[str] = Field(
        description="List of document names used to generate the answer",
        examples=[["Resume", "ReelOps Summary"]],
    )
