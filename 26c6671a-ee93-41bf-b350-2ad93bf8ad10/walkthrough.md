# Walkthrough - Release Candidate Blueprint (RC0)

I have successfully generated the **Release Candidate Blueprint** for the ADK (Artifact Development Kit) based on the "Docker-first" spine.

## Generated Artifacts

### Repository Structure `adk/`

The following structure has been created in your workspace:

```text
adk/
├── adk.ps1            # Windows PowerShell Host Wrapper
├── adk                # Linux/Mac Host Wrapper
├── contracts/v0/      # The Immutable Standard
│   ├── schemas/       # artifact, event, gate_result, state, tool_policy
│   ├── state_machine/ # states.yaml, transitions.yaml
│   ├── gates/         # catalog.yaml, severity.yaml
│   └── mappings/      # vocabulary_map.yaml
├── cli/               # Docker-first Reference Implementation
│   ├── Dockerfile
│   ├── adk.sh
│   └── commands/      # validate, pack, verify, run_golden_path
├── examples/
│   └── golden_path/   # Input JSON and README
├── docs/              # Boundaries & Threat Model
├── tests/             # Contract & Integration Tests
└── .github/workflows/ # CI & Release automation
```

### Key Decisions Implemented

1. **Spine**: Docker-first. Logic encapsulated in `cli/Dockerfile`.
2. **Wrappers**: Added `adk.ps1` and `adk` to handle Docker build/run + volume mounting.
3. **Contracts**: Implemented strict JSON schemas and YAML policies in `contracts/v0`.
4. **Vocabulary**: Implemented the `vocabulary_map` to bridge Public terms (Event Log) to Internal terms (SSOT).
5. **CI/CD**: Added GitHub Actions for automatic validation and releasing.

## Verification

I have verified that:

- [x] All 5 core schemas exist.
- [x] The State Machine transitions are defined.
- [x] The CLI wrapper scripts act as the entry point.
- [x] The CI workflows are configured to test the contracts.
- [x] Host wrappers (`adk.ps1`, `adk`) are present in the root.

### Release Verification (Manual)

Due to a missing Docker runtime, I performed a **Local Verification Protocol**:
- **Content Check**: Validated `adk-contracts-v0.tar.gz` contains all `contracts/v0/` files.
- **Integrity Check**: Verified `adk-contracts-v0.tar.gz.sha256` aligns with the file hash.
  - Hash: `A99E89B20A88A88A6F2CE985B06C69569DBE764C9095386BD97ED7BA2AA3C555`

### Model Architecture Check

I executed a structural validation script (`tests/contracts/validate_architecture.py`) using Python:
- [x] **Schemas**: All 5 JSON schemas parsed successfully.
- [x] **State Machine**: All transitions in `transitions.yaml` reference valid states defined in `states.yaml`.
- [x] **States**: DRAFT, COMPILED, EXECUTED, VALIDATED, FINALIZED, REJECTED.

## Game Application: Ghost Void

I have scaffolded the **Ghost Void** game application in:

- `server/`: Node.js Game Server
- `server/react-client/`: React Web Client

### How to Run

1. **Start the Server**:

    ```bash
    cd server
    npm install
    node server.js
    ```

    *Starts on port 8080.*

2. **Start the Client**:

    ```bash
    cd server/react-client
    npm install
    npm run dev
    ```

    *Open the URL shown (e.g., <http://localhost:5173>).*
