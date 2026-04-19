from rag.models import Citation, RetrievedChunk


def citations_from_chunks(chunks: list[RetrievedChunk]) -> list[Citation]:
    seen: set[tuple[str, int | None]] = set()
    citations: list[Citation] = []

    for chunk in chunks:
        key = (chunk.source_file, chunk.page_number)
        if key in seen:
            continue
        seen.add(key)
        citations.append(
            Citation(
                source_file=chunk.source_file,
                book_title=chunk.book_title,
                page_number=chunk.page_number,
            )
        )

    return citations


def format_citation(citation: Citation) -> str:
    if citation.page_number is None:
        return f"{citation.book_title} ({citation.source_file})"
    return f"{citation.book_title} ({citation.source_file}, p.{citation.page_number})"


def format_citation_block(citations: list[Citation]) -> str:
    return "\n".join(f"- {format_citation(c)}" for c in citations)
