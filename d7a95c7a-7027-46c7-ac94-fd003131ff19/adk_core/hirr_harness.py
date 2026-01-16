import json
import hashlib
from typing import Any, Dict

def deterministic_dumps(data: Any) -> str:
    """
    Serializes data to a JSON string deterministically.
    Enforces sort_keys=True and tight separators to avoid 
    layout-based non-determinism.
    """
    # separators=(',', ':') removes whitespace around separators
    return json.dumps(data, sort_keys=True, separators=(',', ':'))

def calculate_struct_hash(data: Any) -> str:
    """
    Calculates the SHA-256 hash of the deterministic JSON representation
    of a data structure.
    """
    json_str = deterministic_dumps(data)
    return hashlib.sha256(json_str.encode('utf-8')).hexdigest()

def verify_struct_integrity(data: Any, expected_hash: str) -> bool:
    """
    Verifies if a data structure matches its expected hash (Golden Path).
    """
    actual_hash = calculate_struct_hash(data)
    return actual_hash == expected_hash

class HirrHarness:
    """
    The High-Integrity Replay & Record (HIRR) Harness.
    """
    def __init__(self):
        self._registry = {} # Stores 'Golden Path' hashes

    def register_golden_hash(self, key: str, hash_val: str):
        self._registry[key] = hash_val

    def validate_state(self, key: str, current_state: Dict[str, Any]) -> bool:
        if key not in self._registry:
            raise KeyError(f"No golden hash registered for key: {key}")
        
        expected = self._registry[key]
        return verify_struct_integrity(current_state, expected)
