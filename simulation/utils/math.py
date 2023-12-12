import numpy as np

from .quantities import Vector
from ..satellite.satellite import Satellite

def integrate(x: Vector, y: Vector) -> Vector:
    return np.cumsum(y) * np.gradient(x)

def compare_with_tolerance(x1: Vector, x2: Vector, tolerance: float=0.001) -> bool:
    """Return wether the difference between two vectors is within a certain tolerance percentage."""
    return np.nanmax(np.abs((x1 - x2) / np.max(x1))) < tolerance

def extract_values(satellites: Vector[Satellite], function) -> Vector:
    return np.array(list(map(function, satellites)))
