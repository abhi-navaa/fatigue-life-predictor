"""
Basquins stress life fatigue model
"""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike

from fatigue.exceptions import (
    InvalidCycleError,
    InvalidStressError,
    ModelNotApplicableError,
)
from fatigue.material import Material
from fatigue.models.base import LifeModel


class BasquinModel(LifeModel):
    """
    Stres life fatigue model based on basquins equation.

    Parameters
    -------------
    material
        material containing basquins fatigue properties.
    """

    def __init__(self, material: Material) -> None:

        self.material = material

        if material.fatigue_strength_coefficient is None:
            raise ModelNotApplicableError(
                " Material does not define fatigue strength coefficients."
            )
        if material.fatigue_strength_exponent is None:
            raise ModelNotApplicableError(
                " Material does not define fatigue_strength_exponent."
            )

    @property
    def sigma_f(self) -> float:
        return self.material.fatigue_strength_coefficient

    @property
    def b(self) -> float:
        return self.material.fatigue_strength_exponent

    def life(self, stress_amplitude: ArrayLike):
        """
        Predict fatigue life from stress amplitude.

        Parameters
        -----------

        stress_amplitude
            Alternating stress amplitude (MPa).

        Returns
        ---------

        float
            cycles to faliure.
        """
        stress = np.asarray(stress_amplitude, dtype=float)

        if np.any(stress <= 0):
            raise InvalidStressError("Stress amplitude must be positive")

        return 0.5 * (stress_amplitude / self.sigma_f) ** (1.0 / self.b)

    def allowable_stress(self, cycles: ArrayLike):
        """
        Predict aloowable stress for a desired fatigue life.
        """
        cycles = np.asarray(cycles, dtype=float)

        if np.any(cycles <= 0):
            raise InvalidCycleError("Cycles must be positive.")

        return self.sigma_f * (2.0 * cycles) ** self.b
