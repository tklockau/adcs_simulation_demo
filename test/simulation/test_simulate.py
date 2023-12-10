import pytest
import os
import sys
from pathlib import Path
import numpy as np

sys.path.insert(1, str(Path(__file__).parent.parent.parent))
from simulation.simulate import simulate
from simulation.satellite.satellite import Satellite
from simulation.satellite.components.reaction_wheel import ReactionWheel

def test_simulate_attitude():
    satellite = Satellite(
        attitude=5,
        angular_velocity=0,
        rotational_inertia=4,
        reaction_wheel=ReactionWheel(
            angular_velocity=0,
            rotational_inertia=1
        )
    )

    time = np.linspace(0, 60, 100_000)

    reaction_wheel_angular_velocity = -1/120 * time ** 2 + 0

    satellite_states = simulate(satellite, reaction_wheel_angular_velocity, time)

    calculated_attitudes = np.array(list(map(Satellite.attitude, satellite_states)))
    ground_truth_angular_velocity = - (satellite.reaction_wheel.rotational_inertia / satellite.rotational_inertia) * reaction_wheel_angular_velocity
    ground_truth = satellite.attitude + np.cumsum(ground_truth_angular_velocity) * np.gradient(time)

    assert np.nanmax(np.abs((ground_truth - calculated_attitudes) / np.max(ground_truth))) < 0.001

if __name__ == "__main__":
    os.system("clear")
    pytest.main([__file__, "--disable-pytest-warnings", "--cache-clear"])