from rag.models import RetrievedChunk


def rerank_candidates(chunks: list[RetrievedChunk], query: str) -> list[RetrievedChunk]:
    """Starter reranker: stable sort by score, then by chunk id."""
    _ = query
    return sorted(chunks, key=lambda c: (-c.score, c.chunk_id))
