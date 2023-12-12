import numpy as np

from .satellite.satellite import Satellite
from .utils.quantities import AngularVelocity, Time, Vector

def simulate(
    satellite: Satellite, 
    reaction_wheel_angular_velocity: Vector[AngularVelocity],
    time: Vector[Time],
) -> np.ndarray:
    """
    Simulate a satellites rotation based the reaction wheel velocity.
    """

    satellite_states = [satellite]

    for i, dt in enumerate(np.gradient(time)[1:]):
        satellite_states.append(satellite_states[-1].propagate(reaction_wheel_angular_velocity[i], dt))

    return satellite_states