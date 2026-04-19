from rag.citations.formatter import format_citation_block
from rag.prompting.response_policy import compose_response
from rag.retrieve.rerank import rerank_candidates
from rag.retrieve.retriever import retrieve_candidates


def answer_query(query: str, top_k: int = 5) -> dict:
    retrieval = retrieve_candidates(query=query, top_k=top_k)
    reranked = rerank_candidates(retrieval.chunks, query=query)
    retrieval = retrieval.__class__(
        chunks=reranked,
        confidence=retrieval.confidence,
        used_lexical_fallback=retrieval.used_lexical_fallback,
    )

    response = compose_response(query=query, retrieval=retrieval)
    return {
        "invocation": response.invocation,
        "witness": response.witness,
        "exhortation": response.exhortation,
        "reflection": response.reflection,
        "citations": [
            {
                "book_title": c.book_title,
                "source_file": c.source_file,
                "page_number": c.page_number,
            }
            for c in response.citations
        ],
        "citation_block": format_citation_block(response.citations),
    }
