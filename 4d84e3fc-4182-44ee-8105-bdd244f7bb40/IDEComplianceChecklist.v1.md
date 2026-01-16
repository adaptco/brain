# IDE Compliance Checklist (v1)
> **Artifact ID:** `adk://policy/ide.checklist.v1`
> **Enforcement:** Normative Gate (Pass/Fail)

This checklist defines the **minimum Control Surface capabilities** required for any development environment used to contribute to the ADK.

## 1. Schema & Validation Contracts
- [ ] **JSON Schema Binding**: IDE automatically validates `*.json` and `*.yaml` files against declared `$schema` URLs.
- [ ] **LSP Active**: Language Server Protocol (LSP) overhead is running for Python (e.g., Pyright/Pylance) and/or TypeScript.
- [ ] **No "Magic" Ignoring**: Editor does not silently suppress linter errors (e.g., widespread `# type: ignore` hiding).

## 2. Policy-as-Code Binding
- [ ] **Pre-commit Installed**: `pre-commit install` has been run; hooks trigger on `git commit`.
- [ ] **Formatting Determinism**: Editor respects `.editorconfig` (indentation, charset, trim trailing whitespace).
- [ ] **Lint on Save (Recommended)**: Editor runs auto-fix/lint (Ruff/ESLint) on file save.

## 3. The "Replay Court" (Local CI Parity)
- [ ] **Local CI Command**: Developer knows the single command to run the full CI suite locally (e.g., `make test-ci` or `./run_checks.sh`).
- [ ] **Container Runtime**: Docker or Podman is active and accessible by the tools.
- [ ] **No System Leakage**: Tests do not rely on globally installed packages outside the declared virtualenv/container.

## 4. Debugging Capability
- [ ] **Async/Process Awareness**: Debugger allows attaching to subprocesses and async loops (crucial for Agent orchestration).
- [ ] **Breakpoints Work**: Verified ability to hit a breakpoint in the core logic.

## 5. Control Environment
- [ ] **Dev Container Parity** (If using VS Code): The "Reopen in Container" action builds successfully.
- [ ] **Golden Image**: If specialized tools are needed, they match the versions in `.devcontainer/devcontainer.json`.

---
**Attestation:**
By pushing code, I certify my environment meets these controls.
