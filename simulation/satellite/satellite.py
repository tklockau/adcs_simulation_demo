from dataclasses import dataclass

from .satellite_state import SatelliteState
from .satellite_properties import SatelliteProperties
from .components.reaction_wheel import ReactionWheel
from ..utils.make_fields_classvariables import make_fields_classvariables
from ..utils.quantities import AngularVelocity, Time

@dataclass
class Satellite:
    """
    Object representing all important attributes of our satellite. Can store any configuration 
    needed to model it (like MOVE-II, MOVE-III).
    """

    state: SatelliteState
    """
    Storage of satellite attributes, that change over time (like attitude).
    """

    properties: SatelliteProperties
    """
    Storage of permanent satellite attributes (like mass or moment of inertia).
    """

    reaction_wheel: ReactionWheel
    """
    One examplary active component of the satellite used to control attitude.
    """

    def propagate(self, reaction_wheel_angular_velocity: AngularVelocity, time_delta: Time) -> "Satellite":
        """
        Advance the satellite state by a given time delta and return the result.
        """

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

move_2b = Satellite(
    state=SatelliteState(
        attitude=0,
        angular_velocity=0
    ),
    properties=SatelliteProperties(
        moment_of_inertia=4
    ),
    reaction_wheel=ReactionWheel(
        moment_of_inertia=1,
        angular_velocity=0
    )
)
    