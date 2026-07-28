"""
Goodman Stress Correction
"""

import numpy as np
from numpy.typing import ArrayLike

from corrections.base import MeanStressCorrection
from fatigue.exceptions import InvalidMaterialError, InvalidStressError
from fatigue.material import Material


class GoodmanCorrection(MeanStressCorrection):
    """
    Stress correction model based on goodman equation.

    Parameters
    -------------
    material
        material containing basquins fatigue properties.
    """

    def __init__(self, material: Material) -> None:

        self.material = material

        if material.ultimate_strength is None:
            raise InvalidMaterialError(" Material does not define ultimate strength.")
        if material.ultimate_strength <= 0:
            raise InvalidMaterialError(" Ultimate tensile strength must be positive.")

    @property
    def S_ut(self) -> float:
        return self.material.ultimate_strength

    def equivalent_stress(
        self,
        stress_amplitude: ArrayLike,
        mean_stress: ArrayLike,
    ) -> np.ndarray:
        """
        Evaluate goodman correction

        Parameters
        -----------

        stress_amplitude
            Alternating stress amplitude (MPa).

        mean_stress
            Mean stress value (MPa).

        Returns
        ---------

        float
            Equivalent stress (MPa).
        """
        sigma_a = np.asarray(stress_amplitude, dtype=float)
        sigma_m = np.asarray(mean_stress, dtype=float)
        if np.any(sigma_m >= self.S_ut):
            raise InvalidStressError("Mean stress must be less than ultimate strength.")

        return sigma_a / (1 - sigma_m / self.S_ut)
