"""
The classes in this module do not have any function reason to be used, but should be used as type 
hints and initiators to signify what exactly a variable means.
"""
import typing as t
import numpy as np

class Vector(np.ndarray):

    @classmethod
    def __getitem__(cls, *args, **kwargs):
        return cls
    
    @classmethod
    def linear(cls, start: float, stop: float, resolution: int=100_000) -> "Vector":
        """
        Create a linear vector of floating point numbers between a given start and stop with a 
        resolution.

        Parameters
        ----------
        start : float
            start value of the vector
        stop : float
            end value of the vector (inclusive)
        resolution : int, optional
            number of vector elements (default is 100 000)
        """
        return np.linspace(start, stop, resolution)
    
    def zeros(cls, number_of_elements: int) -> "Vector":
        """
        Create a vector with only zeros.
        """
        return np.zeros(number_of_elements)

class Angle(float):
    """An angle in radiants. Inherits from float."""
    pass

class AngularVelocity(float):
    """Angular velocity in rad/s. Inherits from float."""

class MomentOfInertia(float):
    """Moment of inertia in kg * m ** 2. Inherits from float."""

class Time(float):
    """Time in seconds. Inherits from float."""
