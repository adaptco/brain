# Unified Shell Production Enhancements

## Goal Description

Upgrade the unified shell prototype to production-ready status with six major enhancements: FFI bindings, gRPC client, TOML configuration, Rich logging, error handling, and plugin system.

## User Review Required

> [!IMPORTANT]
> **C++ Safety Layer**: The FFI bridge requires a compiled C++ library (`libsafetylayer.dll`/`.so`). This plan includes a minimal C implementation for demonstration. For production, you would replace this with your actual safety layer library.

> [!WARNING]
> **gRPC Dependency**: The RPC bridge requires `grpcio` and `grpcio-tools` packages. These will be added to requirements.txt.

---

## Proposed Changes

### Infrastructure

#### [NEW] [requirements.txt](file:///c:/Users/eqhsp/code/adaptco/unified_shell_proto/requirements.txt)

- `tomli` - TOML parsing (stdlib in 3.11+)
- `rich` - Beautiful terminal output
- `grpcio` / `grpcio-tools` - gRPC communication
- `tenacity` - Retry logic

#### [NEW] [adk.toml](file:///c:/Users/eqhsp/code/adaptco/unified_shell_proto/adk.toml)

- Production configuration file with all bridge settings

---

### 1. TOML Configuration System

#### [NEW] [config.py](file:///c:/Users/eqhsp/code/adaptco/unified_shell_proto/config.py)

- Parse `adk.toml` using tomli
- Environment variable overrides
- Default fallback values

#### [MODIFY] [shell.py](file:///c:/Users/eqhsp/code/adaptco/unified_shell_proto/shell.py)

- Replace JSON loading with TOML parser
- Use new Config class

---

### 2. Rich Logging System

#### [NEW] [logging_config.py](file:///c:/Users/eqhsp/code/adaptco/unified_shell_proto/logging_config.py)

- Rich console with panels, tables, progress bars
- Structured log formatting
- Color-coded bridge identification

#### [MODIFY] All bridge files

- Replace `print()` with Rich console output
- Add progress spinners for long operations

---

### 3. Error Handling & Retry Logic

#### [NEW] [errors.py](file:///c:/Users/eqhsp/code/adaptco/unified_shell_proto/errors.py)

- Custom exception hierarchy:
  - `ShellError` (base)
  - `BridgeError` (bridge failures)
  - `RetryableError` (transient failures)
  - `FatalError` (unrecoverable)

#### [NEW] [retry.py](file:///c:/Users/eqhsp/code/adaptco/unified_shell_proto/retry.py)

- Retry decorator using tenacity
- Configurable backoff strategies
- Per-bridge retry policies

---

### 4. FFI Bridge (Real ctypes Bindings)

#### [NEW] [lib/safety_layer.c](file:///c:/Users/eqhsp/code/adaptco/unified_shell_proto/lib/safety_layer.c)

- Minimal C implementation for demonstration:
  - `validate_schema(const char* json_str)` → int
  - `compute_hash(const char* data, size_t len)` → uint64_t
  - `clip_value(double value, double min, double max)` → double

#### [MODIFY] [bridges/ffi_bridge.py](file:///c:/Users/eqhsp/code/adaptco/unified_shell_proto/bridges/ffi_bridge.py)

- Real ctypes bindings with proper type definitions
- Error code translation
- Memory safety guards

---

### 5. RPC Bridge (gRPC Client)

#### [NEW] [proto/shell_service.proto](file:///c:/Users/eqhsp/code/adaptco/unified_shell_proto/proto/shell_service.proto)

- Service definition for remote commands
- Message types for simulate/deploy

#### [NEW] [bridges/grpc_client.py](file:///c:/Users/eqhsp/code/adaptco/unified_shell_proto/bridges/grpc_client.py)

- Generated gRPC stubs wrapper
- Connection pooling
- Timeout handling

#### [MODIFY] [bridges/rpc_bridge.py](file:///c:/Users/eqhsp/code/adaptco/unified_shell_proto/bridges/rpc_bridge.py)

- Use gRPC client instead of stubs
- Integrate retry logic
- Add health checking

---

### 6. Plugin System

#### [NEW] [plugins/base.py](file:///c:/Users/eqhsp/code/adaptco/unified_shell_proto/plugins/base.py)

- `BaseBridge` abstract class
- Plugin interface contract

#### [NEW] [plugins/registry.py](file:///c:/Users/eqhsp/code/adaptco/unified_shell_proto/plugins/registry.py)

- Dynamic bridge registration
- Plugin discovery from directory
- Route table extension

#### [MODIFY] [shell.py](file:///c:/Users/eqhsp/code/adaptco/unified_shell_proto/shell.py)

- Use plugin registry for routing
- Support `--plugin-dir` CLI flag

---

## Verification Plan

### Automated Tests

1. **Unit Tests** - Run with pytest:

   ```bash
   cd c:/Users/eqhsp/code/adaptco/unified_shell_proto
   python -m pytest tests/ -v
   ```

2. **Config Loading Test**:

   ```bash
   python -c "from config import Config; c = Config('adk.toml'); print(c)"
   ```

3. **FFI Bridge Test** (requires compiled library):

   ```bash
   python shell.py validate test.json
   python shell.py hash somefile.txt
   ```

4. **IO Bridge Test**:

   ```bash
   python shell.py git --version
   ```

### Manual Verification

1. **Rich Output**: Run any command and verify colorized, formatted output appears in terminal
2. **Error Handling**: Run `python shell.py unknown_command` and verify graceful error message
3. **Plugin Discovery**: Add a custom plugin to `plugins/` directory and verify it registers
