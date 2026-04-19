import json

from rag.retrieve import retriever


def test_retriever_uses_chunk_artifacts_when_available(tmp_path) -> None:
    chunks_file = tmp_path / "chunks.jsonl"
    row = {
        "chunk_id": "acts:p1:c1",
        "book_title": "Acts of Peter",
        "source_file": "11. Acts of Peter.pdf",
        "page_number": 1,
        "text": "Steadfast witness and prayer were kept by the elders.",
    }
    chunks_file.write_text(json.dumps(row) + "\n", encoding="utf-8")

    original = retriever.CHUNKS_FILE
    retriever.CHUNKS_FILE = chunks_file
    try:
        result = retriever.retrieve_candidates("steadfast witness", top_k=3)
    finally:
        retriever.CHUNKS_FILE = original

    assert result.chunks
    assert result.chunks[0].source_file == "11. Acts of Peter.pdf"
    assert result.used_lexical_fallback is False


def test_retriever_falls_back_to_lexical_when_semantic_misses(tmp_path) -> None:
    chunks_file = tmp_path / "chunks.jsonl"
    row = {
        "chunk_id": "acts:p1:c1",
        "book_title": "Acts of Peter",
        "source_file": "11. Acts of Peter.pdf",
        "page_number": 1,
        "text": "The witness was kept in the assembly.",
    }
    chunks_file.write_text(json.dumps(row) + "\n", encoding="utf-8")

    original = retriever.CHUNKS_FILE
    retriever.CHUNKS_FILE = chunks_file
    original_semantic = retriever._semantic_score
    retriever._semantic_score = lambda query, text: 0.0
    try:
        result = retriever.retrieve_candidates("assembly", top_k=3)
    finally:
        retriever.CHUNKS_FILE = original
        retriever._semantic_score = original_semantic

    assert result.chunks
    assert result.used_lexical_fallback is True
