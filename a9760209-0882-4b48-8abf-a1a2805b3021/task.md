# Hawkthorne Speedrun Bot

## Phase 1: Game Interface Layer

- [ ] Create `hawkthorne_bridge.lua` (State Observer + Input Injector)
- [ ] Implement IPC socket for JSON-RPC

## Phase 2: MCP Action Hub

- [ ] Create `mcp_action_server.py` with endpoints
  - [ ] `observe` - Get game state
  - [ ] `execute(action)` - Inject action
  - [ ] `checkpoint` - Validation snapshot
  - [ ] `handoff(context)` - Chain context passing
- [ ] Define handoff protocol schema

## Phase 3: LLM Agent Cluster

- [ ] Implement `agent_runner.py`
  - [ ] Planner agent (gemini-2.5-pro) - Route optimization
  - [ ] Executor agent (gemini-flash) - Frame-by-frame synthesis
  - [ ] Validator agent (gemini-pro) - Checkpoint verification
- [ ] Create agent handoff chain logic

## Phase 4: Tensor Manifold (Queen Boo)

- [ ] Implement worldline vector encoding
- [ ] Create `queen_boo.py` manifold generator
- [ ] Implement geodesic path computation

## Verification

- [ ] Level 1 Clear < 30s
- [ ] Boss Room Entry < 2 min
- [ ] Full Run < 10 min
