# Walkthrough: Docling Pipeline

## Summary

Built a **deterministic document processing pipeline** using IBM Docling, PyTorch embeddings, and an append-only ledger with hash-chain integrity.

## Components Created

### Infrastructure

| File | Description |
|------|-------------|
| [docker-compose.yml](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/docker-compose.yml) | Multi-service: Redis, Qdrant, ingest-api, workers |

### Schemas (`docling/schemas/`)

| File | Description |
|------|-------------|
| [doc_normalized_v1.py](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/docling/schemas/doc_normalized_v1.py) | Pydantic schema for parsed documents |
| [chunk_embedding_v1.py](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/docling/schemas/chunk_embedding_v1.py) | Pydantic schema for embeddings |

### Services

| Service | Path | Description |
|---------|------|-------------|
| ingest-api | [main.py](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/docling/ingest_api/main.py) | FastAPI: `POST /ingest` |
| docling-worker | [tasks.py](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/docling/docling_worker/tasks.py) | Docling parse + normalize |
| embed-worker | [tasks.py](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/docling/embed_worker/tasks.py) | PyTorch embeddings |

### Common Utilities (`docling/common/`)

- **canonicalize.py**: JCS + SHA256 hashing
- **normalize.py**: NFKC text + L2 vector normalization

### Ledger (`docling/ledger/`)

- **ledger.py**: Append-only JSONL with hash-chain

## Running the Pipeline

```bash
# Start all services
docker compose up --build -d

# Ingest a document
curl -X POST http://localhost:8000/ingest -F file=@document.pdf

# View ledger
cat docling/data/ledger.jsonl | jq .
```

## Determinism Anchors

All outputs are reproducible via:

- `parser.config_hash`
- `embedding.weights_hash`
- `integrity.sha256_canonical`
- `integrity.prev_ledger_hash`
