import time
import random
import math
from docking_shell import DockingShell
from spoke_interface import SpokeAdapter
from typing import Dict, Any, List

class DummyFieldGame(SpokeAdapter):
    def __init__(self, shape=(10, 10, 10)):
        self._shape = shape
        self._name = "Sandbox_Alpha"
        self._size = 1
        for s in shape: self._size *= s

    @property
    def name(self) -> str:
        return self._name

    def get_voxel_state(self) -> List[float]:
        # Return random noise
        return [random.random() for _ in range(self._size)]

    def receive_token(self, token: List[float]) -> Dict[str, Any]:
        avg = sum(token) / len(token) if token else 0
        return {"status": "ACK", "token_mean": f"{avg:.4f}"}

def learning_routine():
    print("=== Agency Docking Shell: Learning Routine (Pure Python) ===")
    
    # 1. Initialize
    spoke_shape = (10, 10, 10) # 1000 voxels
    game = DummyFieldGame(shape=spoke_shape)
    hub = DockingShell(tensor_shape=spoke_shape)
    
    # 2. Dock
    hub.dock(game)

    # 3. Bootstrap Knowledge (RAG)
    print(">>> Prime RAG Knowledge Base...")
    # Since our 'eigen-embedding' is the size of the input (1000) in this lite version,
    # we make our concepts that size.
    vec_size = 1000 
    for i in range(5):
        vec = [random.random() for _ in range(vec_size)]
        hub.tensor_field.ingest_knowledge(f"Concept_{i:03d}", vec)

    # 4. Learning Loops
    print(">>> Engaging Learning Loops (Eigen-Stablization)...")
    for epoch in range(5):
        print(f"\n--- Epoch {epoch+1} ---")
        result = hub.cycle()
        
        rag_context = result['rag_context']
        top_concept = rag_context[0] if rag_context else ("None", 0.0)
        
        # Calculate simplistic entropy of the preview
        preview = result['eigen_state_preview']
        # simple variance check
        mean = sum(preview)/len(preview)
        var = sum((x - mean)**2 for x in preview) / len(preview)

        print(f"   [State Variance]: {var:.4f}")
        print(f"   [RAG Unification]: Match -> {top_concept[0]} (Score: {top_concept[1]:.4f})")
        print(f"   [Spoke Feedback]: {result['feedback']}")

        time.sleep(0.2)

    print("\n=== Docking Sequence Complete. Shell is Active. ===")

if __name__ == "__main__":
    learning_routine()
