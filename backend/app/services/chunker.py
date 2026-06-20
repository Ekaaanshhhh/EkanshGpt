"""
Text Chunker Service
======================
Splits extracted text into smaller, overlapping chunks for embedding.

Why chunk text?
────────────────
Embedding models have a maximum input length (typically 512 tokens).
Even if they didn't, smaller chunks produce more focused embeddings
that retrieve better. Think of it like indexing a book — you want
chapter-level entries, not one entry for the whole book.

Why overlap?
─────────────
If a sentence sits right at a chunk boundary, it gets split in half.
Overlap ensures both chunks contain the full sentence, so retrieval
can find it regardless of which chunk gets matched.

    Chunk 1: [=========|overlap|]
    Chunk 2:           [overlap|=========]

Usage:
    from app.services.chunker import chunk_text

    chunks = chunk_text("long document text...", chunk_size=500, overlap=50)
"""

import re

from app.config import settings
from app.utils.logger import logger


def chunk_text(
    text: str,
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[str]:
    """
    Split text into overlapping chunks using a recursive strategy.

    Strategy (from coarsest to finest):
    1. Try splitting on paragraph breaks (\\n\\n)
    2. If paragraphs are too large, split on sentences (. ! ?)
    3. If sentences are too large, split by character count

    This preserves semantic boundaries — a chunk is more likely to
    contain a complete thought.

    Args:
        text: The full text to chunk.
        chunk_size: Maximum characters per chunk. Defaults to settings.CHUNK_SIZE.
        overlap: Number of overlapping characters between chunks.
                 Defaults to settings.CHUNK_OVERLAP.

    Returns:
        List of text chunks. Empty list if input is empty.
    """
    if not text or not text.strip():
        return []

    chunk_size = chunk_size or settings.CHUNK_SIZE
    overlap = overlap or settings.CHUNK_OVERLAP

    # Step 1: Split into paragraphs
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

    # Step 2: Build chunks from paragraphs, respecting size limits
    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:
        # If this paragraph alone exceeds chunk_size, split it further
        if len(paragraph) > chunk_size:
            # Flush current chunk first
            if current_chunk:
                chunks.append(current_chunk.strip())
                current_chunk = ""

            # Split the oversized paragraph into sentences
            sentence_chunks = _split_by_sentences(paragraph, chunk_size)
            chunks.extend(sentence_chunks)
            continue

        # If adding this paragraph would exceed the limit, flush
        if len(current_chunk) + len(paragraph) + 2 > chunk_size:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = paragraph
        else:
            # Add paragraph to current chunk
            if current_chunk:
                current_chunk += "\n\n" + paragraph
            else:
                current_chunk = paragraph

    # Don't forget the last chunk
    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    # Step 3: Apply overlap between chunks
    if overlap > 0 and len(chunks) > 1:
        chunks = _apply_overlap(chunks, overlap)

    # Filter out any empty chunks
    chunks = [c for c in chunks if c.strip()]

    logger.info(
        f"Chunked {len(text)} chars into {len(chunks)} chunks "
        f"(size={chunk_size}, overlap={overlap})"
    )

    return chunks


def _split_by_sentences(text: str, chunk_size: int) -> list[str]:
    """
    Split text by sentence boundaries when paragraphs are too large.

    Uses regex to split on sentence-ending punctuation (. ! ?)
    followed by a space or end of string.
    """
    # Split on sentence boundaries (period, exclamation, question mark)
    sentences = re.split(r"(?<=[.!?])\s+", text)

    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 > chunk_size:
            if current_chunk:
                chunks.append(current_chunk.strip())
            # If a single sentence exceeds chunk_size, force-split it
            if len(sentence) > chunk_size:
                chunks.extend(_force_split(sentence, chunk_size))
                current_chunk = ""
            else:
                current_chunk = sentence
        else:
            if current_chunk:
                current_chunk += " " + sentence
            else:
                current_chunk = sentence

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks


def _force_split(text: str, chunk_size: int) -> list[str]:
    """
    Last resort: split text by character count when even sentences are too long.
    Tries to split on word boundaries to avoid cutting words in half.
    """
    chunks = []
    words = text.split()
    current_chunk = ""

    for word in words:
        if len(current_chunk) + len(word) + 1 > chunk_size:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = word
        else:
            if current_chunk:
                current_chunk += " " + word
            else:
                current_chunk = word

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks


def _apply_overlap(chunks: list[str], overlap: int) -> list[str]:
    """
    Add overlap between consecutive chunks.

    Takes the last `overlap` characters from the previous chunk
    and prepends them to the next chunk.
    """
    if not chunks:
        return chunks

    overlapped = [chunks[0]]

    for i in range(1, len(chunks)):
        prev_chunk = chunks[i - 1]

        # Get the overlap text from the end of the previous chunk
        overlap_text = prev_chunk[-overlap:] if len(prev_chunk) >= overlap else prev_chunk

        # Try to start overlap at a word boundary
        space_idx = overlap_text.find(" ")
        if space_idx != -1:
            overlap_text = overlap_text[space_idx + 1:]

        # Prepend overlap to current chunk
        overlapped.append(overlap_text + " " + chunks[i])

    return overlapped
