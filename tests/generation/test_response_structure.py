from app.services.orchestrator import answer_query
from rag.models import RetrievalResult
from rag.prompting.response_policy import compose_response


def test_response_includes_four_part_structure() -> None:
    response = answer_query("What is the witness concerning steadfastness?")

    assert response["invocation"]
    assert response["witness"]
    assert response["exhortation"]
    assert response["reflection"]


def test_response_includes_at_least_one_citation() -> None:
    response = answer_query("Show one testimony.")
    assert response["citations"], "Expected at least one citation in evidence-backed response."


def test_low_confidence_response_requests_broader_search() -> None:
    retrieval = RetrievalResult(chunks=[], confidence=0.0, used_lexical_fallback=False)

    response = compose_response("What witness is given for steadfastness?", retrieval=retrieval)

    assert "Retrieved evidence:" in response.witness
    assert "Traditional interpretation" in response.exhortation
    assert "broaden retrieval" in response.exhortation.lower() or "widen the search" in response.reflection.lower()
