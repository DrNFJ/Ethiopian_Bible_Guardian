import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHUNKS_FILE = ROOT / "data" / "chunks" / "chunks.jsonl"
OUT_FILE = ROOT / "tests" / "fixtures" / "retrieval_fixtures.json"


def load_chunk_rows() -> list[dict]:
    if not CHUNKS_FILE.exists():
        raise FileNotFoundError(
            f"Missing chunk artifact: {CHUNKS_FILE}. Run scripts/extract_chunks.py first."
        )

    rows: list[dict] = []
    for line in CHUNKS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        rows.append(json.loads(line))
    return rows


def build_fixtures_from_chunks(rows: list[dict], max_items: int = 25) -> list[dict]:
    fixtures: list[dict] = []

    for row in rows[:max_items]:
        fixtures.append(
            {
                "query": f"Show witness from {row['book_title']}",
                "expected": {
                    "book_title": row["book_title"],
                    "source_file": row["source_file"],
                    "page_number": row["page_number"],
                },
            }
        )

    return fixtures


def main() -> None:
    rows = load_chunk_rows()
    if not rows:
        raise RuntimeError(
            "Chunk artifact exists but has no rows. Re-run scripts/extract_chunks.py and verify extraction output."
        )
    fixtures = build_fixtures_from_chunks(rows)

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps(fixtures, indent=2), encoding="utf-8")
    print(f"Wrote {len(fixtures)} fixtures to {OUT_FILE}")


if __name__ == "__main__":
    main()
