---
description: "Use when writing or updating tests for retrieval output, citation formatting, or response policy checks. Enforces citation-style assertions for the Ethiopian-canon RAG assistant."
name: "Tests Citation Assertions"
applyTo: "tests/**"
---

# Tests Citation Assertions

Primary policy source: [AGENTS.md](../../AGENTS.md)
Companion RAG rules: [rag-quality-gates.instructions.md](./rag-quality-gates.instructions.md)

## Required Assertions For Relevant Test Changes

- Verify each evidence-backed answer includes at least one citation.
- Verify citation includes source title.
- Verify page number is present when extraction provides it.
- Verify no fabricated chapter or verse marker appears in generated output.

## Preferred Test Patterns

- Use explicit fixtures for retrieval candidates and expected citations.
- Keep assertions deterministic and avoid brittle full-string snapshots.
- Assert structured fields first, then rendered text.

## Minimum Coverage Expectations

- Retrieval behavior change: add a relevance-focused assertion.
- Citation formatter change: add a formatting-focused assertion.
- Prompt/orchestration change: add assertions for Invocation, Witness, Exhortation, Reflection sections.

## Failure Message Guidance

- Include source file and failing field in assertion messages.
- Explain whether failure is missing citation, malformed citation, or evidence-policy violation.
