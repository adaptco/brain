# evolved Batch Processing & Sovereign Signing

Enhance the `embed-worker` with a "Sovereign Wallet Proxy" scaffold for batch signing and full GPU-ready DataLoader logic.

## Proposed Changes

### [docling-cluster/services/embed-worker]

#### [MODIFY] [worker.py](file:///c:/Users/eqhsp/Downloads/Qube/docling-cluster/services/embed-worker/worker.py)

- **GPU-Ready DataLoader**: Update `get_embeddings_batch` to handle device placement (`cuda` vs `cpu`).
- **Sovereign Wallet Proxy**: Scaffold a `WalletProxy` class that "signs" the batch content hash.
- **Enhanced "Scribe" Logging**: Add detailed telemetry for batch signing and ledger commits.

## Verification Plan

### Automated Tests

- `test_batch_signing.py`: Verify that the batch content hash is correctly signed by the proxy.
- `test_gpu_logic.py`: Verify that the device selection logic correctly falls back to CPU if no CUDA is present.
