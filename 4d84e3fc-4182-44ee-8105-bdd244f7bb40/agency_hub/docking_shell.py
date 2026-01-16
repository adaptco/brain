from typing import Optional, Dict, Any, List, Tuple
import math
from tensor_field import TensorField
from spoke_interface import SpokeAdapter

class DockingShell:
    """
    The Hub (Pure Python).
    Coordinates the connection between the Voxelized Environment (Spoke)
    and the Cognitive Layer.
    """

    def __init__(self, tensor_shape: Tuple[int, ...] = (10, 10, 10)):
        print(f"[Hub] Initializing Docking Shell with Tensor Shape {tensor_shape}...")
        self.tensor_field = TensorField(tensor_shape)
        self.active_spoke: Optional[SpokeAdapter] = None
        self.eigen_manifold_history: List[List[float]] = []

    def dock(self, spoke: SpokeAdapter):
        print(f"[Hub] Docking Spoke: {spoke.name}")
        self.active_spoke = spoke

    def cycle(self) -> Dict[str, Any]:
        if not self.active_spoke:
            raise RuntimeError("No Spoke Docked!")

        # 1. Observe
        voxel_state = self.active_spoke.get_voxel_state()

        # 2. Update Field
        self.tensor_field.update_state(voxel_state)

        # 3. Normalize (Eigenstate Embedding)
        eigen_embedding = self.tensor_field.compute_eigen_embedding()
        self.eigen_manifold_history.append(eigen_embedding)

        # 4. Unify with RAG (Vector Dot Product)
        query_vec = eigen_embedding  
        rag_hits = self.tensor_field.map_rag_unification(query_vec)

        # 5. Generate Token
        token = self._synthesize_token(eigen_embedding, rag_hits)
        
        # 6. Act
        feedback = self.active_spoke.receive_token(token)
        
        return {
            "eigen_state_preview": eigen_embedding[:5], # Just show first 5 for creating log
            "rag_context": rag_hits,
            "feedback": feedback
        }

    def _synthesize_token(self, embedding: List[float], context: List) -> List[float]:
        # Simple heuristic: Tanh-like squash using math.tanh
        return [math.tanh(x) for x in embedding]
