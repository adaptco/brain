# Integrate Embed Worker (RQ Version)

Integrate the PyTorch/Qdrant Embed Worker using `RQ` as the task queue, while maintaining consistency with the existing Velocity Architecture / Jurassic Pixels spec.

## Proposed Changes

### [docling-cluster/lib]

#### [MODIFY] [canonical.py](file:///c:/Users/eqhsp/Downloads/Qube/docling-cluster/lib/canonical.py)

- Add `compute_chunk_id` function to generate deterministic chunk IDs.

#### [MODIFY] [__init__.py](file:///c:/Users/eqhsp/Downloads/Qube/docling-cluster/lib/__init__.py)

- Export `compute_chunk_id`.

---

### [docling-cluster/schemas]

#### [MODIFY] [__init__.py](file:///c:/Users/eqhsp/Downloads/Qube/docling-cluster/schemas/__init__.py)

- Export `ChunkerInfo` as `Chunker`, `EmbeddingInfo` as `Embedding`, and `ProvenanceInfo` as `Provenance` to match the new worker's imports.

---

### [docling-cluster/services/embed-worker]

#### [MODIFY] [requirements.txt](file:///c:/Users/eqhsp/Downloads/Qube/docling-cluster/services/embed-worker/requirements.txt)

- Add `rq` dependency.

#### [MODIFY] [Dockerfile](file:///c:/Users/eqhsp/Downloads/Qube/docling-cluster/services/embed-worker/Dockerfile)

- Update `CMD` to run the worker via `python worker.py` (since the script has a `__main__` block that starts the RQ worker).

#### [MODIFY] [worker.py](file:///c:/Users/eqhsp/Downloads/Qube/docling-cluster/services/embed-worker/worker.py)

- Replace existing Celery-based worker with the new RQ-based PyTorch/Qdrant worker provided by the user.
- Ensure the `sys.path` insertion correctly points to `/app` (as in the provided script).

## Verification Plan

### Automated Tests

- I will create a test script `verify_worker_imports.py` to ensure all imports in the worker script are valid given the modified lib and schemas.
- Run: `python docling-cluster/services/embed-worker/worker.py --check-only` (if I add a check-only flag) or just verify imports manually by running a snippet.

### Manual Verification

- Verify the Docker build: `docker build -t embed-worker ./docling-cluster/services/embed-worker`
- Verify the RQ worker starts correctly and connects to Redis.
