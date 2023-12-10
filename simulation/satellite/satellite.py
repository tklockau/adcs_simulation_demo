from dataclasses import dataclass
import numpy as np

from .components.reaction_wheel import ReactionWheel
from ..utils.make_fields_classvariables import make_fields_classvariables

@dataclass
class Satellite:
    attitude: float
    angular_velocity: float
    rotational_inertia: float
    reaction_wheel: ReactionWheel

    def propagate(self, reaction_wheel_angular_velocity, time_difference) -> "Satellite":

        new_angular_velocity = - (self.reaction_wheel.rotational_inertia / self.rotational_inertia) * reaction_wheel_angular_velocity
        new_attitude = self.attitude + new_angular_velocity * time_difference

        return Satellite(
            attitude=new_attitude,
            angular_velocity=new_angular_velocity,
            rotational_inertia=self.rotational_inertia,
            reaction_wheel=ReactionWheel(
                angular_velocity=reaction_wheel_angular_velocity,
                rotational_inertia=self.reaction_wheel.rotational_inertia
            )
        )

make_fields_classvariables(Satellite)
    