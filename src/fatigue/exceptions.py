"""
custom exceptions for fatigue package
"""

from __future__ import annotations


class FatigueError(Exception):
    """Base exception for the fatigue package"""


class InvalidMaterialError(FatigueError):
    """Raised when material properties are invalid"""


class InvalidStressError(FatigueError):
    """Rasied when an invalid stress state is supplied"""


class InvalodLoadError(FatigueError):
    """Raised when an invalid load definition is supplied"""


class ModelNotApplicableError(FatigueError):
    """Raised when the fatigue model is used outside its valid range"""


class InvalidCycleError(FatigueError):
    """Raised when invalid cycles are supplied"""
