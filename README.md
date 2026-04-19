# Ethiopian Bible Guardian

A citation-first RAG scaffold for a solemn, ancient-voiced assistant grounded in the Ethiopian canon corpus.

## Current Stage

This repository is initialized with starter modules for:
- Corpus manifest generation
- PDF extraction and chunking interfaces
- Retrieval and reranking interfaces
- Citation formatting and four-part response orchestration
- API entrypoint and baseline tests

## Layout

- app/: API and service orchestration
- rag/: ingestion, indexing, retrieval, prompting, citations
- data/: generated manifest, chunks, and index artifacts
- config/: retrieval and generation settings
- tests/: retrieval, generation, and safety checks
- scripts/: corpus and indexing tasks

## Quick Start

1. Create and activate a virtual environment.
2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Generate corpus manifest:

```powershell
python scripts/generate_manifest.py
```

4. Extract page-level chunks with provenance:

```powershell
python scripts/extract_chunks.py
```

5. Generate retrieval fixtures from chunks:

```powershell
python scripts/generate_retrieval_fixtures.py
```

6. Run tests:

```powershell
pytest
```

7. Start API:

```powershell
uvicorn app.api.main:app --reload
```

## Policy Notes

- Do not modify source files in corpus/ unless explicitly requested.
- Retrieval must happen before answer generation.
- Doctrinal or historical answers require citation(s).
- Output format is Invocation, Witness, Exhortation, Reflection.
