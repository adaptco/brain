# Implementation Plan: Docling Pipeline

## Goal

Build a **deterministic document parsing pipeline** using IBM Docling, PyTorch embeddings, and an append-only ledger with hash-chain integrity.

## User Review Required

> [!IMPORTANT]
> This plan creates a `docling/` directory with the new pipeline code. The existing `compose.yaml` will be **replaced** with a multi-service configuration.

## Proposed Changes

### Project Structure

```text
knowledge/
├── docling/
│   ├── ingest_api/          # FastAPI service
│   ├── docling_worker/      # Docling parse worker
│   ├── embed_worker/        # PyTorch embedding worker
│   ├── ledger/              # Hash-chain ledger library
│   ├── schemas/             # JSON schemas
│   └── common/              # Shared utils (JCS, hashing)
├── docker-compose.yml       # Multi-service compose
└── ...
```

---

### Infrastructure

#### [MODIFY] [docker-compose.yml](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/compose.yaml)

Replace with multi-service configuration:

- `redis:alpine` — task queue
- `qdrant:latest` — vector store
- `ingest-api` — FastAPI (port 8000)
- `docling-worker` — Celery worker
- `embed-worker` — Celery worker

---

### New Files

#### [NEW] `docling/schemas/doc_normalized_v1.py`

Pydantic model for `doc.normalized.v1`.

#### [NEW] `docling/schemas/chunk_embedding_v1.py`

Pydantic model for `chunk.embedding.v1`.

#### [NEW] `docling/common/canonicalize.py`

JCS canonicalization + SHA256 hashing.

#### [NEW] `docling/common/normalize.py`

L2 normalization for embeddings (PyTorch).

#### [NEW] `docling/ledger/ledger.py`

Append-only JSONL writer with hash-chain.

#### [NEW] `docling/ingest_api/main.py`

FastAPI app: `POST /ingest` → enqueue to `parse_queue`.

#### [NEW] `docling/docling_worker/worker.py`

Celery worker: Docling parse + normalize.

#### [NEW] `docling/embed_worker/worker.py`

Celery worker: chunk + embed + L2 normalize.

---

## Verification Plan

### Automated Tests

```bash
# Build and start all services
docker compose up --build -d

# Submit a test document
curl -X POST http://localhost:8000/ingest -F file=@test.pdf

# Check ledger for deterministic hashes
cat docling/data/ledger.jsonl | jq '.integrity.sha256_canonical'
```

### Determinism Replay Test

- Ingest same document twice → verify identical `doc_id`, `chunk_ids`, and embedding hashes.
