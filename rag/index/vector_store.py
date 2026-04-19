from rag.models import RetrievedChunk


class InMemoryVectorStore:
    """Starter placeholder for embeddings and nearest-neighbor lookup."""

    def __init__(self) -> None:
        self._items: list[RetrievedChunk] = []

    def upsert(self, chunks: list[RetrievedChunk]) -> None:
        self._items.extend(chunks)

    def search(self, query: str, top_k: int = 5) -> list[RetrievedChunk]:
        _ = query
        return self._items[:top_k]
