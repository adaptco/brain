# Ghost Void Game - Implementation Plan

## Goal

Scaffold a dual-process application (Node.js Server + React Client) featuring a "Terminal Shell" interface and a game canvas.

## Proposed Architecture

### 1. Game Server (`server/`)

- **Runtime**: Node.js
- **Dependencies**: `ws` (WebSockets), `express` (optional, for static serving later).
- **Key File**: `server.js`
  - Manages WS connections.
  - Listens for `CMD_DEPLOY` from the terminal.
  - Broadcasts `GENESIS_EVENT` to clients.

### 2. React Client (`server/react-client/`)

- **Tooling**: Vite + React
- **Styling**: CSS Modules or simple CSS (Dark/Cyberpunk theme).
- **Components**:
  - `App.jsx`: Main layout.
  - `GameCanvas.jsx`: Pure HTML5 Canvas renderer for the "Game". handles Z (shoot) and Arrow (move) inputs.
  - `Terminal.jsx`: Overlay shell. Parses text input. Handles `/deploy`.

## Step-by-Step Implementation

1. **Server Scaffold**:
    - Create `server/package.json`.
    - Write `server.js` with basic "echo" and "command parsing" logic.
2. **Client Scaffold**:
    - Use `npm create vite@latest` (simulated via file creation) to set up React.
    - Implement `Terminal.jsx` with an input loop and history display.
    - Implement `GameCanvas.jsx` with a basic requestAnimationFrame loop.
3. **Integration**:
    - Connect Client `ws` to `localhost:8080`.
    - Ensure `/deploy` in Terminal -> Sends msg to Server -> Server logs "Big Boss Triggered" -> Server sends "Genesis" -> Client shows visual effect.

## User Verification

- Run `node server.js` in one term.
- Run `npm run dev` in another.
- Visit localhost.
