import json
from dataclasses import asdict
from pathlib import Path

from rag.ingest.chunker import chunk_page_text
from rag.ingest.pdf_extract import extract_pdf_pages
from rag.models import ChunkRecord


def build_chunks_for_pdf(pdf_path: Path, max_chars: int = 800) -> list[ChunkRecord]:
    chunks: list[ChunkRecord] = []
    pages = extract_pdf_pages(pdf_path)

    for page in pages:
        chunks.extend(
            chunk_page_text(
                source_file=page["source_file"],
                page_number=page["page_number"],
                text=page["text"],
                max_chars=max_chars,
            )
        )

    return chunks


def write_chunks_jsonl(chunks: list[ChunkRecord], out_file: Path) -> None:
    out_file.parent.mkdir(parents=True, exist_ok=True)
    lines = [asdict(chunk) for chunk in chunks]
    payload = "\n".join(json.dumps(line, ensure_ascii=False) for line in lines)
    if payload:
        payload += "\n"
    out_file.write_text(payload, encoding="utf-8")
