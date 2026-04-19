---
name: rag-conversation-lead
description: "Design, scaffold, or refine a RAG pipeline for the Ethiopian canon assistant with solemn tone, citation-first answering, and a four-part conversation-leading response format (Invocation, Witness, Exhortation, Reflection). Use when: building ingestion/indexing/retrieval, prompt orchestration, citation formatting, or dialogue policy."
---

# RAG Conversation Lead Skill

## Outcome

Produce or improve a retrieval-grounded assistant that leads each response with sacred tone and explicit source evidence.

## Inputs

- Corpus location: `corpus/`
- User objective: feature, fix, or evaluation task
- Constraints: no fabrication, citation-required for doctrinal claims

## Workflow

1. Inspect the corpus and confirm source availability.
2. Preserve source integrity:
   - Never alter original PDFs in `corpus/` by default.
3. Implement or verify ingestion with provenance:
   - Extract text with page association.
   - Emit chunk metadata (`book_title`, `source_file`, `page_number`, `chunk_id`).
4. Implement or verify retrieval:
   - Semantic retrieval first.
   - Optional lexical fallback for rare names/phrases.
   - Rerank before generation.
5. Apply response orchestration policy:
   - Invocation: concise sacred framing.
   - Witness: retrieved excerpts and citations.
   - Exhortation: clear answer grounded in evidence.
   - Reflection: one guiding follow-up question.
6. Enforce uncertainty handling:
   - If evidence is weak, state uncertainty and request scope expansion.
7. Validate with tests/evals:
   - Retrieval relevance checks.
   - Citation presence checks.
   - Style and safety checks.

## Citation Rules

- Do not emit unsupported claims.
- Cite source title each time evidence is used.
- Include page number when available from extraction.
- Keep quotes short and faithful to extracted text.

## Tone Rules

- Maintain solemn, ancient, reverent style.
- Avoid modern slang and comedic phrasing.
- Keep language understandable for non-specialists.

## Anti-Patterns To Avoid

- Answering before retrieval.
- Blending interpretation and evidence without labels.
- Fabricating chapter/verse numbering.
- Overly long monologues without a guiding reflection prompt.

## Deliverable Checklist

- Ingestion and retrieval are provenance-aware.
- Final answer format follows the four-part structure.
- At least one citation appears for evidence-backed answers.
- Uncertainty behavior is explicit and user-visible.
