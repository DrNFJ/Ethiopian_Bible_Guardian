---
mode: ask
model: GPT-5.3-Codex
description: "Scaffold or update the solemn Ethiopian-canon RAG project structure, wiring ingestion/retrieval/citation flow and enforcing the four-part conversation-leading response policy."
---

Goal: Create or refine repository code structure for a citation-grounded RAG assistant with sacred tone.

Requirements:
- Keep original source PDFs in `corpus/` unchanged.
- Use the recommended layout from `AGENTS.md`.
- Ensure retrieval occurs before generation.
- Enforce response sections:
  1. Invocation
  2. Witness (with citations)
  3. Exhortation
  4. Reflection
- Add tests for retrieval relevance and citation presence.

Task inputs to request from user before coding:
- Preferred stack (Python/FastAPI, Node, other)
- Vector store preference
- Embedding and generation model preference
- Deployment target (local, cloud, edge)

Deliverables:
- Folder scaffolding
- Initial config files
- Retrieval/generation pipeline stubs
- Test stubs for citation + style policy
- Short runbook in README if missing
