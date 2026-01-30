# Implementation Plan: ADK Completion (Integration)

## Goal Description

Unify the isolated components (`unified_shell_proto` and `agency_hub`) into a cohesive **Agency Development Kit (ADK)**. This transforms the prototypes into a single installable toolchain that manages the Agentic Loop.

## Proposed Changes

### 1. Unified Directory Structure (`adk_core/`)

We will create a root package `adk_core` containing:

- `shell/` (The Unified Shell logic)
- `runtime/` (The Agency Hub logic)
- `bridges/` (The connectivity layer)

### 2. Configuration (`adk.toml`)

Implement a TOML-based configuration system.

```toml
[project]
name = "MyAgent"
version = "0.1.0"

[hub]
tensor_shape = [16, 16, 16]

[bridges]
default = "subprocess"
```

### 3. CLI Integration (`shell.py` -> `adk`)

Update the `UnifiedShell` to:

- Load `adk.toml`.
- Route `adk hub` commands to the `AgencyHub`.
- Route `adk repl` to the Python REPL.

#### [MODIFY] [shell.py](file:///c:/Users/eqhsp/code/adaptco/unified_shell_proto/shell.py)

* Add `toml` parsing (using `tomllib` if py3.11+ or simple fallback).
- Add `hub` command to routing table.
- Import `AgencyHub` to run in-process (or RPC).

#### [REFCTOR] [agency_hub/](file:///c:/Users/eqhsp/.gemini/antigravity/brain/4d84e3fc-4182-44ee-8105-bdd244f7bb40/agency_hub/)

* Move `agency_hub` into the unified structure as `adk_core.runtime`.
- Ensure `docking_shell` can be initialized with config dicts.

## Verification Plan

1. **Setup**: Create `adk.toml`.
2. **Run**: Execute `python -m adk_core.shell hub start`.
3. **Verify**: Hub starts, loads config, and enters learning loop.
