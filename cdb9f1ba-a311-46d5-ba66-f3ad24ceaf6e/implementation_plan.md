# Docling Cluster Pipeline Implementation Plan

## Goal

Align the existing batch processing implementation with the detailed Docling Cluster Pipeline specification, ensuring all core libraries, schemas, and determinism anchors are properly configured.

## Proposed Changes

### Core Libraries

#### [MODIFY] [normalize.py](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/docling-pipeline/lib/normalize.py)

- Add `l2_normalize(tensor)` for PyTorch L2 normalization of embedding vectors.

#### [MODIFY] [canonical.py](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/docling-pipeline/lib/canonical.py)

- Add `append_to_ledger(record, ledger_path)` helper function for direct ledger appends.

---

### Schemas

#### [NEW] [doc.normalized.v1.schema.json](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/docling-pipeline/schemas/doc.normalized.v1.schema.json)

JSON Schema for normalized document events.

#### [NEW] [chunk.embedding.v1.schema.json](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/docling-pipeline/schemas/chunk.embedding.v1.schema.json)

JSON Schema for chunk embedding events.

---

### Worker Refinement

#### [MODIFY] [worker.py](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/docling-pipeline/services/embed_worker/worker.py)

- Import and utilize `l2_normalize` from `lib.normalize`.
- Ensure batch processing uses L2 normalization on embedding tensors.

## Verification Plan

### Replay Test

1. Submit a known document to `/ingest`
2. Capture `doc_id`, `chunk_ids`, and embedding hashes
3. Purge and re-process
4. Assert identical hashes to verify determinism

### Infrastructure Verification

- Verify `docker-compose.yml` environment variables match determinism anchors
- Confirm ledger persistence via volume mounts
