# ADAPTCO-ADK v0.1.0-alpha (Release Candidate)

## Overview

This bundle contains the compiled **Integrity Gate** for the ADK. It is designed to act as an unyielding law of gravity for your development lifecycle, ensuring environmental determinism and eliminating model drift.

## Contents

* `adk.exe`: The standalone CLI executable.
* `examples/`: Sample capsules for testing verification logic.

## Quick Start

The ADK does not require a shell to "dock"; it is self-contained. You can invoke it from any terminal.

### 1. Verification

Run the replay harness to verify the integrity of the binary itself:

```powershell
.\adk.exe replay
```

### 2. Validation

Validate your staged capsules:

```powershell
.\adk.exe validate
```

### 3. Commit

Use the ADK to wrap your git commits, ensuring the Integrity Gate is checked:

```powershell
.\adk.exe commit -m "Your commit message"
```
