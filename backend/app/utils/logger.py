"""
EkanshGPT Logger Configuration
================================
Structured logging using loguru — think of it as Python's 'pino'.

Usage:
    from app.utils.logger import logger

    logger.info("Server started")
    logger.error("Something failed", exc_info=True)
    logger.debug("Processing file", file_name="resume.pdf")
"""

import sys

from loguru import logger

# ── Remove default loguru handler ───────────────────────────
# loguru comes with a default stderr handler. We remove it
# and add our own with custom formatting.
logger.remove()

# ── Console handler (development) ──────────────────────────
# Colorized, human-readable output for local development.
# Format: timestamp | level | module:function:line | message
logger.add(
    sys.stderr,
    level="DEBUG",
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    ),
    colorize=True,
)

# ── File handler (production) ──────────────────────────────
# JSON-structured logs written to a rotating file.
# Useful for log aggregation tools later.
logger.add(
    "logs/ekanshgpt_{time:YYYY-MM-DD}.log",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} | {message}",
    rotation="10 MB",      # Rotate when file hits 10MB
    retention="30 days",   # Keep logs for 30 days
    compression="zip",     # Compress rotated files
)
