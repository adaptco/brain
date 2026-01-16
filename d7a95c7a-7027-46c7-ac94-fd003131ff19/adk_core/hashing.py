import hashlib
import os

def normalize_newlines(content: bytes) -> bytes:
    """
    Normalizes line endings to \n (Unix-style) to ensure cross-platform
    determinism between Windows and Linux environments.
    """
    # Replace Windows \r\n with \n
    return content.replace(b'\r\n', b'\n')

def calculate_file_hash(filepath: str) -> str:
    """
    Calculates the SHA-256 hash of a file after normalizing line endings.
    This acts as the 'Hashing Anchor' for the ADK.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    sha256_hash = hashlib.sha256()
    
    with open(filepath, "rb") as f:
        content = f.read()
        
    # Crucial: Normalize before hashing
    normalized_content = normalize_newlines(content)
    sha256_hash.update(normalized_content)
    
    return sha256_hash.hexdigest()

def verify_file_integrity(filepath: str, expected_hash: str) -> bool:
    """
    Verifies if a file matches its expected hash.
    """
    actual_hash = calculate_file_hash(filepath)
    return actual_hash == expected_hash
