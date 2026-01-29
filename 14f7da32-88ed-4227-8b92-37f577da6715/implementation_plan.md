# Implement Docling Worker & Core Libraries

We need to implement the actual document processing logic. The `lib` and `schemas` directories are currently empty, so we must build the core utilities first.

## Proposed Changes

### [docling-cluster/lib]

#### [NEW] [canonical.py](file:///c:/Users/eqhsp/Downloads/Qube/docling-cluster/lib/canonical.py)

- JCS (JSON Canonicalization Scheme) implementation.
- SHA256 hashing utilities.
- Ensures identical JSON produces identical hashes.

#### [NEW] [ledger.py](file:///c:/Users/eqhsp/Downloads/Qube/docling-cluster/lib/ledger.py)

- Hash-chain ledger implementation.
- Records operations (ingest, parse, embed).

### [docling-cluster/schemas]

#### [NEW] [doc_normalized_v1.py](file:///c:/Users/eqhsp/Downloads/Qube/docling-cluster/schemas/doc_normalized_v1.py)

- Pydantic model for the normalized document.
- Fields: `text`, `source_hash`, `pages`, `metadata`.

### [docling-cluster/services/docling-worker]

#### [MODIFY] [worker.py](file:///c:/Users/eqhsp/Downloads/Qube/docling-cluster/services/docling-worker/worker.py)

- **Import** `docling.document_converter`.
- **Logic**:
    1. Check if document hash already exists in ledger (deduplication).
    2. Parse PDF/Image using Docling.
    3. Normalize output to `DocNormalizedV1`.
    4. Compute canonical hash.
    5. Save normalized JSON to disk/S3 (mocking S3 with shared volume for now).
    6. Enqueue job for `embed-worker`.

## Verification Plan

### Automated Tests

1. **Unit Tests**: Test `canonical.py` with known JSONs to verify hash stability.
2. **Integration**: Submit a real PDF (from `test_document.pdf` if available, or create one).
3. **Verify**: Check worker logs for "Processed document..." and "Enqueued embed job...".
