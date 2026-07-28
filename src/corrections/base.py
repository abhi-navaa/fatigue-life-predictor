from abc import ABC, abstractmethod


class MeanStressCorrection(ABC):
    """
    Base interface for mean stress correction models.
    """

    @abstractmethod
    def equivalent_stress(
        self,
        alternating_stress: float,
        mean_stress: float,
        ultimate_strength: float,
    ) -> float:
        """Return corrected alternating stress."""
        raise NotImplementedError
