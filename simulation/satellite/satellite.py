from dataclasses import dataclass

from .satellite_state import SatelliteState
from .satellite_properties import SatelliteProperties
from .components.reaction_wheel import ReactionWheel
from ..utils.make_fields_classvariables import make_fields_classvariables
from ..utils.quantities import AngularVelocity, Time

@dataclass
class Satellite:
    state: SatelliteState
    properties: SatelliteProperties
    reaction_wheel: ReactionWheel

    def propagate(self, reaction_wheel_angular_velocity: AngularVelocity, time_delta: Time) -> "Satellite":

        reaction_wheel = ReactionWheel(
            reaction_wheel_angular_velocity, 
            self.reaction_wheel.moment_of_inertia
        )

        return Satellite(
            state=self.state.propagate(
                self.properties,
                reaction_wheel=reaction_wheel,
                time_delta=time_delta
            ),
            properties=self.properties,
            reaction_wheel=reaction_wheel,
        )

make_fields_classvariables(Satellite)
    