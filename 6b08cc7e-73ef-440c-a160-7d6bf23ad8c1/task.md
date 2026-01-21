# Verification Strategy Implementation

## Tasks

- [x] Create implementation plan for review
- [x] Fix `bundle_id` generation to be deterministic (content-hash based)
- [x] Create `tests/` directory structure
- [x] Implement Replay Test (submit same doc twice → identical bundle_id/hashes)
- [x] Implement Integration Test (end-to-end ingest → ledger entry)
- [x] Add pytest configuration to pyproject.toml
- [x] Verify tests pass

## Embed Worker Implementation

- [x] Implement `embed-worker/worker.py` from user snippet
- [x] Verify imports and schema compliance
- [ ] Test deterministic embedding generation
