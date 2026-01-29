# Manifold Scaffolding Implementation Plan

## Goal Description
Create a "Worker" (automation script) that standardizes the dockerization of all completed scripts/services in the codebase. This "scaffolds the manifold" by generating a unified `docker-compose.yaml` (Eigenstate Matrix) and individual `Dockerfile`s for each component.

## Unification "Dot Product" Strategy
The worker will apply a "Dockerization Vector" to the "Project Vector" (Matrix) to generate the standardized infrastructure.

## Proposed Changes

### 1. The Eigenstate Matrix (Configuration)
#### [NEW] [manifold_matrix.json](file:///c:/Users/eqhsp/.gemini/antigravity/manifold_matrix.json)
defins the targets to be dockerized.
Structure:
```json
[
  {
    "name": "adk-cli",
    "path": "implicit",
    "type": "python",
    "entrypoint": "cli/adk.py",
    "dockerfile_exists": true
  },
  {
    "name": "ghost-void-server",
    "path": "playground/ghost-void/server",
    "type": "node",
    "port": 8080
  },
  {
    "name": "docling-ingest",
    "path": "knowledge/docling/ingest_api",
    "type": "fastapi",
    "port": 8000
  },
  {
    "name": "glacial-nadir",
    "path": "glacial-nadir",
    "type": "python",
    "entrypoint": "main_agent.py"
  }
]
```

### 2. The Worker (Scaffolder)
#### [NEW] [scaffold_manifold.py](file:///c:/Users/eqhsp/.gemini/antigravity/scaffold_manifold.py)
A Python script that:
1.  Reads `manifold_matrix.json`.
2.  Iterates through each project.
3.  **Dockerfile Generation**:
    -   If `Dockerfile` is missing, generates one based on `type` (node, python, fastapi).
    -   Uses `package.json` or `requirements.txt` detection.
4.  **Manifold Assembly**:
    -   Generates a root `docker-compose.yaml` that defines all these services, linking them together.

### 3. Execution
-   Run `python scaffold_manifold.py` to generate the artifacts.

## Verification Plan
### Automated Verification
-   Run the worker.
-   Check file existence: `docker-compose.yaml` and sub-project `Dockerfile`s.
-   Run `docker-compose config` to validate the generated manifest.
