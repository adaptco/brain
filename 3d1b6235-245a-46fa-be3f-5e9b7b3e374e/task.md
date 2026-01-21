
# Task: Docling Pipeline & Thread Merge

## Infrastructure

- [x] Create `docker-compose.yml` with all services
- [x] Create Dockerfiles for each service
- [x] Create `requirements.txt` per service

## Schemas

- [x] Define `doc.normalized.v1` JSON schema
- [x] Define `chunk.embedding.v1` JSON schema
- [x] Implement JCS canonicalization + hashing

## Services

- [x] `ingest-api` (FastAPI): accept docs, return `bundle_id`
- [x] `docling-worker`: parse + normalize
- [x] `embed-worker`: chunk + embed
- [x] `ledger`: append-only JSONL + hash-chain

## Thread Merge

- [x] Resolve 'current problems' (lint/encoding issues addressed)
- [x] Consolidate ADK, Server, and Pipeline logic
- [x] Commit all changes to `main` branch
- [x] Create Unified Walkthrough (merged threads)

## Verification

- [x] Build Docker images (Simulated via syntax check/local build ops)
- [x] Unified Commit b1e9837
