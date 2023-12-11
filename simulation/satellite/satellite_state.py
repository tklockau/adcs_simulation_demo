from dataclasses import dataclass

from ..utils.make_fields_classvariables import make_fields_classvariables
from ..utils.quantities import Angle, AngularVelocity, Time
from .components.reaction_wheel import ReactionWheel
from .satellite_properties import SatelliteProperties

@dataclass
class SatelliteState:
    attitude: Angle
    angular_velocity: AngularVelocity

    def propagate(self, properties: SatelliteProperties, reaction_wheel: ReactionWheel, time_delta: Time) -> "SatelliteState":
        return SatelliteState(
            attitude=self._calc_attitude(properties, reaction_wheel, time_delta),
            angular_velocity=self._calc_angular_velocity(properties, reaction_wheel)
        )

    def _calc_attitude(self, properties: SatelliteProperties, reaction_wheel: ReactionWheel, time_delta: Time) -> Angle:
        angular_velocity = self._calc_angular_velocity(properties, reaction_wheel)
        return self.attitude + angular_velocity * time_delta

    def _calc_angular_velocity(self, properties: SatelliteProperties, reaction_wheel: ReactionWheel) -> AngularVelocity:
        moment_of_inertia_ratio = reaction_wheel.moment_of_inertia / properties.moment_of_inertia
        return - moment_of_inertia_ratio * reaction_wheel.angular_velocity

make_fields_classvariables(SatelliteState, ".state")