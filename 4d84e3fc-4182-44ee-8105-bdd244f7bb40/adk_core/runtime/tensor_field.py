"""TensorField - Voxelized state and eigenvalue embedding."""
import math
from typing import List, Tuple

def vec_dot(v1: List[float], v2: List[float]) -> float:
    return sum(x*y for x, y in zip(v1, v2))

def vec_normalize(v: List[float]) -> List[float]:
    mag = math.sqrt(sum(x*x for x in v)) or 1.0
    return [x / mag for x in v]

class TensorField:
    def __init__(self, shape: Tuple[int, ...]):
        self.shape = shape
        size = 1
        for dim in shape:
            size *= dim
        self.state_tensor: List[float] = [0.0] * size
        self.rag_memory: List[List[float]] = []
        self.rag_keys: List[str] = []

    def update_state(self, new_tensor: List[float]):
        self.state_tensor = new_tensor

    def compute_eigen_embedding(self) -> List[float]:
        s = sorted([abs(x) for x in self.state_tensor], reverse=True)
        total = sum(s) + 1e-9
        return [x / total for x in s]

    def map_rag_unification(self, query: List[float], top_k: int = 3) -> List[Tuple[str, float]]:
        if not self.rag_memory:
            return []
        mem_dim = len(self.rag_memory[0])
        q = query[:mem_dim] if len(query) > mem_dim else query + [0.0]*(mem_dim - len(query))
        scores = [(self.rag_keys[i], vec_dot(q, m)) for i, m in enumerate(self.rag_memory)]
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]

    def ingest_knowledge(self, key: str, embedding: List[float]):
        self.rag_memory.append(vec_normalize(embedding))
        self.rag_keys.append(key)
