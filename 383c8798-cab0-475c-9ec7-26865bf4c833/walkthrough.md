# Docling Normalization Cluster - Walkthrough

## Summary

Built a deterministic, high-throughput document processing pipeline:
**Documents → IBM Docling → Canonical JSON → Batch PyTorch Embeddings → Qdrant**

The system has been upgraded to **"Scribe" Batch Mode**, utilizing PyTorch `DataLoader` for vectorized inference and **Sovereign Wallet Proxy** for signing batch digests, ensuring "Saintly Honesty" across the ledger.

## Files Created (25 total)

```text
docling-cluster/
├── docker-compose.yml          # Local dev deployment
├── kind-cluster.yaml           # Local K8s cluster config
├── pyproject.toml              # Python dependencies
├── README.md
├── lib/
│   ├── canonical.py            # JCS canonicalization + SHA256
│   ├── normalize.py            # L2 norm, document text norm
│   └── ledger.py               # Hash-chain ledger
├── schemas/
│   ├── doc_normalized_v1.py    # Pydantic: normalized doc
│   └── chunk_embedding_v1.py   # Pydantic: chunk + vector
├── services/
│   ├── ingest-api/             # FastAPI ingestion (RQ producer)
│   ├── docling-worker/         # RQ Docling parser
│   └── embed-worker/           # RQ PyTorch embedder + Qdrant
├── k8s/
│   ├── configmap.yaml          # Pinned versions
│   └── deployments.yaml        # All services
└── scripts/
    ├── deploy-local.sh
    └── deploy-local.bat
```

## Quick Start

```bash
cd docling-cluster
docker-compose up --build
curl -X POST http://localhost:8000/ingest -F "file=@doc.pdf"
```

## Determinism Anchors

|Anchor|Location|
|---|---|
|Docling version|`k8s/configmap.yaml`|
|Normalizer version|`lib/normalize.py`|
|Embedder model + hash|`services/embed-worker/worker.py`|
|Queue System|RQ (Redis Queue)|
|Batch Logic|`services/embed-worker/worker.py` (DataLoader)|
|Batch Signing|`WalletProxy` (Sovereign Key)|
|Hash chain|`lib/ledger.py`|
{

    "configurations": [
        {
            "type": "node",
            "request": "launch",
            "name": "Run create-jest",
            "runtimeExecutable": "create-jest",
            "cwd": "${workspaceFolder}",
            "args": []
        },
        {
            "name": "PowerShell: Launch Short File",
            "type": "PowerShell",
            "request": "launch",
            "script": "${file}",
            "args": [],
            "cwd": "${fileDirname}"
        },
        {
            "name": "Batch: Launch Current File",
            "type": "shell",
            "request": "launch",
            "command": "${file}",
            "cwd": "${fileDirname}"
        },
        {
            "name": "Containers: Python - Fastapi",
            "type": "docker",
            "request": "launch",
            "preLaunchTask": "docker-run: debug",
            "python": {
                "pathMappings": [
                    {
                        "localRoot": "${workspaceFolder}",
                        "remoteRoot": "/app"
                    }
                ],
                "projectType": "fastapi"
            }
        }
    ]
}
