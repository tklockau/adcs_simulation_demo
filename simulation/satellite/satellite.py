from dataclasses import dataclass
import numpy as np

from .components.reaction_wheel import ReactionWheel
from ..utils.make_fields_classvariables import make_fields_classvariables
from ..utils.quantities import Angle, AngularVelocity, MomentOfInertia, Time

@dataclass
class Satellite:
    attitude: Angle
    angular_velocity: AngularVelocity
    moment_of_inertia: MomentOfInertia
    reaction_wheel: ReactionWheel

    def propagate(self, reaction_wheel_angular_velocity: AngularVelocity, time_difference: Time) -> "Satellite":

        new_angular_velocity = - (self.reaction_wheel.moment_of_inertia / self.moment_of_inertia) * reaction_wheel_angular_velocity
        new_attitude = self.attitude + new_angular_velocity * time_difference

        return Satellite(
            attitude=new_attitude,
            angular_velocity=new_angular_velocity,
            moment_of_inertia=self.moment_of_inertia,
            reaction_wheel=ReactionWheel(
                angular_velocity=reaction_wheel_angular_velocity,
                moment_of_inertia=self.reaction_wheel.moment_of_inertia
            )
        )

make_fields_classvariables(Satellite)
    