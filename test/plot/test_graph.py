import pytest
import os
import sys
from pathlib import Path
import numpy as np

sys.path.insert(1, str(Path(__file__).parent.parent.parent))
from simulation.plot.graph import Graph
from simulation.utils.quantities import Vector, Angle
from simulation.satellite.satellite import Satellite, SatelliteState

def create_satellite_with_attitude(attitude: Angle) -> Satellite:
    return Satellite(
        state=SatelliteState(
            attitude=attitude,
            angular_velocity=0
        ),
        properties=None,
        reaction_wheel=None
    )

def test_color():
    y_values = np.zeros(5)

    g0 = Graph("", y_values)
    g1 = Graph("", y_values)
    g2 = Graph.from_satellites("", [], lambda x: x)
    g3 = Graph("", y_values)

    assert g0.color != g1.color != g2.color
    assert g0.color == g3.color

def test_from_satellite():
    satellites = [
        create_satellite_with_attitude(1),
        create_satellite_with_attitude(2),
        create_satellite_with_attitude(3)
    ]

    graph = Graph.from_satellites("", satellites, SatelliteState.attitude)

    assert np.all(graph.y_values == Vector[Angle].linear(1, 3, 3))
    

if __name__ == "__main__":
    os.system("clear")
    pytest.main([__file__, "--disable-pytest-warnings", "--cache-clear", "-v"])