# ADAPTCO-ADK CLI & Integrity Engine Implementation Plan

Implementation plan for building and testing the ADAPTCO-ADK (v0.1.0-alpha) CLI tool with Environmental Determinism.

## User Review Required

> [!IMPORTANT]
> This implementation will create a new project directory at `C:\Users\eqhsp\.gemini\antigravity\scratch\adaptco-adk`. After creation, you should set this as your active workspace.

## Proposed Changes

### Project Structure

```
adaptco-adk/
├── src/
│   ├── hashing.py          # Hashing anchor with SHA-256
│   ├── hirr_harness.py     # HIRR harness for deterministic JSON
│   ├── schema_validator.py # Schema validation logic
│   └── adk.py              # Main CLI entry point
├── tests/
│   └── test_capsule.json   # Test fixture
├── dist/                   # Build output (generated)
│   └── adk.exe            # Compiled executable
├── requirements.txt        # Python dependencies
├── build.spec             # PyInstaller configuration
├── Dockerfile.foundation  # Docker foundation image
└── README.md              # Project documentation
```

---

### Core Components

#### [NEW] [hashing.py](file:///C:/Users/eqhsp/.gemini/antigravity/scratch/adaptco-adk/src/hashing.py)

Implements the "Hashing Anchor" with:

- `normalize_newlines(content: str) -> str`: Normalizes line endings to `\n`
- `calculate_file_hash(filepath: str) -> str`: Computes SHA-256 hash of normalized file content

#### [NEW] [hirr_harness.py](file:///C:/Users/eqhsp/.gemini/antigravity/scratch/adaptco-adk/src/hirr_harness.py)

Implements the "HIRR Harness" with:

- `deterministic_dumps(data: dict) -> str`: Produces deterministic JSON with sorted keys and strict separators

#### [NEW] [schema_validator.py](file:///C:/Users/eqhsp/.gemini/antigravity/scratch/adaptco-adk/src/schema_validator.py)

Implements schema validation logic:

- `validate_capsule(filepath: str) -> bool`: Validates JSON capsule structure

#### [NEW] [adk.py](file:///C:/Users/eqhsp/.gemini/antigravity/scratch/adaptco-adk/src/adk.py)

Main CLI entry point with three commands:

- `validate <file>`: Runs schema validation
- `replay <file>`: Runs HIRR harness verification
- `commit`: Wraps git commit with pre-flight integrity checks

---

### Build Configuration

#### [NEW] [requirements.txt](file:///C:/Users/eqhsp/.gemini/antigravity/scratch/adaptco-adk/requirements.txt)

Python dependencies for the project.

#### [NEW] [build.spec](file:///C:/Users/eqhsp/.gemini/antigravity/scratch/adaptco-adk/build.spec)

PyInstaller specification for building standalone executable:

- Entry point: `src/adk.py`
- Output: `dist/adk.exe`
- Single-file executable with all dependencies bundled

---

### Docker Foundation

#### [NEW] [Dockerfile.foundation](file:///C:/Users/eqhsp/.gemini/antigravity/scratch/adaptco-adk/Dockerfile.foundation)

Multi-stage Docker build:

- Stage 1: Compile ADK from source to native Linux binary
- Stage 2: Embed binary at `/usr/local/bin/adk`
- Build verification: Execute `adk --version` during build

---

### Test Fixtures

#### [NEW] [test_capsule.json](file:///C:/Users/eqhsp/.gemini/antigravity/scratch/adaptco-adk/tests/test_capsule.json)

Sample JSON capsule for testing validation and replay functionality.

## Verification Plan

### Automated Tests

1. **Validation Test**

   ```powershell
   python src/adk.py validate tests/test_capsule.json
   ```

   Expected output: `Validation Successful.`

2. **Replay Test**

   ```powershell
   python src/adk.py replay tests/test_capsule.json
   ```

   Expected output: `HIRR Replay: All systems nominal. Determinism holds.`

3. **Commit Interception Test**

   ```powershell
   python src/adk.py commit
   ```

   Expected output: Multi-stage integrity gate messages

4. **Executable Build Test**

   ```powershell
   pyinstaller build.spec
   dist/adk.exe --help
   ```

   Expected: Help message displayed

5. **Executable Validation Test**

   ```powershell
   dist/adk.exe validate tests/test_capsule.json
   dist/adk.exe replay tests/test_capsule.json
   ```

   Expected: Same outputs as Python version

### Manual Verification

- Review test output logs for correctness
- Verify executable size and dependencies
- Confirm deterministic behavior across multiple runs
