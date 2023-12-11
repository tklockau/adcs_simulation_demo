from dataclasses import dataclass

from ..utils.make_fields_classvariables import make_fields_classvariables
from ..utils.quantities import MomentOfInertia

@dataclass
class SatelliteProperties:
    moment_of_inertia: MomentOfInertia

make_fields_classvariables(SatelliteProperties, ".properties")