from dataclasses import dataclass

from ..utils.make_fields_classvariables import make_fields_classvariables
from ..utils.quantities import MomentOfInertia

@dataclass
class SatelliteProperties:
    """
    Storage of permanent satellite attributes.
    """

    moment_of_inertia: MomentOfInertia
    """
    Describes the opposition of a body to a change in rotation. 
    See https://en.wikipedia.org/wiki/Moment_of_inertia.
    """

make_fields_classvariables(SatelliteProperties, ".properties")