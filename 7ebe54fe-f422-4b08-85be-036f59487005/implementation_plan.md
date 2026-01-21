# Docling Cluster Pipeline Implementation Plan

Goal: Create a deterministic, hash-anchored document processing pipeline using IBM Docling, PyTorch embeddings, and a local-first Docker Compose deployment.

## Core Modules

### [NEW] `lib/canonical.py`

- `jcs_canonical_bytes(obj)`: RFC8785-style JSON canonicalization.
- `sha256_hex(b)`: SHA256 hex digest.
- `hash_canonical_without_integrity(payload)`: Strips integrity, hashes, re-injects.
- `append_to_ledger(record, ledger_path)`: Appends with `prev_ledger_hash`.

### [NEW] `lib/normalize.py`

- `normalize_text(text)`: NFKC, collapse whitespace, LF endings.
- `l2_normalize(tensor)`: PyTorch L2 normalization.

## Services

### [NEW] `ingest_api/main.py` (FastAPI)

- `POST /ingest`: Accepts file upload + metadata, returns `bundle_id`.
- Enqueues to `parse_queue` (Redis).

### [MODIFY] `docling_worker/tasks.py`

- Consumes `parse_queue`.
- Parses with IBM Docling.
- Normalizes text.
- Batches chunks (e.g., groups of 32).
- Enqueues batches to `embed_queue`.

### [MODIFY] `embed_worker/worker.py`

- Consumes `embed_queue`.
- Processes batches using PyTorch batch inference.
- Uses L2 normalization on batch tensors.
- Performs bulk upsert to Qdrant.
- Appends multiple records to ledger efficiently.

## Infrastructure (`docker-compose.yml`)

- `redis:alpine`: Queue backend.
- `qdrant:latest`: Vector store.
- `ingest-api`: FastAPI (port 8000).
- `docling-worker`: Celery/RQ worker.
- `embed-worker`: Celery/RQ worker.
- Volume: `./ledger:/data/ledger` (Persistent ledger).

## Verification Plan

### Automated Replay Test

1. Submit a known document to `/ingest`.
2. Capture `doc_id`, `chunk_ids`, embedding hashes.
3. Purge and re-process.
4. Assert identical hashes.
