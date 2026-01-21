# Finalize Emergence & Launch Playground

We are finalizing the "Big Boss Emergence" feature and the new "Terminal" component in the Playground. This will allow for sandbox testing of agent behaviors via the web interface.

## User Review Required

> [!IMPORTANT]
> This plan commits all currently uncommitted changes in `ghost-void`, which is assumed to be the correct workspace behavior.

## Proposed Changes

### Ghost Void Engine (`/antigravity/playground/ghost-void`)

#### [MODIFY] [Makefile](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/Makefile)

- Added `test_engine` target to build and run engine tests.

#### [MODIFY] [BigBoss.hpp](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/include/agents/BigBoss.hpp) / [BigBoss.cpp](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/src/agents/BigBoss.cpp)

- Implemented `DeployEmergence` method for spawning the Genesis Plane.

#### [MODIFY] [Boss.hpp](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/include/agents/Boss.hpp) / [Boss.cpp](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/src/agents/Boss.cpp)

- Added virtual `DeployEmergence` method to base class.

#### [MODIFY] [Orchestrator.cpp](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/src/engine/Orchestrator.cpp)

- Added logic to parse "genesis_plane" command and trigger `TriggerGenesis()`.

#### [MODIFY] [Sandbox.hpp](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/include/engine/Sandbox.hpp) / [Sandbox.cpp](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/src/engine/Sandbox.cpp)

- Added `TriggerGenesis` method to delegate to the Boss.

#### [NEW] [Terminal.jsx](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/server/react-client/src/components/Terminal.jsx)

- React component for the in-game terminal shell.

#### [MODIFY] [App.jsx](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/server/react-client/src/App.jsx)

- Integrated `Terminal` component into the main layout.

#### [MODIFY] [index.css](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/server/react-client/src/index.css)

- Added styles for the Terminal overlay.

#### [MODIFY] [boss_test.cpp](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/tests/boss_test.cpp)

- Added unit tests for `DeployEmergence`.

## Verification Plan

### Automated Tests

Run the following commands in `ghost-void` root:

```sh
make test        # Runs safety_test
make test_engine # Runs engine_test (includes component tests)
```

Compile and run `boss_test` manually if needed:

```sh
g++ -I./include -std=c++17 tests/boss_test.cpp src/agents/BigBoss.cpp src/agents/Boss.cpp src/engine/Physics.cpp src/engine/WorldModel.cpp src/safety/SafetyLayer.cpp -o bin/boss_test
./bin/boss_test
```

### Manual Verification

1. **Build Frontend**:

    ```sh
    cd server/react-client
    npm install
    npm run build
    ```

2. **Start Server**:

    ```sh
    cd server
    npm install
    node server.js
    ```

3. **Playground Test**:
    - Open `http://localhost:8080`.
    - Verify the "GHOST VOID SHELL" is visible at the bottom.
    - Type `/deploy` and press Enter.
    - Check the terminal logs for command confirmation.
    - Verify in the game canvas that a new plane appears (if visual feedback is available) or server logs confirm "deploying emergence".
