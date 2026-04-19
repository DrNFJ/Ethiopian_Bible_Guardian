import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = ROOT / "corpus"
OUT_FILE = ROOT / "data" / "raw" / "corpus_manifest.json"


def normalize_title(file_name: str) -> str:
    stem = Path(file_name).stem
    return re.sub(r"^\d+\.\s*", "", stem).strip()


def build_manifest() -> list[dict]:
    files = sorted(CORPUS_DIR.glob("*.pdf"))
    manifest: list[dict] = []

    for idx, file_path in enumerate(files, start=1):
        manifest.append(
            {
                "id": idx,
                "book_title": normalize_title(file_path.name),
                "source_file": file_path.name,
                "path": str(file_path.relative_to(ROOT)).replace("\\", "/"),
            }
        )

    return manifest


def main() -> None:
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    manifest = build_manifest()
    OUT_FILE.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote {len(manifest)} entries to {OUT_FILE}")


if __name__ == "__main__":
    main()
