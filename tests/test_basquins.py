import numpy as np
import pytest

from fatigue.material import Material
from fatigue.models.basquin import BasquinModel


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


def test_life_positive(steel):

    model = BasquinModel(steel)
    assert model.life(300) > 0


def test_allowable_stress_positive(steel):

    model = BasquinModel(steel)
    assert model.allowable_stress(1e6) > 0


def test_lower_stress_increase_life(steel):

    model = BasquinModel(steel)
    high = model.life(350)
    low = model.life(250)
    assert low > high


def test_round_trip(steel):

    model = BasquinModel(steel)
    stress = np.array([200.0, 250.0, 300.0])
    life = model.life(stress)
    recovered = model.allowable_stress(life)
    assert recovered == pytest.approx(stress, rel=1e-10)


def test_vectorized_life(steel):

    model = BasquinModel(steel)
    stress = np.array([200.0, 250.0, 300.0])
    life = model.life(stress)
    assert life.shape == stress.shape
    assert life[0] > life[1] > life[2]
