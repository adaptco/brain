from abc import ABC, abstractmethod
from typing import Dict, Any, List

class SpokeAdapter(ABC):
    """
    The Interface Contract for 'Field Games'.
    Pure Python Version.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique identifier for this Spoke."""
        pass

    @abstractmethod
    def get_voxel_state(self) -> List[float]:
        """
        Returns the current state of the environment as a Flattened List.
        """
        pass

    @abstractmethod
    def receive_token(self, token: List[float]) -> Dict[str, Any]:
        """
        Accepts the 'Token' (Action Vector) from the Hub.
        """
        pass
