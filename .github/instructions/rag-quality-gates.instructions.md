---
description: "Use when implementing or modifying RAG ingestion, indexing, retrieval, reranking, citation formatting, or response orchestration for the Ethiopian-canon assistant. Enforces evidence-first generation, citation checks, and safety gates."
name: "RAG Retrieval and Citation Quality Gates"
applyTo: "rag/**"
---

# RAG Retrieval and Citation Quality Gates

Primary policy source: [AGENTS.md](../../AGENTS.md)

## Required Gates

- Retrieve before generation: never draft answer content until retrieval candidates are available.
- Preserve evidence boundaries: separate retrieved evidence from interpretation.
- Require citation for doctrinal or historical claims.
- Never fabricate chapter or verse labels.
- If retrieval confidence is low, explicitly state uncertainty and ask permission to broaden search.

## Required Chunk Metadata

- `book_title`
- `source_file`
- `page_number`
- `chunk_id`

## Implementation Rules

- Keep original PDFs in `corpus/` read-only unless explicitly requested otherwise.
- Prefer semantic retrieval with keyword fallback for rare names or transliterations.
- Use reranking before final context assembly.
- Keep witness quotations short and source-faithful.

## Test Expectations For Changes In rag/

- Add or update at least one retrieval test when retrieval logic changes.
- Add or update at least one citation-format test when answer formatting changes.
- Add or update safety behavior tests when uncertainty or refusal logic changes.

## Completion Checklist

- Retrieval executes before response generation.
- Citation output includes source title, and page when available.
- Answer templates support Invocation, Witness, Exhortation, Reflection.
- Tests cover the changed behavior.
