# Mega Man Emulation Implementation Plan

Goal: Use the ADK framework to build a game engine scaffolding a Mega Man emulation, including level generation ("World Model"), avatar control, and physics.

## User Review Required
> [!IMPORTANT]
> The emulation will be text/state-based for the "Orchestrator" view. 9 Levels will be scaffolded via the `LevelGenerator`, but only the logic for platforming and boss encounters will be implemented, not the full graphical assets.

## Proposed Changes

### Build System
#### [NEW] [Makefile](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/Makefile)
- Compiles `src` and `tests`.

### ADK Framework Setup (Prerequisites)
#### [NEW] [devcontainer.ide_control_surface.v1](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/adk/env/devcontainer.ide_control_surface.v1)
#### [NEW] [ide.compliance_checklist.v1](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/adk/policy/ide.compliance_checklist.v1)
#### [NEW] [ci_parity.v1](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/adk/runbook/ci_parity.v1)

### Engine Core (`src/engine`)
#### [NEW] [Orchestrator.hpp](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/include/engine/Orchestrator.hpp) / [main.cpp](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/src/main.cpp)
- **Game Loop**: Inputs -> Physics -> World Update -> Render (State).
- **Asset Loader**: Mock loader for "9 Levels".

#### [NEW] [Sandbox.hpp](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/include/engine/Sandbox.hpp)
- Holds the `WorldModel` and `Entities`.
- Manages strict framing (Side-scrolling window).

#### [NEW] [WorldModel.hpp](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/include/engine/WorldModel.hpp) (Agentic Field)
- **LevelGenerator**: Procedurally generates platforms/hazards based on "Level ID" (1-9).
- **BossRoom**: Special segment at the end of a level.
- **Checkpoint**: State serialization point.

#### [NEW] [Physics.hpp](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/include/engine/Physics.hpp)
- **SafetyLayer Integration**: Enforces "World Boundaries" and "Collision" as safety constraints.
- Gravity, Jump dynamics, Dash.

### Agents
#### [NEW] [Avatar.hpp](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/src/agents/Avatar.hpp)
- "Mega Man" state machine (Idle, Run, Jump, Shoot).

#### [NEW] [Boss.hpp](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/src/agents/Boss.hpp)
- Simple behavior tree for Boss (e.g., Jump, Shoot, Pattern).

### WebSocket Shell
#### [NEW] [server.js](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/server/server.js)
- Node.js WebSocket Server (`ws` library).
- Spawns the Game Engine process.
- Relays JSON messages between WebSocket and Game Engine Stdin/Stdout.

#### [MODIFY] [Orchestrator.cpp](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/src/engine/Orchestrator.cpp)
- Update game loop to read commands from Stdin.
- Output game state as JSON to Stdout.

### SPA Checkpoint (Client)
#### [NEW] [index.html](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/server/public/index.html)
- Main entry point. Defines the Canvas and UI controls.

#### [NEW] [style.css](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/server/public/style.css)
- Retro "NES" style CSS.

#### [NEW] [client.js](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/server/public/client.js)
- Connects to WebSocket.
- Sends inputs (Arrow keys, Space).
- Renders received state (Avatar pos, Level tiles) on Canvas.

### React SPA Migration
#### [NEW] [server/react-client](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/server/react-client)
- Vite + React + TypeScript (optional, sticking to JS for speed/consistency with previous files unless inferred otherwise, staying JS based on `server.js`).
- **Components**:
  - `App.jsx`: Main container.
  - `GameCanvas.jsx`: Handles Canvas Ref and Rendering loop.
  - `HUD.jsx`: Displays Score and Energy.
  - `ConnectionStatus.jsx`: Shows WS status.
- **Hooks**:
  - `useGameSocket`: Manages WS connection and state updates.

## Verification Plan

### Automated Tests
- `make test_emulation`:
    - Load Level 1.
    - Spawn Avatar.
    - Simulate 100 frames of running/jumping.
    - Verify Avatar reaches "Checkpoint" or interacts with "Boss".
