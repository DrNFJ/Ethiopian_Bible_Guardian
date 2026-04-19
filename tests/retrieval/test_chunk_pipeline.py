from rag.ingest.chunker import chunk_page_text


def test_chunk_pipeline_emits_required_provenance_fields() -> None:
    chunks = chunk_page_text(
        source_file="11. Acts of Peter.pdf",
        page_number=3,
        text="In steadfast witness, the elders spoke with clarity.",
        max_chars=20,
    )

    assert chunks
    first = chunks[0]
    assert first.book_title == "Acts of Peter"
    assert first.source_file == "11. Acts of Peter.pdf"
    assert first.page_number == 3
    assert first.chunk_id
