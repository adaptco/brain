# Agency Docking Shell: Architecture Walkthrough

This codebase implements the **Agency Docking Shell**, a portable "Hub" for Agentic Field Games. It normalizes environmental states into a shared cognitive manifold.

## 1. System Components

### [DockingShell](file:///c:/Users/eqhsp/.gemini/antigravity/brain/4d84e3fc-4182-44ee-8105-bdd244f7bb40/agency_hub/docking_shell.py) (The Hub)
The central controller. It "docks" with a Spoke (environment) and runs the **Cycle**:
`Observe -> Normalize -> Unify -> Act`.

### [TensorField](file:///c:/Users/eqhsp/.gemini/antigravity/brain/4d84e3fc-4182-44ee-8105-bdd244f7bb40/agency_hub/tensor_field.py) (The Math Core)
Handles the heavy lifting:
*   **Voxelized State**: Manages the n-dimensional state of the world.
*   **Eigen-Embedding**: Normalizes the state variance to create a stable "Eigenstate".
*   **RAG Unification**: Maps the Eigenstate to knowledge vectors via dot-product similarity.

### [SpokeAdapter](file:///c:/Users/eqhsp/.gemini/antigravity/brain/4d84e3fc-4182-44ee-8105-bdd244f7bb40/agency_hub/spoke_interface.py) (The Interface)
The `ABC` (Abstract Base Class) that any "Field Game" (Sandbox) must implement to plug into the Hub.

## 2. Verification (Learning Routine)

We successfully ran the **[learning_routine.py](file:///c:/Users/eqhsp/.gemini/antigravity/brain/4d84e3fc-4182-44ee-8105-bdd244f7bb40/agency_hub/learning_routine.py)**.

**Results:**
*   **Docking:** Successful connection to `DummyFieldGame`.
*   **Knowledge Injection:** Primed RAG with 5 simulated concepts.
*   **Stabilization:** Ran 5 epochs of the `cycle()`, producing valid "Tokens" (Actions) based on the state variance.

## 3. Usage
To run the hub and see the "Agency" in action:

```bash
cd agency_hub
python learning_routine.py
```

## 4. Next Steps
*   **Create a Real Spoke**: Replace `DummyFieldGame` with the 2.5D Mario Kart engine we discussed.
*   **Connect LLM**: Replace the `_synthesize_token` heuristic with a real call to Geminin/GPT.
