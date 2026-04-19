import re
from pathlib import Path

from rag.models import ChunkRecord


def infer_book_title(source_file: str) -> str:
    """Normalize numeric prefixes from corpus filenames into display titles."""
    stem = Path(source_file).stem
    return re.sub(r"^\d+\.\s*", "", stem).strip()


def chunk_page_text(
    source_file: str,
    page_number: int,
    text: str,
    max_chars: int = 800,
) -> list[ChunkRecord]:
    """Create fixed-width text chunks while preserving provenance fields."""
    book_title = infer_book_title(source_file)
    normalized = " ".join(text.split())
    if not normalized:
        return []

    chunks: list[ChunkRecord] = []
    start = 0
    part = 1

    while start < len(normalized):
        piece = normalized[start : start + max_chars]
        chunk_id = f"{Path(source_file).stem}:p{page_number}:c{part}"
        chunks.append(
            ChunkRecord(
                chunk_id=chunk_id,
                book_title=book_title,
                source_file=source_file,
                page_number=page_number,
                text=piece,
            )
        )
        start += max_chars
        part += 1

    return chunks
