import numpy as np
import pytest

from corrections.goodman import GoodmanCorrection
from fatigue.exceptions import (
    InvalidMaterialError,
    InvalidStressError,
)
from fatigue.material import Material


@pytest.fixture
def steel():

    return Material(
        name="Demo Steel",
        elastic_modulus=210000,
        poissons_ratio=0.30,
        yield_strength=550,
        ultimate_strength=650,
        fatigue_strength_coefficient=1000.0,
        fatigue_strength_exponent=-0.10,
    )


def test_mean_stress_zero(steel):

    model = GoodmanCorrection(steel)
    mean_stress = np.array([0, 0, 0])
    stress_amplitude = np.array([100.0, 100.0, 100.0])
    stress_amp = model.equivalent_stress(stress_amplitude, mean_stress)
    assert stress_amp[0] == stress_amp[1] == stress_amp[2]


def test_mean_stress_tensile(steel):

    model = GoodmanCorrection(steel)
    mean_stress = np.array([200.0, 250.0, 300.0])
    stress_amplitude = np.array([100.0, 100.0, 100.0])
    stress_eq = model.equivalent_stress(stress_amplitude, mean_stress)
    assert stress_eq[0] < stress_eq[1] < stress_eq[2]


def test_mean_stress_compressive(steel):

    model = GoodmanCorrection(steel)
    mean_stress = np.array([-200.0, -250.0, -300.0])
    stress_amplitude = np.array([100.0, 100.0, 100.0])
    stress_eq = model.equivalent_stress(stress_amplitude, mean_stress)
    assert stress_eq[0] > stress_eq[1] > stress_eq[2]


def test_mean_stress_exceed_ultimate(steel):

    model = GoodmanCorrection(steel)
    mean_stress = np.array([700.0])
    stress_amplitude = np.array([100.00])

    with pytest.raises(InvalidStressError):
        model.equivalent_stress(stress_amplitude, mean_stress)


def test_exact_goodman_value(steel):

    model = GoodmanCorrection(steel)
    stress_eq = model.equivalent_stress(100.0, 200.0)
    assert np.isclose(stress_eq, 100.0 / (1 - 200.0 / 650.0))


def test_invalid_ultimate_strength():

    with pytest.raises(InvalidMaterialError):
        Material(
            name="Test",
            elastic_modulus=210000,
            poissons_ratio=0.3,
            yield_strength=550,
            ultimate_strength=0,
            fatigue_strength_coefficient=1000,
            fatigue_strength_exponent=-0.1,
        )
