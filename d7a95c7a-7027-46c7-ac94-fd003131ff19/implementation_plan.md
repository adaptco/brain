# ADK CLI & Integrity Engine Implementation Plan

## Goal Description
Implement the `adk` CLI wrapper to serve as the unified "User Surface" for the ADAPTCO-ADK. This includes recreating the "Environmental Determinism" components (`hashing.py`, `hirr_harness.py`) described by the user to ensure infrastructure-level integrity and model drift elimination. The CLI will provide `validate`, `replay`, and `commit` commands.

## User Review Required
> [!IMPORTANT]
> Since the referenced `hashing.py` and `hirr_harness.py` were not found in the workspace, this plan includes their creation based on the "Analysis" section of the request.

## Proposed Changes

### Core Infrastructure (The Spine)
#### [NEW] [hashing.py](file:///c:/Users/eqhsp/.gemini/antigravity/brain/d7a95c7a-7027-46c7-ac94-fd003131ff19/adk_core/hashing.py)
*   **Purpose**: The "Hashing Anchor".
*   **Logic**: 
    *   Read files in binary mode.
    *   Normalize `\r\n` to `\n`.
    *   Compute SHA-256 (or similar) hash.
    *   Ensure cross-platform stability.

#### [NEW] [hirr_harness.py](file:///c:/Users/eqhsp/.gemini/antigravity/brain/d7a95c7a-7027-46c7-ac94-fd003131ff19/adk_core/hirr_harness.py)
*   **Purpose**: The "HIRR Harness".
*   **Logic**:
    *   Deterministic JSON serialization.
    *   `sort_keys=True`.
    *   Specific separators (e.g., `(',', ':')`).
    *   Verify state against "Golden Path" hashes.

### CLI Wrapper (The Surface)
#### [NEW] [adk.py](file:///c:/Users/eqhsp/.gemini/antigravity/brain/d7a95c7a-7027-46c7-ac94-fd003131ff19/adk.py)
*   **Purpose**: The CLI entry point.
*   **Commands**:
    *   `validate`: Runs schema validation (will need a placeholder or basic schema validator).
    *   `replay`: Triggers `hirr_harness` validation.
    *   `commit`: Wrapper for git commit, running validation/replay checks first ("Integrity Gate").

### Schemas
#### [NEW] [schema_validator.py](file:///c:/Users/eqhsp/.gemini/antigravity/brain/d7a95c7a-7027-46c7-ac94-fd003131ff19/adk_core/schema_validator.py)
*   **Purpose**: Basic schema validation logic.

## Verification Plan
### Automated Tests
*   Run `python adk.py replay` and verify it passes for valid data.
*   Run `python adk.py validate` with a dummy schema/data.
*   Run `python adk.py commit` (simulated) to check the hook logic.

### Manual Verification
*   Execute the `adk` commands in the terminal and check output messages.
