import numpy as np

from ..quantities.vector import Vector

def integrate(x: Vector, y: Vector) -> Vector:
    return np.cumsum(y) * np.gradient(x)