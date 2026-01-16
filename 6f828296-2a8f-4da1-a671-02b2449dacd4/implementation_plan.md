# Driver Training Routine Plan

## Goal Description
Establish a formal learning routine for the `TokenSuzuki.PocketBunny.R32` driver using a specialized **Embedding Circuit**. This approach encodes vehicle state into a dense latent representation before deriving control actions, creating a portable "Identity Core" that can be frozen and distributed.

## User Review Required
> [!IMPORTANT]
> The "Policy" is now explicitly defined as an `EmbeddingCircuit`.
> The output artifact will be a serialized circuit (e.g., `suzuki_r32_circuit.pt` or `.onnx`) rather than just checking weights.

## Proposed Changes
### Training Module
#### [NEW] [circuit.py](file:///c:/Users/eqhsp/.gemini/antigravity/implicit/training/circuit.py)
- Defines the `EmbeddingCircuit` class:
    - **Input Layer**: Telemetry (Yaw, Speed, Lateral G, Slip Angle).
    - **Embedding Layer**: Compresses state into a "Driver Signature" (Latent Space).
    - **Action Head**: Decodes embedding into Control (Steer, Throttle, Brake).
    - Includes `forward()` and `export()` methods.

#### [NEW] [reward.py](file:///c:/Users/eqhsp/.gemini/antigravity/implicit/training/reward.py)
- `calculate_reward(state, action, next_state)`:
    - **Flow**: Encourages smooth embedding transitions (minimizing latent jerk).
    - **Kawaii**: Penalizes aggressive mechanical inputs.
    - **Pace**: Reward for sector times.

#### [NEW] [train.py](file:///c:/Users/eqhsp/.gemini/antigravity/implicit/training/train.py)
- Initializes the `EmbeddingCircuit`.
- Runs the training loop (Gradient Descent on the Circuit).
- **Output**: Saves the trained `EmbeddingCircuit` as the "MINTED" artifact.

#### [NEW] [config.yaml](file:///c:/Users/eqhsp/.gemini/antigravity/implicit/training/config.yaml)
- Hyperparameters for the Circuit:
    - Embedding Dimension: 64
    - Depth: 3
    - Activation: GELU ("Smooth")

## Verification Plan
### Automated Verification
- Run `python training/train.py --dry-run` to ensure the Circuit initializes and forwards data correctly.
- Verify the output file `suzuki_r32_circuit.pt` (or equivalent) is generated.
