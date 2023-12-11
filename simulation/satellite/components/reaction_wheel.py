from dataclasses import dataclass
import numpy as np

from ...utils.make_fields_classvariables import make_fields_classvariables
from ...utils.quantities import AngularVelocity, MomentOfInertia

@dataclass
class ReactionWheel:
    """
    Container of attributes of a reaction wheel used to orient a satellite in space.
    See https://en.wikipedia.org/wiki/Reaction_wheel.
    """

    angular_velocity: AngularVelocity
    """
    Rotational speed of the reaction wheel.
    See https://en.wikipedia.org/wiki/Angular_velocity.
    """
    
    moment_of_inertia: MomentOfInertia
    """
    Describes the opposition of a body to a change in rotation. 
    See https://en.wikipedia.org/wiki/Moment_of_inertia.
    """

make_fields_classvariables(ReactionWheel)