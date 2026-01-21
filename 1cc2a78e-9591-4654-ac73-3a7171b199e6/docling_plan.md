# Docling Cluster Pipeline Implementation Plan

## Goal

Create a deterministic, hash-anchored document processing pipeline using IBM Docling, PyTorch embeddings, and a local-first Docker Compose deployment.

## Architecture & Flow

1. **Service Synchronization**:
    - **Redis/RQ**: Orchestrates asynchronous task management.
    - **Qdrant**: Manages `document_chunks` using Cosine Distance.
    - **PyTorch**: Executes high-fidelity embedding generation.

2. **The Integrity Protocol**:
    - **Identity**: SHA-256 content IDs for every chunk.
    - **Normalization**: L2 normalization for performant similarity search.
    - **Canonical Hashing**: JCS (RFC8785) to maintain "Saintly Honesty".

## Proposed Changes

### [NEW] `pipeline/` Directory Structure

#### [NEW] `docker-compose.yml`

- Services: `redis`, `qdrant`, `ingest-api`, `docling-worker`, `embed-worker`.
- Persistent ledger volume: `./ledger:/data/ledger`.

#### [NEW] `schemas/`

- `doc.normalized.v1.schema.json`: Formal JSON Schema for parsed output.
- `chunk.embedding.v1.schema.json`: Formal JSON Schema for embeddings.

#### [NEW] `lib/`

- `canonical.py`: JCS hash + ledger logic (`append_to_ledger`).
- `normalize.py`: Text normalization + L2 vector normalization.

#### [NEW] `ingest_api/`

- FastAPI endpoint (`POST /ingest`) returns `bundle_id`.

#### [NEW] `docling_worker/`

- `worker.py`: IBM Docling parsing + batching (32 chunks/batch).

#### [NEW] `embed_worker/`

- `worker.py`: PyTorch `DataLoader` batch inference + bulk Qdrant upsert.

---

## Determinism Anchors

| Key | Value |
|-----|-------|
| `pipeline_version` | `v1.0.0` |
| `docling_version` | `0.4.0` |
| `normalizer_version` | `norm.v1` |
| `embedder_model_id` | `sentence-transformers/all-MiniLM-L6-v2` |

## Verification Plan

### Replay Test

1. Submit document to `/ingest`.
2. Capture `doc_id` and `chunk_ids`.
3. Purge system and re-process.
4. **Assert** identical hashes across all stages.
