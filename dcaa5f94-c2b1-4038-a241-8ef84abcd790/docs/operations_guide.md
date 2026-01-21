# Operational Guide: Zapier-Native Architecture

## Debugging & Failure Recovery

### 1. The "Stuck" Event

**Symptom**: `AgentEvent` stays in "Pending" status forever.
**Diagnosis**:

* Check **Zap History** for Zap B (Routing) or Zap C (External Tool).
* If Zap C failed, the webhook didn't reach the External Tool.
* If Zap C succeeded, the External Tool failed to call back (Zap D).
**Recovery**:
* **Manual Retry**: Replay the Zap run in Zapier History.
* **Force Close**: Manually update the `AgentEvents` row status to "Failed" in Zapier Tables to unblock any dependent logic.

### 2. Loop Detection

**Symptom**: Infinite events being generated.
**Prevention**:

* Ensure Zap A (Button) only creates *one* event per click.
* Ensure the External Tool does *not* trigger a new "Run Analysis" event upon completion, but instead updates the existing one.
**Recovery**:
* Turn off Zaps A and B immediately.
* Clear the `AgentEvents` table of spurious pending records.

## Scaling Strategy (Zapier Limits)

### 1. Task Usage

* **Optimization**: Use **Paths** (Logic) in a single Zap rather than chaining multiple separate Zaps where possible, to keep logic contained.
* **Batching**: If high volume, consider buffering events in the External Tool and updating Zapier via API in batches (though Zapier Tables API is record-by-record).

### 2. Rate Limiting

* Zapier Webhooks have rate limits.
* **Strategy**: If your External Tool sends updates too fast, implement a queue/throttle on the External Tool side to space out callbacks to Zap D.

### 3. Data Retention

* Zapier Tables has record limits (e.g., 50k records).
* **Strategy**: Implement an archiving routine (a separate Zap runs weekly) that deletes `Completed` events older than 30 days or exports them to Google Sheets/Airtable before deletion.
