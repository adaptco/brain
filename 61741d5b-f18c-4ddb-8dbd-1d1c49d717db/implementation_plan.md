# Simulation Kernel Implementation Plan

## Goal Description
Create a "SimKernel" architecture to unify the physics engine, vehicle models (ISFModel), and avatar models (LexusAgent). This Kernel will serve as the runtime "OS" for the Agent, allowing objects to be plugged in as "containerized sockets" (modules). This structure enables the AI to build and manage its own simulation environment.

## Proposed Changes

### Game Architecture (`server/react-client/src/game/`)

#### [NEW] [SimKernel.js](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/server/react-client/src/game/SimKernel.js)
-   **Class `SimKernel`**: The core runtime "OS".
    -   `modules`: Map of pluggable tools (Physics, Renderer, AI).
    -   `entities`: List of active world objects.
    -   `plug(name, module)`: Method to attach containerized sockets.
    -   `start()`, `stop()`, `loop()`: Main executive loop.

#### [NEW] [PhysicsSocket.js](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/server/react-client/src/game/PhysicsSocket.js)
-   **Class `PhysicsSocket`**: A module that implements the physics logic.
    -   Connects `ISFModel` physics updates to the Kernel loop.
    -   Manages global physics properties (gravity, drag).

#### [MODIFY] [LexusAgent.js](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/server/react-client/src/game/LexusAgent.js)
-   Implement `onSpawn(kernel)` to register with the OS.
-   Update `update(deltaTime)` to be time-step independent.

#### [MODIFY] [ISFModel.js](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/server/react-client/src/game/ISFModel.js)
-   Refine `update()` to accept `deltaTime`.
-   Ensure physical properties are accessible to `PhysicsSocket`.

### React Components (`server/react-client/src/components/`)

#### [MODIFY] [GameCanvas.jsx](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/server/react-client/src/components/GameCanvas.jsx)
-   Refactor to instantiate `SimKernel`.
-   Create a `RendererSocket` adapter to pass the Canvas 2D context to the Kernel.
-   Remove manual game loop logic (delegate to Kernel).

## Verification Plan

### Manual Verification
1.  **Launch Server**: Start the local development server (`npm run dev` in `server/react-client`).
2.  **Browser Check**: Open the game URL.
3.  **Observation**:
    -   Verify `LexusAgent` (Blue Box) spawns and moves.
    -   Verify physics works (acceleration/braking/steering).
    -   Check Console logs for "Kernel Boot" and "Socket Plugged" messages.
