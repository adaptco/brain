# Mega Man Game Engine Walkthrough

I have scaffolded the Mega Man Game Engine using the ADK framework.

## Components Implemented

### 1. Engine Core
- **[Orchestrator](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/include/engine/Orchestrator.hpp)**: Manages the game loop and sandbox.
- **[Sandbox](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/include/engine/Sandbox.hpp)**: Container for the entities and world model.
- **[WorldModel](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/include/engine/WorldModel.hpp)**: Generates procedural/mocked levels (currently implements rudimentary platforms and boss room logic).
- **[Physics](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/include/engine/Physics.hpp)**: Handles gravity, collision detection, and enforcement of safety bounds.

### 2. Agents
- **[Avatar](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/include/agents/Avatar.hpp)**: Implements Mega Man's state machine (Idle, Run, Jump, Shoot).
- **[Boss](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/include/agents/Boss.hpp)**: A basic Boss agent that tracks the player.

### 3. Build System
- **[Makefile](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/Makefile)**: Provided for compilation.

### 4. WebSocket Shell & React SPA Checkpoint
- **[server.js](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/server/server.js)**: A Node.js + Express server.
    - Serves the compiled React App from `../public` (which is where `react-client/dist` should go, or configured otherwise).
    - Note: Vite config builds to `../public`, so `server.js` serving `public` works perfectly.
- **[react-client](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/server/react-client)**: The React source code.

## How to Run

> [!WARNING]
> A C++ compiler (`g++` or similar) and `make` were not found in the current environment. You will need to install MinGW or use Visual Studio's developer command prompt to compile.

### 1. Compile Engine
```sh
g++ -I./include -std=c++17 src/main.cpp src/engine/*.cpp src/agents/*.cpp src/safety/*.cpp -o bin/ghost-void_engine.exe
```

### 2. Build and Run React SPA
```sh
cd server/react-client
npm install
npm run build
cd ..
npm install
node server.js
```
- Open a browser to `http://localhost:8080`.
- The connection status should turn green (if server is running).
- The Engine process will spawn when you connect (logic in server.js).

### Alternative: Run in Dev Mode
```sh
cd server/react-client
npm run dev
```
(You will need to ensure the WebSocket URL in `App.jsx` points to `ws://localhost:8080`).

## Verification
I have included a verification test file `tests/engine_test.cpp` which asserts that the Level Loading and Orchestrator initialization work correctly.
