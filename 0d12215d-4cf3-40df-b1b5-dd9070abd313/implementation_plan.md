# Agentic RAG Pipeline Implementation Plan

## Goal Description

Create a comprehensive simulation of an Agentic RAG workflow involving a Helper Bot (Claude API), a Worker for RAG tasks, LoRa model generation scripts, Pandas automation ("Panda"), and an auto-linting tool. This fulfills the user's request to "Show Gemini Code Assist actions" by building the requested architecture.

## User Review Required
>
> [!NOTE]
> This plan assumes a "greenfield" creation of these scripts within the current workspace. No external API keys are hardcoded; placeholders will be used for the Claude API.

## Proposed Changes

We will create a modular Python project structure.

### Project Root

#### [NEW] [requirements.txt](file:///c:/Users/eqhsp/.gemini/antigravity/brain/0d12215d-4cf3-40df-b1b5-dd9070abd313/requirements.txt)

- `anthropic`
- `pandas`
- `pylint`

### Agent & Worker

#### [NEW] [bot.py](file:///c:/Users/eqhsp/.gemini/antigravity/brain/0d12215d-4cf3-40df-b1b5-dd9070abd313/src/bot.py)

- Main entry point.
- Initializes the "Helper Bot" using `anthropic` client (mocked/stubbed).
- Dispatches tasks to the Worker.

#### [NEW] [worker.py](file:///c:/Users/eqhsp/.gemini/antigravity/brain/0d12215d-4cf3-40df-b1b5-dd9070abd313/src/worker.py)

- Receives tasks.
- Calls RAG and Model Generation modules.

### Modules

#### [NEW] [rag.py](file:///c:/Users/eqhsp/.gemini/antigravity/brain/0d12215d-4cf3-40df-b1b5-dd9070abd313/src/rag/rag.py)

- Implementation of the RAG logic (simulated retrieval).

#### [NEW] [lora.py](file:///c:/Users/eqhsp/.gemini/antigravity/brain/0d12215d-4cf3-40df-b1b5-dd9070abd313/src/lora/lora.py)

- Scripts for "LoRa" and "Extender" model generation logic.

#### [NEW] [panda_script.py](file:///c:/Users/eqhsp/.gemini/antigravity/brain/0d12215d-4cf3-40df-b1b5-dd9070abd313/src/scripts/panda_script.py)

- Pandas script to "create a Panda" (data processing).

### Tools

#### [NEW] [lint_roller.py](file:///c:/Users/eqhsp/.gemini/antigravity/brain/0d12215d-4cf3-40df-b1b5-dd9070abd313/src/tools/lint_roller.py)

- "Auto roll lint" tool using `pylint`.

## Verification Plan

### Automated Tests

- Run the `bot.py` script and check console output for the sequence:
    1. Bot activates.
    2. Worker starts.
    3. RAG retrieval happens.
    4. LoRa script runs.
    5. Panda script runs.
    6. Lint roller finishes.

Command: `python src/bot.py`
