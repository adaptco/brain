# Task: Docling Pipeline Implementation

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
- [x] `docling-worker`: parse + normalize → `doc.normalized.v1`
- [x] `embed-worker`: chunk + embed → `chunk.embedding.v1`
- [x] `ledger`: append-only JSONL + hash-chain

## Queues / Storage

- [x] Redis for task queues
- [x] Qdrant for vector storage

## Verification

- [ ] Build Docker images
- [ ] Integration test: full pipeline end-to-end
