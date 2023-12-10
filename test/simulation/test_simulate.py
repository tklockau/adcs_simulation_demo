import pytest
import os
import sys
from pathlib import Path
import numpy as np

sys.path.insert(1, str(Path(__file__).parent.parent.parent))
from simulation.simulate import simulate
from simulation.satellite.satellite import Satellite
from simulation.satellite.components.reaction_wheel import ReactionWheel
from simulation.math.integrate import integrate
from simulation.utils.quantities import Angle, AngularVelocity, MomentOfInertia

def test_simulate_attitude():
    satellite = Satellite(
        attitude=Angle(5),
        angular_velocity=AngularVelocity(0),
        moment_of_inertia=MomentOfInertia(4),
        reaction_wheel=ReactionWheel(
            angular_velocity=AngularVelocity(0),
            moment_of_inertia=MomentOfInertia(1)
        )
    )

    time = np.linspace(0, 60, 100_000)

    reaction_wheel_angular_velocity = -1/120 * time ** 2 + 0

    satellite_states = simulate(satellite, reaction_wheel_angular_velocity, time)

    calculated_attitudes = np.array(list(map(Satellite.attitude, satellite_states)))
    ground_truth_angular_velocity = - (satellite.reaction_wheel.moment_of_inertia / satellite.moment_of_inertia) * reaction_wheel_angular_velocity
    ground_truth = satellite.attitude + integrate(time, ground_truth_angular_velocity)

    assert np.nanmax(np.abs((ground_truth - calculated_attitudes) / np.max(ground_truth))) < 0.001

if __name__ == "__main__":
    os.system("clear")
    pytest.main([__file__, "--disable-pytest-warnings", "--cache-clear"])