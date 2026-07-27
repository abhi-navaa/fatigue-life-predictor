import pytest

from fatigue.exceptions import InvalidMaterialError
from fatigue.material import Material


def test_invalid_yield_strength():

    with pytest.raises(InvalidMaterialError):

        Material(
            name="Steel",
            elastic_modulus=210000,
            poissons_ratio=0.30,
            yield_strength=700,
            ultimate_strength=600,
        )


def test_material_creation():
    steel = Material(
        name="AISI 1045",
        elastic_modulus=210000,
        poissons_ratio=0.30,
        yield_strength=530,
        ultimate_strength=625,
    )
    assert steel.name == "AISI 1045"
    assert steel.elastic_modulus == 210000
    assert steel.poissons_ratio == 0.30
