# Plan: Fix Verification & Embed Artifacts

## Goal

1. Resolving the `jest` execution failure for `Qube/QubeAgent.test.ts`.
2. Implementing the logic to "embed artifacts into permanent knowledge" by writing signed events to the ADK event log upon system triggers (like the Genesis Event).
3. Deploying the Docling Cluster locally and verifying service availability.

## User Review Required
>
> [!NOTE]
> The current `server.js` is a simple WebSocket server. We will likely need to extend it or wrap it to interact with the file system (for the event log).

## Proposed Changes

### 1. Fix Test Infrastructure

* **Investigate**: Rerun `jest` to capture full error.
* **Fix**: Likely adjusting `jest.config.js` or `package.json` imports, or fixing the `child_process` spawn path in the test.
  * Current Test Path: `QubeAgent.test.ts`
  * Target Server: `../server/server.js`
  * Potential Issue: `__dirname` resolution in `ts-jest`.

### 2. Implement Artifact Embedding

* **Design**: The "Genesis Event" in `server.js` should trigger the creation of an ADK-compliant Event.
  * **Event Type**: `emit` or `geneisis` (custom).
  * **Payload**: The simulation initialization data.
  * **Storage**: `knowledge/events/event_log.jsonl` (or similar).

#### [MODIFY] [server.js](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/server/server.js)

* Add `fs` write capability or call an external `adk` script to append the event.
* Ensure it adheres to `event.schema.json`.

### 3. Deploy Docling Cluster

* **Action**: Run `.\scripts\deploy-local.bat` in `Qube/docling-cluster`.
* **Verification**: Check `docker-compose ps` and hit health endpoints.

## Verification Plan

### Automated Tests

* Run `npx jest` and ensure it passes.
* Verify `output/events` contains a valid JSON line after the test runs.

### Manual Verification

* Verify Docling services (API, Vector Store, Ledger) are up.
* Check Docker container statuses.
