from scripts.generate_retrieval_fixtures import build_fixtures_from_chunks


def test_fixture_builder_maps_required_fields() -> None:
    rows = [
        {
            "chunk_id": "acts:p1:c1",
            "book_title": "Acts of Peter",
            "source_file": "11. Acts of Peter.pdf",
            "page_number": 1,
            "text": "Sample witness text.",
        }
    ]

    fixtures = build_fixtures_from_chunks(rows, max_items=1)

    assert len(fixtures) == 1
    expected = fixtures[0]["expected"]
    assert expected["book_title"] == "Acts of Peter"
    assert expected["source_file"] == "11. Acts of Peter.pdf"
    assert expected["page_number"] == 1
