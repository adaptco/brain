# CI Parity Runbook: The Replay Court
> **Goal:** If it fails in CI, it MUST fail locally with the exact same error.

This runbook defines the canonical commands to reproduce CI gates on your local machine.

## 1. Quick Check (The "Smoke Test")
Before pushing, always run the pre-commit hooks. This catches 90% of formatting and schema errors.

```bash
pre-commit run --all-files
```

## 2. Full Suite (The "Gatekeeper")
To run the full test suite exactly as the CI server does:

```bash
# Example: If using Make
make test-ci

# Example: If using a script
./scripts/run_ci.sh
```

**Note:** If these commands fail locally, **do not push**. The CI will definitely fail.

## 3. Containerized Replay (The "Golden Standard")
If you suspect environment drift (e.g., "It works on my machine but fails in CI"), you must run the checks inside the clean container environment:

```bash
# 1. Build the control surface
docker build -t adk-control-surface .

# 2. Run the checks inside it
docker run --rm -v $(pwd):/workspace adk-control-surface make test-ci
```

## 4. Debugging CI Failures
If you need to poke around inside the failing environment:

```bash
docker run -it --rm -v $(pwd):/workspace adk-control-surface /bin/bash
```

## 5. Schema Validation
To strictly validate all JSON/YAML files against their schemas:

```bash
# This uses the check-jsonschema CLI (ensure it is installed)
check-jsonschema --schemafile schemas/config.schema.json config/*.json
```
