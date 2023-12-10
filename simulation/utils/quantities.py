"""
The classes in this module do not have any function reason to be used, but should be used as type 
hints and initiators to signify what exactly a variable means.
"""
import numpy as np

class Vector(np.ndarray):
    pass

class Angle(float):
    """An angle in radiants. Inherits from float."""
    pass

class AngularVelocity(float):
    """Angular velocity in rad/s. Inherits from float."""

class MomentOfInertia(float):
    """Moment of inertia in kg * m ** 2. Inherits from float."""

class Time(float):
    """Time in seconds. Inherits from float."""
