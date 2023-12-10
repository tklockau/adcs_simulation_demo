from dataclasses import dataclass
import numpy as np

@dataclass
class ReactionWheel:
    angular_velocity: np.ndarray
    rotational_inertia: float