# Release Bundle Orchestration Plan

I will act as the runtime orchestrator to produce the official V0 release bundle.

## Goal
Generate the distributable artifacts for the ADK, proving the "spine" works as intended.

## Proposed Steps

1.  **Validate Environment**: Ensure `adk/` exists and Docker is ready.
2.  **Execute Pack**: Run `.\adk.ps1 pack`.
    *   This triggers the Dockerized CLI.
    *   It archives `contracts/v0`.
    *   It generates a SHA256 checksum.
3.  **Verify Output**: Check for the existence of:
    *   `adk-contracts-v0.tar.gz`
    *   `adk-contracts-v0.tar.gz.sha256`
4.  **Validate Bundle**: Run `.\adk.ps1 verify <bundle>` to ensure the pack is valid.

## Outcome
A signed, stamped release bundle ready for distribution (simulating a GH Release).
