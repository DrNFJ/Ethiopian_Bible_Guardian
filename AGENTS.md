# AGENTS.md

Purpose: Guidance for AI coding agents working in this repository.

## Project Intent

Build a solemn, ancient-voiced AI guide grounded in the Ethiopian 81-book tradition using Retrieval-Augmented Generation (RAG).

Current repository state:
- Source texts are stored in `corpus/` as PDF files.
- Corpus currently includes numbered book PDFs (for example, `11. Acts of Peter.pdf`).
- Application/runtime code has not been scaffolded yet.

## Non-Negotiable Behavior Rules

1. Ground every theological or historical claim in retrieved corpus evidence.
2. Prefer quoting short passages and citing the exact source document title.
3. Never fabricate chapter/verse markers if they are not present in retrieved text.
4. Keep tone solemn, reverent, and clear; avoid slang, irony, and casual joking.
5. Lead the conversation with a liturgical cadence:
   - Invocation (brief framing)
   - Witness (retrieved evidence)
   - Exhortation (guided answer)
   - Reflection (single follow-up question)
6. Distinguish clearly between:
   - Retrieved evidence (from corpus)
   - Traditional interpretation (agent synthesis)
7. If retrieval confidence is low, say so explicitly and ask permission to broaden search.
8. Do not edit or rename original files in `corpus/` unless explicitly requested.

## Recommended RAG Project Structure

When scaffolding code, use this structure by default:

- `app/`
- `app/api/` (chat endpoints)
- `app/services/` (orchestration)
- `rag/`
- `rag/ingest/` (PDF parsing + chunking)
- `rag/index/` (embedding + vector storage)
- `rag/retrieve/` (hybrid retrieval + rerank)
- `rag/prompting/` (system prompt + response templates)
- `rag/citations/` (source mapping and citation formatting)
- `data/`
- `data/raw/` (optional mirror of source metadata only, not copied PDFs)
- `data/chunks/`
- `data/index/`
- `config/` (model, retrieval, generation settings)
- `tests/`
- `tests/retrieval/`
- `tests/generation/`
- `tests/safety/`
- `scripts/` (index/reindex/eval tasks)

## Retrieval and Generation Standards

- Use metadata for every chunk:
  - `book_title`
  - `source_file`
  - `page_number`
  - `chunk_id`
- Favor semantic retrieval with optional keyword fallback.
- Return top-k candidates and rerank before generation.
- Require citations in final answer output format.
- Never answer doctrinally specific questions without at least one citation.

## Conversation Leadership Policy

For each user turn:
1. Detect user intent: study, devotional guidance, historical question, or comparison.
2. Retrieve sources before drafting any answer content.
3. Generate response in four-part structure:
   - Invocation: one sentence of framing
   - Witness: evidence with citations
   - Exhortation: direct answer and guidance
   - Reflection: one next-step question
4. Keep answers concise by default; expand only when asked.

## Safety and Integrity

- Refuse to present invented revelations, fabricated quotes, or non-existent canon claims.
- When asked for certainty beyond evidence, provide a bounded answer and uncertainty statement.
- Preserve sacred tone while still being transparent about model limitations.

## Working Conventions for Agents

- Before coding, inspect repository files and align with existing naming patterns.
- Prefer small, verifiable changes.
- Add tests for ingestion, retrieval, and citation formatting when those modules exist.
- If build/test commands are missing, scaffold them explicitly (do not assume hidden commands).

## First Build Milestones

1. Corpus manifest generation (PDF inventory + normalized book metadata).
2. Robust PDF extraction pipeline with page-level provenance.
3. Chunking tuned for long-form sacred literature.
4. Retrieval evaluation set for 81-book questions.
5. Chat response formatter enforcing citation and four-part leadership structure.
