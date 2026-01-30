"""IO Bridge - Subprocess Wrapper for external tools."""
import subprocess
import json
import os
from typing import List, Dict, Any

class IOBridge:
    """Execute external commands via subprocess with context propagation."""
    
    def __init__(self, context: Dict[str, Any]):
        self.context = context
    
    def execute(self, command: List[str]) -> int:
        print(f"[IO Bridge] Executing: {' '.join(command)}")
        env = os.environ.copy()
        env["ADK_CONTEXT_JSON"] = json.dumps(self.context)
        env["ADK_WORKSPACE_ROOT"] = self.context.get("workspace_root", "")
        try:
            result = subprocess.run(command, env=env, capture_output=True, text=True)
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(f"[stderr] {result.stderr}")
            return result.returncode
        except FileNotFoundError:
            print(f"[IO Bridge] Command not found: {command[0]}")
            return 127
        except Exception as e:
            print(f"[IO Bridge] Error: {e}")
            return 1
