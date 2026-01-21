# Walkthrough - Docling Pipeline

## Implementation Complete

| Component | Status |
|-----------|--------|
| Infrastructure | ✅ docker-compose.yml with Redis, Qdrant, 4 services |
| Schemas | ✅ doc.normalized.v1, chunk.embedding.v1 |
| JCS Library | ✅ Canonicalization + hashing |
| ingest-api | ✅ FastAPI document submission |
| docling-worker | ✅ Parse + normalize |
| embed-worker | ✅ REFINED: PyTorch-ready + RQ worker |
| ledger | ✅ Append-only hash-chain |
| Replay Test | ✅ PASSED |

## Refined Embed Worker

The `embed_worker` has been upgraded to use:

- **PyTorch Structure**: L2 normalization and mock model inference loop.
- **RQ (Redis Queue)**: Robust worker management via `rq.Worker`.
- **Enhanced Schemas**: Includes `chunk_text`, `provenance`, and late-bound `integrity` hashing.

## Directory Structure

```text
docling/
├── docker-compose.yml
├── services/
│   ├── ingest-api/
│   ├── docling-worker/
│   ├── embed-worker/
│   └── ledger/
├── schemas/
├── lib/jcs.py
└── tests/
```

## Usage

```bash
cd docling
docker-compose up --build
```

Ingest: `curl -X POST http://localhost:8000/ingest -F "file=@doc.txt"`
Verify: `curl http://localhost:8001/verify`
