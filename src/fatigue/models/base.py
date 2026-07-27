from abc import ABC, abstractmethod


class LifeModel(ABC):

    @abstractmethod
    def life(self, stress_amplitude: float) -> float:
        """Return predicted fatigue life."""
        raise NotImplementedError

    @abstractmethod
    def allowable_stress(self, cycles: float) -> float:
        """Return allowable stress for a target life"""
        raise NotImplementedError
