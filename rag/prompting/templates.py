from rag.models import RetrievedChunk


def build_invocation() -> str:
    return "Peace be upon this inquiry, and let witness arise before interpretation."


def build_witness(chunks: list[RetrievedChunk], low_confidence: bool) -> str:
    if not chunks:
        return "No witness text could be retrieved from the corpus."

    quotes = []
    for chunk in chunks[:2]:
        snippet = chunk.text[:180].strip()
        quotes.append(f'"{snippet}"')

    witness = " ".join(quotes)
    if low_confidence:
        witness += " Retrieval confidence is low; broader search may be needed."
    return witness


def build_exhortation(query: str, low_confidence: bool) -> str:
    if low_confidence:
        return (
            "A bounded answer can be offered, yet confidence is limited by the present witness. "
            "Grant leave to broaden retrieval if you seek firmer testimony."
        )
    return (
        "From the witness presented, a faithful first answer is offered in humility: "
        f"{query.strip() or 'clarify your question so the witness may be sharper.'}"
    )


def build_reflection() -> str:
    return "Would you have me remain in this book, or compare witness across related texts?"
