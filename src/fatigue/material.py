"""
material definition of fatigue analysis.
All stress-related properties are expressed in MPA unless otherwise noted.

"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Material:
    """
    Represent the mechanical and fatigue properties of the material.

    Parameters
    -------------
    name : str
        Material designation.

    elastic modulus : float
        Young's Modulus (MPa).

    poisson_ratio : float
        Poisson's ratio.

    yield strength : float
        Yield strength (MPa).

    ultimate_strength : float
        Ultimate tensile strength (Mpa).

    density : float | None
        Density (kg/m^3)

    endurance limit : float | None
        Endurance Limit (Mpa)

    fatigue_strength_coefficient : float | None
        Basquin's fatigue strength coefficient (MPa)

    fatigue_strength_exponent : float | None
        Basquin's exponeent

    """

    name: str

    elastic_modulus: float
    poissons_ratio: float

    yield_strength: float
    ultimate_strength: float

    density: float | None = None

    endurance_limit: float | None = None

    fatigue_strength_coefficient: float | None = None
    Fatigue_strenth_exponenet: float | None = None

    def __post_init__(self) -> None:

        if self.elastic_modulus <= 0:
            raise ValueError("Elastic Modulus must be positive")

        if not (0.00 < self.poissons_ratio < 0.50):
            raise ValueError("Poissons ratio must be between 0 and 0.5")

        if self.yield_strength <= 0:
            raise ValueError("Yield strength must be positive")

        if self.ultimate_strength <= 0:
            raise ValueError(" Ultimate tensile strength must be positive")

        if self.yield_strength > self.ultimate_strength:
            raise ValueError("yield cannot exceed ultimate strength")

        if self.endurance_limit is not None and self.endurance_limit <= 0:
            raise ValueError("Endurance limit must be positive")

        if self.density is not None and self.density <= 0:
            raise ValueError("Density must be positive")
