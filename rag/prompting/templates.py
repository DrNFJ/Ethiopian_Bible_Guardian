from rag.models import RetrievedChunk


def build_invocation() -> str:
    return "Peace be upon this inquiry, and let witness arise before interpretation."


def build_witness(chunks: list[RetrievedChunk], low_confidence: bool) -> str:
    if not chunks:
        return "Retrieved evidence: no supporting passage could be recovered from the present search."

    quotes = []
    for chunk in chunks[:2]:
        snippet = chunk.text[:180].strip()
        quotes.append(f'"{snippet}"')

    witness = "Retrieved evidence: " + " ".join(quotes)
    if low_confidence:
        witness += " Retrieval confidence is limited; these lines may be incomplete for a firm conclusion."
    return witness


def build_exhortation(query: str, low_confidence: bool) -> str:
    if low_confidence:
        return (
            "Traditional interpretation (bounded): the present witness is too thin for certainty. "
            "Grant leave to broaden retrieval if you seek firmer testimony across related texts."
        )
    return (
        "Traditional interpretation: from the witness presented, a faithful first answer is offered in humility: "
        f"{query.strip() or 'clarify your question so the witness may be sharper.'}"
    )


def build_reflection(low_confidence: bool) -> str:
    if low_confidence:
        return "Shall I widen the search across additional books to strengthen the witness?"
    return "Would you have me remain in this book, or compare witness across related texts?"
