from dataclasses import dataclass
import numpy as np

from ..utils.quantities import Vector
from ..satellite.satellite import Satellite

@dataclass
class Graph:
    label: str
    y_values: Vector

    _instance_counter = 0
    _COLOR_PALETTE = ("blue", "green", "red")

    @classmethod
    def from_satellites(cls, label: str, satellites: Vector[Satellite], plot_method) -> "Graph":
        return Graph(
            label,
            np.array(list(map(plot_method, satellites)))
        )

    def __post_init__(self):
        self.color = self._COLOR_PALETTE[self._instance_counter % len(self._COLOR_PALETTE)]
        Graph._instance_counter += 1