"""
ADK Core - Unified Shell CLI
The main dispatcher for the Agency Development Kit.
"""
import argparse
import sys
import json
import os
from pathlib import Path
try:
    import tomllib
except ImportError:
    import tomli as tomllib # Fallback or just use json/mock for now if deps missing

from adk_core.bridges.io_bridge import IOBridge
# from adk_core.bridges.ffi_bridge import FFIBridge # Placeholder
# from adk_core.bridges.rpc_bridge import RPCBridge # Placeholder
from adk_core.runtime.docking_shell import DockingShell

class UnifiedShell:
    """
    The Meta-Runtime: Routes user intent to the appropriate execution bridge or internal runtime.
    """
    
    def __init__(self, config_path=None):
        self.config = self._load_config(config_path)
        self.context = self._build_context()
        
        # Initialize bridges
        self.io_bridge = IOBridge(self.context)
        # self.ffi_bridge = FFIBridge(self.context)
        # self.rpc_bridge = RPCBridge(self.context)
        
        # Initialize Runtime (Lazy load usually, but here for demo)
        tensor_shape = tuple(self.config.get("hub", {}).get("tensor_shape", [10, 10, 10]))
        self.hub = DockingShell(tensor_shape=tensor_shape)

    def _load_config(self, config_path):
        """Load configuration from adk.toml."""
        if config_path:
            target = Path(config_path)
        else:
            target = Path.cwd() / "adk.toml"

        if target.exists():
            try:
                with open(target, "rb") as f:
                    return tomllib.load(f)
            except Exception as e:
                print(f"[Warning] Failed to load config: {e}")
        
        # Default Config
        return {
            "project": {"name": "ADK_Default"},
            "hub": {"tensor_shape": [10, 10, 10]},
            "bridges": {"default": "io"}
        }
    
    def _build_context(self):
        """Build the canonical context object."""
        return {
            "workspace_root": str(Path.cwd()),
            "user": os.environ.get("USER", "adk-user"),
            "session_id": "session-init",
            "environment": os.environ.get("ADK_ENV", "development")
        }
    
    def route(self, command, args):
        """
        The Gateway Pattern: Route commands to the appropriate bridge.
        """
        
        # 1. Internal Runtime Commands
        if command == "hub":
            return self._handle_hub_command(args)
            
        # 2. Bridge Commands
        routing_table = {
            "git": lambda: self.io_bridge.execute(["git"] + args.remainder),
            "terraform": lambda: self.io_bridge.execute(["terraform"] + args.remainder),
            "echo": lambda: self.io_bridge.execute(["echo"] + args.remainder),
        }
        
        if command not in routing_table:
            print(f"Error: Unknown command '{command}'")
            print(f"Available commands: hub, {', '.join(routing_table.keys())}")
            return 1
        
        return routing_table[command]()

    def _handle_hub_command(self, args):
        """Handle 'adk hub' subcommands."""
        if not args.remainder:
            print("Usage: adk hub [start|status]")
            return 1
        
        subcmd = args.remainder[0]
        
        if subcmd == "start":
            print(f"Starting Agency Hub for {self.config['project'].get('name')}...")
            # For demo, we just print the status, integrating the loop is next
            print("Hub Initialized.")
            print(f"Tensor Shape: {self.hub.tensor_field.shape}")
            return 0
            
        if subcmd == "status":
            print("Status: STANDBY")
            return 0
            
        print(f"Unknown hub command: {subcmd}")
        return 1

def main():
    parser = argparse.ArgumentParser(
        description="ADK - Agency Development Kit",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("command", help="Command to execute (hub, git, etc)")
    parser.add_argument("remainder", nargs=argparse.REMAINDER, help="Arguments")
    parser.add_argument("--config", help="Path to adk.toml")
    
    args = parser.parse_args()
    
    shell = UnifiedShell(config_path=args.config)
    result = shell.route(args.command, args)
    
    sys.exit(result)

if __name__ == "__main__":
    main()
