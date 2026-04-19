from app.services.orchestrator import answer_query


def test_response_includes_four_part_structure() -> None:
    response = answer_query("What is the witness concerning steadfastness?")

    assert response["invocation"]
    assert response["witness"]
    assert response["exhortation"]
    assert response["reflection"]


def test_response_includes_at_least_one_citation() -> None:
    response = answer_query("Show one testimony.")
    assert response["citations"], "Expected at least one citation in evidence-backed response."
