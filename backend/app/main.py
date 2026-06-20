"""
EkanshGPT Backend — Main Application
======================================
This is the entry point for the FastAPI application.
Think of it as your server.js / app.js in Express.

Run with:
    uvicorn app.main:app --reload --port 8000

Then visit:
    http://localhost:8000/docs   — Interactive API docs (Swagger UI)
    http://localhost:8000/redoc  — Alternative docs (ReDoc)
    http://localhost:8000/api/health — Health check
"""

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.models.schemas import HealthResponse
from app.routers import ingest, chat
from app.utils.logger import logger


# ── Lifespan Event ──────────────────────────────────────────
# This replaces the old @app.on_event("startup") / ("shutdown") pattern.
# It runs setup code before the server starts accepting requests,
# and cleanup code when the server shuts down.
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup and shutdown lifecycle."""

    # ── Startup ─────────────────────────────────────────────
    logger.info("🚀 Starting EkanshGPT Backend...")

    # Ensure required directories exist
    # Note: No ChromaDB dir needed — we use ChromaDB Cloud
    Path(settings.UPLOAD_DIR).mkdir(parents=True, exist_ok=True)
    Path("logs").mkdir(parents=True, exist_ok=True)

    logger.info(f"📁 Upload directory:   {settings.upload_dir}")
    logger.info(f"☁️  ChromaDB Cloud:     {settings.CHROMA_DATABASE}")
    logger.info(f"🧠 Embedding model:    {settings.EMBEDDING_MODEL_NAME}")
    logger.info("✅ EkanshGPT Backend is ready!")

    yield  # Server is running and accepting requests

    # ── Shutdown ────────────────────────────────────────────
    logger.info("👋 Shutting down EkanshGPT Backend...")


# ── Create FastAPI App ──────────────────────────────────────
app = FastAPI(
    title="EkanshGPT API",
    description=(
        "RAG-powered AI assistant backend for Ekansh's portfolio. "
        "Handles document ingestion, embedding generation, and retrieval."
    ),
    version="0.1.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)


# ── CORS Middleware ─────────────────────────────────────────
# Allow the React + Vite frontend to make requests to this API.
# In production, replace "*" with your actual frontend domain.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://ekanshsatsangi.netlify.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Register Routers ───────────────────────────────────────
# Each router is like an Express Router — a group of related endpoints.
# The prefix means all routes in ingest.py start with /api/ingest/...
app.include_router(ingest.router, prefix="/api/ingest", tags=["Ingestion"])
app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])


# ── Health Check Endpoint ───────────────────────────────────
@app.get(
    "/api/health",
    response_model=HealthResponse,
    tags=["System"],
    summary="Health check",
    description="Returns the current health status of the EkanshGPT backend.",
)
async def health_check() -> HealthResponse:
    """
    Health check endpoint.

    Returns a simple status response to verify the server is running.
    This is the first endpoint to test after setting up the project.
    """
    return HealthResponse()


# ── Root Redirect ───────────────────────────────────────────
@app.get("/", include_in_schema=False)
async def root():
    """Redirect root to API docs for convenience."""
    return {
        "message": "Welcome to EkanshGPT API",
        "docs": "/docs",
        "health": "/api/health",
    }
