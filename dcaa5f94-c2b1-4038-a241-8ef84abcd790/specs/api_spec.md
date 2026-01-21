# External Tool API Specification

This document defines the HTTP interface that the "External Tool" must expose to receive events from Zapier.

## Base Configuration

* **Protocol**: HTTPS (Required for Zapier)
* **Authentication**: Bearer Token or API Key (recommended) passed in headers.
* **Content-Type**: `application/json`

## Endpoints

### 1. Receive Agent Event

**Method**: `POST`
**Path**: `/webhook/agent-event`
**Description**: Ingests a new task or event from Zapier.

**Request Body**:
(See [payload_contract.json](../contracts/payload_contract.json))

```json
{
  "event_key": "rec123456789",
  "event_type": "Run Analysis",
  "session_id": "sess_abc123",
  "timestamp": "2023-10-27T10:00:00Z",
  "context": {
    "user_input": "Analyze quarterly report",
    "file_url": "..."
  }
}
```

**Response**:

* **200 OK**: Event received successfully. Code should be executing async (don't block for long tasks).

    ```json
    { "status": "accepted", "message": "Processing started" }
    ```

* **400 Bad Request**: Invalid payload.
* **500 Internal Server Error**: Downstream failure.

### 2. Callback (Outbound from Tool)

**Method**: `POST`
**Target**: Zapier Webhook URL (Zap D)
**Description**: The external tool must call this URL upon completion.

**Request Body**:

```json
{
  "event_key": "rec123456789",
  "status": "Complete",
  "summary": "Analysis finished. Found 3 anomalies.",
  "severity": "Info",
  "output_data": { ... }
}
```
