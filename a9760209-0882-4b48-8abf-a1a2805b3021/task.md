# Unified Shell Design

- [x] Draft Architecture Document (`unified_shell_design.md`)
- [x] Review with User
- [x] Scaffold Prototype Implementation

## Production Enhancements

- [ ] Infrastructure Setup
  - [ ] Create `requirements.txt` with dependencies
  - [ ] Create `adk.toml` configuration file
- [ ] TOML Configuration System
  - [ ] Implement `config.py` parser
  - [ ] Update `shell.py` to use new config
- [ ] Rich Logging System
  - [ ] Implement `logging_config.py`
  - [ ] Update all bridges for Rich output
- [ ] Error Handling & Retry Logic
  - [ ] Implement `errors.py` exception hierarchy
  - [ ] Implement `retry.py` with tenacity
- [ ] FFI Bridge (Real ctypes)
  - [ ] Create minimal C safety layer (`lib/safety_layer.c`)
  - [ ] Update `ffi_bridge.py` with real bindings
- [ ] RPC Bridge (gRPC Client)
  - [ ] Create `proto/shell_service.proto`
  - [ ] Implement `grpc_client.py`
  - [ ] Update `rpc_bridge.py` with gRPC
- [ ] Plugin System
  - [ ] Implement `plugins/base.py` interface
  - [ ] Implement `plugins/registry.py`
  - [ ] Update `shell.py` for dynamic routing
- [ ] Verification
  - [ ] Run all automated tests
  - [ ] Manual verification of Rich output
