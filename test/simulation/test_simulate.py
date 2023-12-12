import pytest
import os
import sys
from pathlib import Path
import numpy as np

sys.path.insert(1, str(Path(__file__).parent.parent.parent))
from simulation.simulate import simulate
from simulation.satellite.satellite import Satellite
from simulation.satellite.satellite_state import SatelliteState
from simulation.satellite.satellite_properties import SatelliteProperties
from simulation.satellite.components.reaction_wheel import ReactionWheel
from simulation.utils.quantities import Angle, AngularVelocity, MomentOfInertia, Vector, Time
from simulation.utils.math import integrate, compare_with_tolerance, extract_values

def test_simulate_attitude():
    satellite = Satellite(
        state=SatelliteState(
            attitude=Angle(5),
            angular_velocity=AngularVelocity(0),
        ),
        properties=SatelliteProperties(MomentOfInertia(4)),
        reaction_wheel=ReactionWheel(
            angular_velocity=AngularVelocity(0),
            moment_of_inertia=MomentOfInertia(1)
        )
    )

    time = Vector[Time].linear(0, 60)
    reaction_wheel_angular_velocity = -1/120 * (time ** 2)

    satellite_states = simulate(satellite, reaction_wheel_angular_velocity, time)

    calculated_attitudes = extract_values(satellite_states, SatelliteState.attitude)

    ground_truth_angular_velocity = - (satellite.reaction_wheel.moment_of_inertia / satellite.properties.moment_of_inertia) * reaction_wheel_angular_velocity
    ground_truth = satellite.state.attitude + integrate(time, ground_truth_angular_velocity)

    assert compare_with_tolerance(ground_truth, calculated_attitudes, 0.001)

if __name__ == "__main__":
    os.system("clear")
    pytest.main([__file__, "--disable-pytest-warnings", "--cache-clear", "-v"])