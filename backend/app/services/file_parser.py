"""
File Parser Service
=====================
Extracts plain text from uploaded documents (PDF, TXT, Markdown).

Why is this its own service?
─────────────────────────────
In Node.js, you might put parsing logic directly in the route handler.
In a production Python app, we isolate it because:

1. **Testability** — You can test parsing without HTTP. Just call parse("file.pdf").
2. **Extensibility** — Adding DOCX support later means editing ONE file, not your route.
3. **Separation of concerns** — The router doesn't need to know HOW text is extracted.

Why PyMuPDF (fitz) over PyPDF2?
─────────────────────────────────
PyMuPDF handles formatted documents (resumes, reports with tables/columns)
much more reliably. PyPDF2 often produces garbled output on complex PDFs.

Usage:
    from app.services.file_parser import parse

    text = parse(Path("uploads/resume.pdf"))
"""

import re
from pathlib import Path

import fitz  # PyMuPDF — the import name differs from the package name
import markdown as md

from app.utils.logger import logger


# File extensions this parser supports
SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".md"}


def parse(file_path: Path) -> str:
    """
    Extract plain text from a file based on its extension.

    This is the single entry point — it dispatches to the right
    parser internally. Think of it like a factory pattern.

    Args:
        file_path: Path to the file to parse.

    Returns:
        Extracted plain text as a string.

    Raises:
        ValueError: If the file extension is not supported.
        FileNotFoundError: If the file doesn't exist.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = file_path.suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: '{extension}'. "
            f"Supported: {', '.join(SUPPORTED_EXTENSIONS)}"
        )

    logger.info(f"Parsing file: {file_path.name} (type: {extension})")

    # Dispatch to the right parser
    parsers = {
        ".pdf": _parse_pdf,
        ".txt": _parse_txt,
        ".md": _parse_markdown,
    }

    text = parsers[extension](file_path)

    # Clean up: normalize whitespace, strip leading/trailing space
    text = _clean_text(text)

    logger.info(f"Extracted {len(text)} characters from {file_path.name}")
    return text


def _parse_pdf(file_path: Path) -> str:
    """
    Extract text from a PDF using PyMuPDF (fitz).

    PyMuPDF reads each page and extracts text while preserving
    reading order — even for multi-column layouts.
    """
    text_parts = []

    with fitz.open(file_path) as doc:
        for page_num, page in enumerate(doc, start=1):
            page_text = page.get_text()
            if page_text.strip():
                text_parts.append(page_text)
                logger.debug(f"  Page {page_num}: {len(page_text)} chars")

    if not text_parts:
        logger.warning(f"No text extracted from PDF: {file_path.name}")

    return "\n".join(text_parts)


def _parse_txt(file_path: Path) -> str:
    """
    Read a plain text file.

    Simple, but we still handle encoding gracefully.
    """
    return file_path.read_text(encoding="utf-8")


def _parse_markdown(file_path: Path) -> str:
    """
    Extract plain text from a Markdown file.

    Strategy: Convert MD → HTML → strip HTML tags.
    This removes formatting (headers, bold, links) while keeping the content.
    """
    raw_md = file_path.read_text(encoding="utf-8")

    # Convert Markdown to HTML
    html = md.markdown(raw_md)

    # Strip HTML tags to get plain text
    plain_text = re.sub(r"<[^>]+>", "", html)

    return plain_text


def _clean_text(text: str) -> str:
    """
    Normalize extracted text.

    - Collapse multiple newlines into double newlines (paragraph breaks)
    - Collapse multiple spaces into single spaces
    - Strip leading/trailing whitespace
    """
    # Collapse 3+ newlines into 2 (preserve paragraph breaks)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Collapse multiple spaces into one
    text = re.sub(r" {2,}", " ", text)

    return text.strip()
