"""Abstract interface for Spoke adapters (Field Games)."""
from abc import ABC, abstractmethod
from typing import Dict, Any, List

class SpokeAdapter(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def get_voxel_state(self) -> List[float]:
        pass

    @abstractmethod
    def receive_token(self, token: List[float]) -> Dict[str, Any]:
        pass
