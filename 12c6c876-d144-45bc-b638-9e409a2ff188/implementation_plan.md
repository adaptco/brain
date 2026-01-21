# Docling Cluster Pipeline Implementation Plan

## Goal

Create a deterministic, hash-anchored document processing pipeline using IBM Docling, PyTorch embeddings, and a local-first Docker Compose deployment.

## Proposed Changes

---

### Pipeline Directory Structure

#### [NEW] [pipeline/](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/pipeline/)

```
pipeline/
├── docker-compose.yml
├── schemas/
│   ├── doc.normalized.v1.schema.json
│   └── chunk.embedding.v1.schema.json
├── lib/
│   ├── canonical.py       # JCS hash + ledger
│   └── normalize.py       # L2 norm + text policy
├── ingest_api/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── main.py            # FastAPI
├── docling_worker/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── worker.py          # Celery/Arq task
├── embed_worker/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── worker.py          # PyTorch embeddings
└── ledger/
    └── ledger.jsonl       # Append-only hash chain
```

---

### Core Modules

#### [NEW] `lib/canonical.py`

- `jcs_canonical_bytes(obj)` – RFC8785-style JSON canonicalization
- `sha256_hex(b)` – SHA256 hex digest
- `hash_canonical_without_integrity(payload)` – Strips `integrity`, hashes, re-injects
- `append_to_ledger(record, ledger_path)` – Appends with `prev_ledger_hash`

#### [NEW] `lib/normalize.py`

- `normalize_text(text)` – NFKC, collapse whitespace, LF endings
- `l2_normalize(tensor)` – PyTorch L2 normalization

---

### Services

#### [NEW] `ingest_api/main.py` (FastAPI)

- `POST /ingest` – Accepts file upload + metadata, returns `bundle_id`
- Enqueues to `parse_queue` (Redis)

#### [NEW] `docling_worker/worker.py`

- Consumes `parse_queue`
- Parses with IBM Docling (pinned version)
- Normalizes text (NFKC, whitespace, LF)
- Emits `doc.normalized.v1` to ledger
- Enqueues chunks to `embed_queue`

#### [NEW] `embed_worker/worker.py`

- Consumes `embed_queue`
- Generates embeddings (PyTorch, pinned model)
- L2 normalizes vectors
- Emits `chunk.embedding.v1` to ledger
- Upserts to Qdrant

---

### Infrastructure

#### [NEW] `docker-compose.yml`

Services:

- `redis:alpine` – Queue backend
- `qdrant:latest` – Vector store
- `ingest-api` – FastAPI (port 8000)
- `docling-worker` – Celery worker
- `embed-worker` – Celery worker

Volumes:

- `./ledger:/data/ledger` – Persistent ledger

---

## Determinism Anchors (ConfigMap-ready)

| Key | Example |
|-----|---------|
| `pipeline_version` | `v1.0.0` |
| `docling_version` | `0.4.0` |
| `normalizer_version` | `norm.v1` |
| `chunker_version` | `chunk.v1` |
| `embedder_model_id` | `sentence-transformers/all-MiniLM-L6-v2` |
| `weights_hash` | `sha256:abc...` |

---

## Verification Plan

### Replay Test

1. Submit a known document to `/ingest`
2. Capture `doc_id`, `chunk_ids`, embedding hashes
3. Purge and re-process
4. Assert identical hashes

### Ledger Integrity

- Verify each record's `prev_ledger_hash` chains correctly
- Reject records with missing integrity fields
