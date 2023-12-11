from dataclasses import dataclass
import numpy as np

from .satellite_state import SatelliteState
from .satellite_properties import SatelliteProperties
from .components.reaction_wheel import ReactionWheel
from ..utils.make_fields_classvariables import make_fields_classvariables
from ..utils.quantities import AngularVelocity, MomentOfInertia, Time

@dataclass
class Satellite:
    state: SatelliteState
    properties: SatelliteProperties
    reaction_wheel: ReactionWheel

    def propagate(self, reaction_wheel_angular_velocity: AngularVelocity, time_difference: Time) -> "Satellite":

        new_angular_velocity = - (self.reaction_wheel.moment_of_inertia / self.properties.moment_of_inertia) * reaction_wheel_angular_velocity
        new_attitude = self.state.attitude + new_angular_velocity * time_difference

        return Satellite(
            state=SatelliteState(
                attitude=new_attitude,
                angular_velocity=new_angular_velocity
            ),
            properties=self.properties,
            reaction_wheel=ReactionWheel(
                angular_velocity=reaction_wheel_angular_velocity,
                moment_of_inertia=self.reaction_wheel.moment_of_inertia
            )
        )

make_fields_classvariables(Satellite)
    