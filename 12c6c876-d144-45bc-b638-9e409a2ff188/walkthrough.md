# Docling Cluster Pipeline Walkthrough

I have implemented a deterministic, high-throughput document processing pipeline (the "Scribe") using IBM Docling, PyTorch, and Qdrant.

## 🏗️ The "Sovereign" Architecture

### 1. Services Orchestration

- **[ingest-api](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/docling-pipeline/services/ingest_api/main.py)**: FastAPI gateway for document uploads.
- **[docling-worker](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/docling-pipeline/services/docling_worker/tasks.py)**: Uses Docling to parse docs and groups chunks into **batches of 32**.
- **[embed-worker](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/docling-pipeline/services/embed_worker/tasks.py)**: Processes batches using vectorized PyTorch inference and perform bulk upserts to **Qdrant**.
- **[ledger-library](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/docling-pipeline/lib/ledger.py)**: Maintains an immutable, append-only hash-chain of every event.

### 2. The Batch Processing Evolution

To handle the 10k–100k document scale, I refactored the embedding flow to use **Batch Processing**:

- **Vectorized Inference**: `get_embeddings` processes multiple texts at once, maximizing GPU/CPU efficiency.
- **L2 Normalization**: Systematic application of $x / \|x\|_2$ across the batch tensor.
- **Bulk Upsert**: Point structures are pushed to Qdrant in a single `upsert` call per batch.

### 3. Determinism & Integrity

- **Canonical JCS Hashing**: Every JSON record is canonicalized (RFC8785) before hashing.
- **Provenance Tracking**: `source_block_refs` tie every embedding back to the page/block index in the source PDF.
- **Model Anchoring**: `WEIGHTS_HASH` is recorded to prevent semantic drift.

## 🚀 Deployment Guide

### Local Launch

```bash
cd docling-pipeline
docker-compose up -d --build
```

### Access Points

- **Ingest API**: `http://localhost:8000/docs`
- **Qdrant Dashboard**: `http://localhost:6333/dashboard`
- **Ledger Audit**: `tail -f docling-pipeline/ledger/ledger.jsonl`

## ✅ Operational Checklist

- [x] Pin Docling v0.5.0
- [x] Group chunks into batches (size=32)
- [x] L2 normalize output tensors
- [x] Chain-hash entire pipeline flow
