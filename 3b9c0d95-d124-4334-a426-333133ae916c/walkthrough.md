# Walkthrough - Embed Worker Integration

I have successfully integrated the new Embed Worker into the `docling-cluster`. This involved transitioning the service from Celery to RQ and updating the shared logic to support deterministic chunk indexing and hash-chain integrity.

## Changes Made

### Shared Library (`lib`)

- [x] **[canonical.py](file:///c:/Users/eqhsp/Downloads/Qube/docling-cluster/lib/canonical.py)**: Added `compute_chunk_id` for deterministic ID generation.
- [x] **[**init**.py](file:///c:/Users/eqhsp/Downloads/Qube/docling-cluster/lib/__init__.py)**: Exported `compute_chunk_id`.

### Shared Schemas (`schemas`)

- [x] **[chunk_embedding_v1.py](file:///c:/Users/eqhsp/Downloads/Qube/docling-cluster/schemas/chunk_embedding_v1.py)**: Added `chunk_text` field and made `integrity` optional for initial creation to support the worker's multi-step hashing process.
- [x] **[**init**.py](file:///c:/Users/eqhsp/Downloads/Qube/docling-cluster/schemas/__init__.py)**: Exported `Chunker`, `Embedding`, and `Provenance` directly for clean worker imports.

### Embed Worker Service

- [x] **[requirements.txt](file:///c:/Users/eqhsp/Downloads/Qube/docling-cluster/services/embed-worker/requirements.txt)**: Replaced `celery` with `rq`.
- [x] **[Dockerfile](file:///c:/Users/eqhsp/Downloads/Qube/docling-cluster/services/embed-worker/Dockerfile)**: Updated `CMD` to run the script directly.
- [x] **[worker.py](file:///c:/Users/eqhsp/Downloads/Qube/docling-cluster/services/embed-worker/worker.py)**: Implemented the new PyTorch/Qdrant logic using `RQ`.

## Verification Results

### Import Verification

I verified that the imports in `worker.py` correctly resolve with the new library structure.

```python
# Verified imports:
from lib import compute_chunk_id, get_ledger, hash_canonical_without_integrity
from schemas import ChunkEmbeddingV1, Chunker, Embedding, Provenance
```

### Docker Readiness

The `Dockerfile` is updated and ready for a fresh build:

```bash
docker build -t embed-worker ./docling-cluster/services/embed-worker
```

### Logic & Integrity

- **Deterministic IDs**: Local tests confirm `compute_chunk_id` produces predictable hashes from content.
- **Pydantic Validation**: Verified that `ChunkEmbeddingV1` can be instantiated by the worker and subsequently enriched with integrity hashes without failing validation.

## Alignment with Velocity Architecture

The integration follows the **Deterministic Emulator** logic by ensuring that all `chunk_id`s are derived from content, and the `IntegritySentinel` logic (from our previous Rust draft) is supported by the `hash_canonical_without_integrity` and `get_ledger` calls.
