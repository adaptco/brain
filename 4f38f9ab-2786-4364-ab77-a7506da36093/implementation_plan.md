# Track Map Visualization Plan

## Goal

The goal is to create a visualization of the vehicle's trajectory (Track Map) by simulating the vehicle dynamics using the trained `EmbeddingCircuit` or the mocked environment in `train.py`.

## User Review Required
>
> [!NOTE]
> This plan requires installing `matplotlib` in the environment to generate the plot. I will proceed with `pip install matplotlib`.

## Proposed Changes

### Training

#### [NEW] [track_mapper.py](file:///c:/Users/eqhsp/.gemini/antigravity/implicit/training/track_mapper.py)

This script will:

1. Import `EmbeddingCircuit` and `mock_step` from `train.py`.
2. Initialize the `EmbeddingCircuit` (random weights or loaded if artifact exists).
3. Initialize vehicle state: `[Yaw, Speed, Lateral G, Slip Angle]` + `Pos X`, `Pos Y`.
4. Run a simulation loop (e.g., 1000 steps).
5. At each step:
    - Get `action` from the circuit.
    - Update `state` using `mock_step`.
    - Integrate position:
        - $x += speed * \cos(yaw)$
        - $y += speed * \sin(yaw)$
    - Store $(x, y)$ coordinates.
6. Use `matplotlib.pyplot` to plot the trajectory.
7. Save the plot to `track_map.png` in the artifacts directory.

## Verification Plan

### Automated

1. Install matplotlib: `pip install matplotlib`
2. Run the mapper: `python training/track_mapper.py`
3. Verify output: Check that `track_map.png` exists and is non-empty.
