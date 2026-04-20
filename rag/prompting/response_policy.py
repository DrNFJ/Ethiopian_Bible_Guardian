from rag.citations.formatter import citations_from_chunks
from rag.models import OrchestratedResponse, RetrievalResult
from rag.prompting.templates import (
    build_exhortation,
    build_invocation,
    build_reflection,
    build_witness,
)


def compose_response(query: str, retrieval: RetrievalResult) -> OrchestratedResponse:
    low_confidence = not retrieval.chunks or retrieval.confidence < 0.55
    citations = citations_from_chunks(retrieval.chunks)

    return OrchestratedResponse(
        invocation=build_invocation(),
        witness=build_witness(retrieval.chunks, low_confidence=low_confidence),
        exhortation=build_exhortation(query, low_confidence=low_confidence),
        reflection=build_reflection(low_confidence=low_confidence),
        citations=citations,
    )
