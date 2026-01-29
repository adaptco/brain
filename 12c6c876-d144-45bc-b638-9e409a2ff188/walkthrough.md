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

---

## 🧭 VT-TQ-Search AI Challenges

I have implemented the "Exploratory Learning" module for ToolQuest.

### Architecture

- **[Challenge Generator](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/toolquest/semantic/challenge_generator.py)**: Service that synthesizes interactive scenarios.
- **[Search API](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/toolquest/semantic/semantic_search_api.py)**: Exposes `POST /api/challenges/generate`.

### Challenge Logic

1. **Cluster Discovery**: Uses Qdrant vector search to find tools semantically related to the focus tool.
2. **Scenario Synthesis**: Generates a task requiring the use of the focus tool + neighbors.
3. **Dynamic Difficulty**: Calculates XP reward and tier based on tool complexity.

### Verification

**Test**: `python -m pytest toolquest/semantic/test_challenge_generator.py`
✅ Passed (Mocked Qdrant)

---

## 🦖 Jurassic Pixels: The Learning Loop

I have implemented the "Home World" HUB and the recursive pattern synthesis system.

### Architecture

- **[Home World (Level 0)](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/src/engine/WorldModel.cpp#L21-L28)**: Stable, symmetric training environment with balanced platforms.
- **[HUB Docking](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/src/qube/QubeRuntime.cpp#L76-L85)**: `DockPattern` method ingests embedding data and rehashes the kernel state.
- **[Pattern Synthesis](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/src/qube/QubeRuntime.cpp#L87-L105)**: `ReorganizeAndSynthesize` generates deterministic synthetic structures from the current state hash.

### The Recursion Loop

1. **Soak**: Embeddings from Qdrant are docked into the Qube HUB.
2. **Reorganize**: Pattern clusters are rehashed and reorganized.
3. **Synthesize**: New `SyntheticStructure` objects are generated.
4. **Materialize**: Structures are spawned back into the `WorldModel` via `SpawnPlane`.
5. **Stabilize**: Agents train in the evolved environment, closing the loop.

### Verification

**Test**: [jurassic_pixels_test.cpp](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/tests/jurassic_pixels_test.cpp)

**Note**: The test requires a C++ compiler. To run manually:

```bash
g++ -I./include tests/jurassic_pixels_test.cpp src/engine/WorldModel.cpp src/qube/QubeRuntime.cpp -o bin/jurassic_pixels_test
./bin/jurassic_pixels_test
```

---

## 🎯 Agency Docking Shell

I have implemented the portable Hub for Agentic Field Games that normalizes environmental states into a shared cognitive manifold.

### Architecture
- **[TensorField](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/agency_hub/tensor_field.py)**: Voxelizes arbitrary states and computes eigenstates via random projection.
- **[SpokeAdapter](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/agency_hub/spoke_adapter.py)**: ABC that Field Games implement to dock with the Hub.
- **[DockingShell](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/agency_hub/docking_shell.py)**: Hub controller executing the Observe → Normalize → Unify → Act cycle.

### The Cycle
1. **Observe**: `spoke.observe()` → raw environmental state
2. **Normalize**: `tensor_field.voxelize_state()` → voxel tensor → eigenstate
3. **Unify**: `tensor_field.rag_unify()` → knowledge-grounded state
4. **Act**: `_synthesize_token()` → action token → `spoke.act()`

### Verification
**Test**: `python agency_hub/learning_routine.py`

**Results**:
- ✅ Docking successful with `DummyFieldGame`
- ✅ Knowledge injection: 5 concepts (64-dim vectors)
- ✅ 5 learning cycles executed
- ✅ Eigenstate variance stabilized

### Next Steps
1. **GhostVoidSpoke**: Integrate with `WorldModel` and `QubeRuntime`
2. **LLM Integration**: Replace `_synthesize_token` with Gemini API
3. **Multi-Environment Learning**: Test agent transfer between spokes
