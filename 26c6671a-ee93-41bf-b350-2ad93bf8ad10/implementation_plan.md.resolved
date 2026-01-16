# Release Candidate Blueprint (RC0) Implementation Plan

Targeting a "Contracts-first + Docker-first CLI" architecture (default recommendation) unless otherwise specified.

## User Review Required

> [!IMPORTANT]
> **Missing Configuration Inputs**
> To generate the final bundle, I need the following decisions from you:
> 1. **Language Spine**: `TypeScript` / `Python` / `Docker-first` (Recommended: **Docker-first**)
> 2. **Package + Repo Name**: e.g. `qadk` + `Q-Enterprises/qadk`
> 3. **License Posture**: `MIT` / `Apache-2.0` / etc.
> 4. **Vocabulary Posture**: `Native` or `Neutral+Mapping` (Recommended: **Neutral+Mapping**)

## Proposed Changes

I will create the following directory structure and files in the current workspace, corresponding to the RC0 Blueprint.

### Repository Layout

```text
(repo_root)/
  contracts/v0/        # The immutable standard
    schemas/           # JSON Schemas
    state_machine/     # YAML Definitions
    gates/             # Policy YAML
    mappings/          # Vocabulary
  cli/                 # The reference implementation
  examples/            # Golden path inputs/outputs
  docs/                # Boundaries & Usage
  tests/               # Integration tests
  .github/workflows/   # CI/CD
```

### Component Details

#### [NEW] [contracts/v0]
- **Schemas**: `artifact.schema.json`, `event.schema.json`, `gate_result.schema.json`, `state.schema.json`, `tool_policy.schema.json`.
- **State Machine**: `states.yaml`, `transitions.yaml`.
- **Gates**: `catalog.yaml`, `severity.yaml`.
- **Mappings**: `vocabulary_map.yaml`.

#### [NEW] [cli]
- **Dockerfile**: For the Docker-first spine (encapsulating the logic).
- **Scripts**: `adk.sh` (entrypoint), `commands/validate.sh`, `commands/pack.sh`, etc.

#### [NEW] [CI & Docs]
- **Workflows**: `ci.yml` (validation), `release.yml` (publishing).
- **Docs**: `boundaries.md`, `threat_model.md`.

## Verification Plan

### Automated Tests
- **Schema Validation**: Run `schema_self_test.sh` to ensure all JSON schemas are valid meta-schemas.
- **Transition Consistency**: Run `transition_consistency_test.sh` to verify state machine integrity.
- **Golden Path**: Run `golden_path_test.sh` to certify the example produces the expected artifacts/events.
- **Docker Build**: Verify `docker build` succeeds for the CLI.

### Manual Verification
- Review `boundaries.md` to ensure it explicitly states what the ADK is *not*.
- Check `LICENSE` matches the user's choice.
