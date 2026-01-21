# Game App Shell Implementation Plan

## Goal Description

Create a "Game App Shell" within the React Client. This will be a "Retro Terminal" style overlay that allows the user to input commands directly to the engine and view logs/output. This enhances the "scaffolding" feel and provides the requested "Shell".

## Proposed Changes

### React Client

#### [NEW] [Terminal.jsx](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/server/react-client/src/components/Terminal.jsx)

- A component that renders a scrolling log of texts.
- An input line at the bottom.
- Handled commands:
  - `/deploy` -> Sends `{"type": "genesis_plane"}` to server (triggering Boss).
  - `/clear` -> Clears local log.
  - `*` -> Sends raw input to server.
- Visuals: Dark background, green monospace text, semi-transparent overlay.

#### [MODIFY] [App.jsx](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/server/react-client/src/App.jsx)

- Import and render `<Terminal />`.
- Pass `sendInput` or similar mechanism to Terminal.
- Layout: Position the terminal as an overlay or below the canvas.

#### [MODIFY] [index.css](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/server/react-client/src/index.css)

- Add CSS classes for `.terminal`, `.terminal-log`, `.terminal-input`.

## Verification Plan

### Manual Verification

- Start `npm run dev` (client) and `npm run start` (server).
- Open browser.
- Type `/deploy` in the new terminal component.
- Verify "Genesis Plane" appears in game and "Deploying model" logs appear in the terminal window (if we pipe logs back, which `server.js` does via `engine.stdout.on`).
