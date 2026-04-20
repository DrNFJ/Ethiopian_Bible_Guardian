from rag.citations.formatter import format_citation
from rag.models import Citation
from rag.models import RetrievalResult
from rag.prompting.response_policy import compose_response


def test_citation_contains_source_title_and_page_when_available() -> None:
    citation = Citation(
        source_file="11. Acts of Peter.pdf",
        book_title="Acts of Peter",
        page_number=4,
    )
    line = format_citation(citation)

    assert "Acts of Peter" in line
    assert "11. Acts of Peter.pdf" in line
    assert "p.4" in line


def test_low_confidence_text_does_not_invent_chapter_or_verse() -> None:
    retrieval = RetrievalResult(chunks=[], confidence=0.0, used_lexical_fallback=False)
    response = compose_response("Give doctrine from this witness.", retrieval=retrieval)
    full = f"{response.witness} {response.exhortation} {response.reflection}".lower()

    assert "chapter" not in full
    assert "verse" not in full
