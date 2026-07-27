import pytest

from fatigue.exceptions import (
    FatigueError,
    InvalidMaterialError,
)


def test_exception_inheritance():
    assert issubclass(InvalidMaterialError, FatigueError)


def test_invalid_material_exceptions():
    with pytest.raises(InvalidMaterialError):
        raise InvalidMaterialError("Invalid material")
