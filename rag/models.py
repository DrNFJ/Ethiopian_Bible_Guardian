from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Citation:
    source_file: str
    book_title: str
    page_number: int | None


@dataclass(frozen=True)
class ChunkRecord:
    chunk_id: str
    book_title: str
    source_file: str
    page_number: int
    text: str


@dataclass(frozen=True)
class RetrievedChunk:
    chunk_id: str
    book_title: str
    source_file: str
    page_number: int
    text: str
    score: float


@dataclass(frozen=True)
class RetrievalResult:
    chunks: List[RetrievedChunk]
    confidence: float
    used_lexical_fallback: bool


@dataclass(frozen=True)
class OrchestratedResponse:
    invocation: str
    witness: str
    exhortation: str
    reflection: str
    citations: List[Citation]

    @property
    def full_text(self) -> str:
        return (
            f"Invocation: {self.invocation}\n\n"
            f"Witness: {self.witness}\n\n"
            f"Exhortation: {self.exhortation}\n\n"
            f"Reflection: {self.reflection}"
        )
