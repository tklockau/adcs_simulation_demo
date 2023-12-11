from dataclasses import dataclass

from ..utils.make_fields_classvariables import make_fields_classvariables
from ..utils.quantities import Angle, AngularVelocity

@dataclass
class State:
    attitude: Angle
    angular_velocity: AngularVelocity

make_fields_classvariables(State, ".state")