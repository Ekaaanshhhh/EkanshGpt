"""
EkanshGPT Backend Configuration
================================
Loads environment variables and exposes them as typed settings.

Think of this like a Node.js config module that reads from .env,
but with runtime type validation via Pydantic.

Usage:
    from app.config import settings
    print(settings.CHROMA_API_KEY)
"""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables / .env file.

    Pydantic automatically:
    - Reads from .env
    - Validates types (str, int, Path)
    - Raises clear errors if required vars are missing
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Ignore unexpected env vars without erroring
    )

    # ── ChromaDB Cloud ─────────────────────────────────────
    # Connection to ChromaDB Cloud — NEVER hardcode these.
    CHROMA_API_KEY: str
    CHROMA_TENANT: str
    CHROMA_DATABASE: str
    CHROMA_COLLECTION_NAME: str = "ekanshgpt_documents"

    # ── HuggingFace ────────────────────────────────────────
    # Token for HuggingFace API (used for chat model in future)
    HUGGINGFACEHUB_API_TOKEN: str
    
    # ── Groq ───────────────────────────────────────────────
    GROQ_API_KEY: str

    # ── Embedding Model ────────────────────────────────────
    # BAAI/bge-small-en-v1.5 runs locally — free, no API calls
    EMBEDDING_MODEL_NAME: str = "BAAI/bge-small-en-v1.5"

    # ── File Uploads ────────────────────────────────────────
    UPLOAD_DIR: str = "./uploads"

    # ── Server ──────────────────────────────────────────────
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

    # ── Chunking ────────────────────────────────────────────
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 50

    # ── Metadata ────────────────────────────────────────────
    DOCUMENT_OWNER: str = "ekansh"

    @property
    def upload_dir(self) -> Path:
        """Return upload directory as a resolved Path object."""
        return Path(self.UPLOAD_DIR).resolve()


# ── Singleton ───────────────────────────────────────────────
# Import this from anywhere: `from app.config import settings`
settings = Settings()
