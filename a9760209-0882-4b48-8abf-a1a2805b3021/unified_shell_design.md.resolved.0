# Unified Shell Architecture: Bridging the Runtime

## The Challenge
Modern development environments are fragmented. We often have:
*   **Infrastructure** defined in Terraform/Go.
*   **Core Logic** in C++/Rust (for performance/safety).
*   **Scripts/Glue** in Python or Bash.
*   **Web/UI** in Node.js/TypeScript.

The goal of the **Unified Shell** (`adk`) is to act as the single **Control Surface** that bridges these distinct runtimes into a coherent, deterministic developer experience. It is not just a "script runner"; it is a **Protocol Translator**.

## Core Architecture

### 1. The Surface Layer (The "Shell")
*   **Role**: The user interface and command dispatcher.
*   **Language**: High-level, rapid iteration (Python).
*   **Responsibility**:
    *   Argument parsing (`argparse`/`click`).
    *   UX/UI (Rich terminal output, progress bars).
    *   **Configuration normalization** (reading `adk.toml` and injecting it into subprocesses).

### 2. The Bridge Layer (The "Interconnect")
To "bridge the runtime," we employ three distinct binding patterns depending on the fidelity required:

#### A. The IO Bridge (Subprocess/Stdio)
*   **Use Case**: Loosely coupled tools (e.g., invoking `git`, `terraform`, or standalone binaries).
*   **Mechanism**: The Shell spawns a child process, pipes `stdin`/`stdout`/`stderr`, and captures exit codes.
*   **The "Unified" Trick**: The Shell wraps the raw output in structured logging. A raw `gcc` error is caught and re-rendered as a formatted ADK alert.
*   **Example**: `adk commit` wrapping `git commit`.

#### B. The FFI Bridge (shared library)
*   **Use Case**: High-performance or Normative Logic (e.g., the "Safety Layer" or cryptographic hashing).
*   **Mechanism**: Python `ctypes` or `cffi` loads a compiled `.so`/`.dll` (e.g., `libsafetylayer.so`).
*   **Benefit**: Zero-latency calls, shared memory state. The Python shell can directly invoke C++ functions to validate a schema *before* any process starts.

#### C. The RPC Bridge (Socket/HTTP)
*   **Use Case**: Isolation or Heavy Environments (e.g., The "Node 6 Actuator" running in a Docker container).
*   **Mechanism**: The Shell spins up a sidecar (daemon) or connects to a running container via gRPC or local socket.
*   **Benefit**: Environment purity. The heavy runtime dependencies (specific JDK, massive ML models) live in the container; the Shell remains lightweight and just sends "Commands".

## Implementation Strategy

### Step 1: The Gateway Pattern
Command routing is decoupled from execution.
```python
# adk.py (Pseudo-code)
def route_command(cmd, args):
    if cmd == "validate":
        # Direct Python Call
        return internal_validator.run(args)
    elif cmd == "simulate":
        # RPC Call to heavy math engine
        return rpc_client.send("simulate", args)
    elif cmd == "deploy":
        # Subprocess Call to Terraform
        return subprocess.run(["terraform", "apply"] + args)
```

### Step 2: The Canonical Context
The Bridge must pass context, not just flags.
*   **The Context Object**: A serializable JSON/Dict containing the *current state* (Auth, Workspace Root, Active Capsule).
*   **Propagation**:
    *   To Subprocess: via Environment Vectors (`ADK_CONTEXT_JSON=...`).
    *   To RPC: via Header Metadata.
    *   To FFI: via Struct pointer.

## Conclusion
You create a unified shell by accepting that the "Shell" is a **Meta-Runtime**. It owns the *Intent* of the user ("Validate", "Deploy") and translates that intent into the specific *Dialect* of the underlying tool (C++ function call, CLI argument, API request), ensuring the user never has to context-switch between those dialects themselves.
