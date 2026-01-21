
# Walkthrough: Unified Knowledge Cloud (RC0)

This document serves as the "Merge Point" for all development threads: the ADK Release Candidate Blueprint, the Embedding Infrastructure, and the Docling Pipeline.

## 1. Integrated Components

The following components are now unified and committed to the `main` branch of the `knowledge/` repository:

### ADK Core (v0)

- **Path**: [adk/](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/adk/)
- **Status**: Release Candidate (RC0) finalized.
- **Includes**: Contracts, validation scripts, threat model, and boundaries.

### Ghost Void Server + React Client

- **Path**: [server/](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/server/)
- **Features**:
  - **Lexus Agent**: "Super App Super Model" Avatar.
  - **Alexis Driver**: Expert logic driving the IS-F container.
  - **Genesis Event**: Triggered by `/deploy`, now with artifact embedding.
- **Verification**: `npm run build` passed successfully.

### Docling Pipeline (Deterministic DB)

- **Path**: [docling/](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/docling/)
- **Features**:
  - **Deterministic Hashing**: JCS-canonical JSON hashing for all documents and embeddings.
  - **Cryptographic Ledger**: Hash-chain integrity in `ledger.jsonl`.
  - **Services**: Ingest API, Docling Worker, Embed Worker (PyTorch).
- **Control**: Managed via `docker-compose.yml`.

## 2. Determinism & Traceability

All components now share a common integrity pattern:

- Every document parse generates a `doc_id` based on content SHAs.
- Every embedding chunk generates a `chunk_id` and is L2-normalized.
- All operations are recorded in the append-only ledger with `prev_hash` links.

## 3. Operations & Debugging

- **Local Runner**: [adk.ps1](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/adk/adk.ps1) (PowerShell wrapper for ADK commands).
- **IDE Control**: [launch.json](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/.vscode/launch.json) added for Dockerized FastAPI debugging.
- **Build**: `docker compose up --build` runs the entire knowledge-processing cluster.

---

✅ **Thread Merge Complete**: All active components (ADK, Game Engine, Pipeline) are validated and anchored in a single commit history.
