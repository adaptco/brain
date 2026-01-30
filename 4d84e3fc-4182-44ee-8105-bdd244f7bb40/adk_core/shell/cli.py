"""
ADK Core - Unified Shell CLI
The main dispatcher for the Agency Development Kit.
"""
import argparse
import sys
import json
import os
from pathlib import Path

from adk_core.bridges.io_bridge import IOBridge
from adk_core.runtime.docking_shell import DockingShell

class UnifiedShell:
    """The Meta-Runtime: Routes user intent to bridges or internal runtime."""
    
    def __init__(self, config_path=None):
        self.config = self._load_config(config_path)
        self.context = self._build_context()
        self.io_bridge = IOBridge(self.context)
        tensor_shape = tuple(self.config.get("hub", {}).get("tensor_shape", [10, 10, 10]))
        self.hub = DockingShell(tensor_shape=tensor_shape)

    def _load_config(self, config_path):
        """Load configuration from adk.toml or JSON fallback."""
        target = Path(config_path) if config_path else Path.cwd() / "adk.toml"
        if target.exists():
            try:
                # Try TOML first (Python 3.11+)
                import tomllib
                with open(target, "rb") as f:
                    return tomllib.load(f)
            except ImportError:
                # Fall back to JSON config
                json_path = target.with_suffix(".json")
                if json_path.exists():
                    with open(json_path) as f:
                        return json.load(f)
            except Exception as e:
                print(f"[Warning] Config load failed: {e}")
        return {"project": {"name": "ADK"}, "hub": {"tensor_shape": [10, 10, 10]}}
    
    def _build_context(self):
        return {
            "workspace_root": str(Path.cwd()),
            "user": os.environ.get("USER", "adk-user"),
            "session_id": "session-init",
            "environment": os.environ.get("ADK_ENV", "development")
        }
    
    def route(self, command, args):
        if command == "hub":
            return self._handle_hub_command(args)
        routing_table = {
            "git": lambda: self.io_bridge.execute(["git"] + args.remainder),
            "echo": lambda: self.io_bridge.execute(["echo"] + args.remainder),
        }
        if command not in routing_table:
            print(f"Error: Unknown command '{command}'")
            print(f"Available: hub, {', '.join(routing_table.keys())}")
            return 1
        return routing_table[command]()

    def _handle_hub_command(self, args):
        if not args.remainder:
            print("Usage: adk hub [start|status]")
            return 1
        subcmd = args.remainder[0]
        if subcmd == "start":
            print(f"[ADK] Starting Hub: {self.config['project'].get('name')}")
            print(f"[ADK] Tensor Shape: {self.hub.tensor_field.shape}")
            return 0
        if subcmd == "status":
            print("[ADK] Hub Status: STANDBY")
            return 0
        print(f"Unknown hub command: {subcmd}")
        return 1

def main():
    parser = argparse.ArgumentParser(description="ADK - Agency Development Kit")
    parser.add_argument("command", help="Command (hub, git, etc)")
    parser.add_argument("remainder", nargs=argparse.REMAINDER)
    parser.add_argument("--config", help="Path to adk.toml")
    args = parser.parse_args()
    shell = UnifiedShell(config_path=args.config)
    sys.exit(shell.route(args.command, args))

if __name__ == "__main__":
    main()
