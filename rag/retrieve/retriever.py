import json
import re
from pathlib import Path

from rag.models import RetrievalResult, RetrievedChunk

ROOT = Path(__file__).resolve().parents[2]
CHUNKS_FILE = ROOT / "data" / "chunks" / "chunks.jsonl"


def _tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9']+", text.lower()))


def _semantic_score(query: str, text: str) -> float:
    q_tokens = _tokenize(query)
    t_tokens = _tokenize(text)
    if not q_tokens or not t_tokens:
        return 0.0
    overlap = len(q_tokens.intersection(t_tokens))
    return overlap / len(q_tokens)


def _lexical_score(query: str, text: str) -> float:
    q_tokens = list(_tokenize(query))
    if not q_tokens:
        return 0.0
    lowered = text.lower()
    hits = sum(1 for token in q_tokens if token in lowered)
    return hits / len(q_tokens)


def _load_chunk_rows() -> list[dict]:
    if not CHUNKS_FILE.exists():
        return []

    rows: list[dict] = []
    for line in CHUNKS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        rows.append(json.loads(line))
    return rows


def _seed_result(top_k: int, query: str) -> RetrievalResult:
    seed = RetrievedChunk(
        chunk_id="seed:p1:c1",
        book_title="Acts of Peter",
        source_file="11. Acts of Peter.pdf",
        page_number=1,
        text="A seed witness passage is returned until index wiring is implemented.",
        score=0.42,
    )
    chunks = [seed][:top_k]
    confidence = 0.42 if query.strip() else 0.0
    return RetrievalResult(
        chunks=chunks,
        confidence=confidence,
        used_lexical_fallback=False,
    )


def retrieve_candidates(query: str, top_k: int = 5) -> RetrievalResult:
    """Retrieve from chunk artifacts with semantic-first and lexical fallback ranking."""
    rows = _load_chunk_rows()
    if not rows:
        return _seed_result(top_k=top_k, query=query)

    semantic_hits: list[RetrievedChunk] = []
    for row in rows:
        score = _semantic_score(query, row.get("text", ""))
        if score <= 0.0:
            continue
        semantic_hits.append(
            RetrievedChunk(
                chunk_id=row["chunk_id"],
                book_title=row["book_title"],
                source_file=row["source_file"],
                page_number=row["page_number"],
                text=row["text"],
                score=score,
            )
        )

    semantic_hits.sort(key=lambda c: c.score, reverse=True)
    ranked = semantic_hits[:top_k]
    used_lexical_fallback = False

    if not ranked:
        fallback_hits: list[RetrievedChunk] = []
        for row in rows:
            score = _lexical_score(query, row.get("text", ""))
            if score <= 0.0:
                continue
            fallback_hits.append(
                RetrievedChunk(
                    chunk_id=row["chunk_id"],
                    book_title=row["book_title"],
                    source_file=row["source_file"],
                    page_number=row["page_number"],
                    text=row["text"],
                    score=score,
                )
            )
        fallback_hits.sort(key=lambda c: c.score, reverse=True)
        ranked = fallback_hits[:top_k]
        used_lexical_fallback = True

    confidence = ranked[0].score if ranked else 0.0
    return RetrievalResult(
        chunks=ranked,
        confidence=confidence,
        used_lexical_fallback=used_lexical_fallback,
    )
