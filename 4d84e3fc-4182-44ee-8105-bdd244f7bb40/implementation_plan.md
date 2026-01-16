# Implementation Plan: Agency Docking Shell

## Goal Description
Build the "Docking Shell" – a centralized Hub for the Agency architecture. This system acts as a harness for "Agentic Field Games" (sandbox environments). It is responsible for ingesting environmental state ("voxelized tensor state"), normalizing it via "Eigenvalue embedding manifolds," and projecting it into a token-space for the LLM.

This is essentially a high-dimensional State-Interpretation Layer (SIL) for AI agents.

## User Review Required
> [!IMPORTANT]
> This is a **Foundational Architecture** task. I will implement this in `Python` (using `numpy`) as it requires significant linear algebra for the "Eigenstate embedding" and "Tensor" manipulations.

## Proposed Changes

### Core Architecture (`agency_hub/`)

#### [NEW] [docking_shell.py](file:///c:/Users/eqhsp/.gemini/antigravity/brain/4d84e3fc-4182-44ee-8105-bdd244f7bb40/agency_hub/docking_shell.py)
The "Hub". It initializes the specific "Field Game" (Spoke) and manages the `TensorField`.
*   **Class `DockingShell`**:
    *   `dock(spoke)`: Connects to an environment.
    *   `cycle()`: The main heartbeat (Tick -> Observe -> Normalize -> Act).

#### [NEW] [tensor_field.py](file:///c:/Users/eqhsp/.gemini/antigravity/brain/4d84e3fc-4182-44ee-8105-bdd244f7bb40/agency_hub/tensor_field.py)
The mathematical engine.
*   **Class `VoxelizedManifold`**:
    *   Maintains a 3D/N-D grid of state vectors.
    *   `project_eigenstate(input_tensor)`: Computes Eigenvalues/Vectors to normalize the input state.
    *   `map_rag(vector)`: Performs the dot-product unification with retrieved knowledge.

#### [NEW] [learning_routine.py](file:///c:/Users/eqhsp/.gemini/antigravity/brain/4d84e3fc-4182-44ee-8105-bdd244f7bb40/agency_hub/learning_routine.py)
The requested "creation routine".
*   Inits the Shell.
*   Runs a calibration loop to "normalize" the eigenvalues (effectively a warm-up/training phase).

### Interface

#### [NEW] [spoke_interface.py](file:///c:/Users/eqhsp/.gemini/antigravity/brain/4d84e3fc-4182-44ee-8105-bdd244f7bb40/agency_hub/spoke_interface.py)
Abstract Base Class for "Field Games".
*   `get_voxel_state()`: Returns raw tensor data.
*   `receive_token(token)`: Accepts LLM actions.

## Verification Plan
1.  **Unit Math Tests**: Verify `tensor_field.py` correctly computes dot products and normalizes vectors (using dummy data).
2.  **Mock Spoke**: Create a simple "DummyGame" spoke.
3.  **Integration Run**: Execute `learning_routine.py` and verify it produces a "Docking Complete" state with stable Eigenvalues.
