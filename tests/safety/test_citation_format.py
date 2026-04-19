from rag.citations.formatter import format_citation
from rag.models import Citation


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
