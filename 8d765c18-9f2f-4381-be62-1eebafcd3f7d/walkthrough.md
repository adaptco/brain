# Walkthrough: Embedding Artifacts into Permanent Knowledge

## Summary

Implemented artifact embedding in the Ghost Void server, allowing events to be persisted to the ADK event log.

## Changes Made

### [server.js](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/server/server.js)

Added `embedEvent()` function that writes ADK-compliant events to a JSONL file:

```javascript
function embedEvent(type, payload, context = {}) {
    const event = {
        id: crypto.randomUUID(),
        type: type,
        timestamp: new Date().toISOString(),
        payload: payload,
        context: context
    };
    fs.appendFileSync(EVENT_LOG_PATH, JSON.stringify(event) + '\n');
    return event;
}
```

Wired the Genesis Event (`/deploy` command) to call `embedEvent('emit', ...)`.

## Validation

### Tests

```
Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
```

### Event Log Output

File: [event_log.jsonl](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/adk/output/event_log.jsonl)

```json
{
  "id": "5362711b-9645-497d-a769-e422feadf784",
  "type": "emit",
  "timestamp": "2026-01-21T18:43:20.693Z",
  "payload": { "timestamp": 1769021000692, "trigger": "deploy_command" },
  "context": { "source": "ghost_void_server", "command": "/deploy" }
}
```

✅ Event conforms to [event.schema.json](file:///c:/Users/eqhsp/.gemini/antigravity/knowledge/adk/contracts/v0/schemas/event.schema.json)

---

## Docling Cluster Deployment

### Status: In Progress ⏳

The Docling Cluster is currently being deployed via `.\scripts\deploy-local.bat`.

**Deployment includes:**

- **Infrastructure**: Redis (7-alpine), Qdrant (Vector Store)
- **Application Services**: Ingest API, Docling Worker, Embed Worker, Ledger
- **Dependencies**: Currently downloading and building ML stacks (Torch, CUDA).

**Current Command Output:**

```
[+] up 21/21
Downloading nvidia_cublas_cu...
Downloading torch-2.10.0...
```

The services will be available at:

- Ingest API: <http://localhost:8000>
- Vector Store: <http://localhost:6333>
- Ledger: <http://localhost:8001>
