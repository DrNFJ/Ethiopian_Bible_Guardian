import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from rag.ingest.pipeline import build_chunks_for_pdf, write_chunks_jsonl

CORPUS_DIR = ROOT / "corpus"
CHUNKS_FILE = ROOT / "data" / "chunks" / "chunks.jsonl"
SUMMARY_FILE = ROOT / "data" / "chunks" / "summary.json"


def build_corpus_chunks(max_chars: int = 800) -> list:
    all_chunks = []
    for pdf_path in sorted(CORPUS_DIR.glob("*.pdf")):
        all_chunks.extend(build_chunks_for_pdf(pdf_path=pdf_path, max_chars=max_chars))
    return all_chunks


def main() -> None:
    chunks = build_corpus_chunks()
    write_chunks_jsonl(chunks=chunks, out_file=CHUNKS_FILE)

    summary = {
        "source_pdfs": len(list(CORPUS_DIR.glob("*.pdf"))),
        "chunk_count": len(chunks),
        "output": str(CHUNKS_FILE.relative_to(ROOT)).replace("\\", "/"),
    }
    SUMMARY_FILE.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_FILE.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(f"Wrote {len(chunks)} chunks to {CHUNKS_FILE}")
    print(f"Wrote summary to {SUMMARY_FILE}")


if __name__ == "__main__":
    main()
