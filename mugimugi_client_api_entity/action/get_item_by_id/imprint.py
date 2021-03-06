from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...main import Imprint
from ...root import ValidRoot


@dataclass
class GetImprintById(ValidRoot[Imprint]):
    elements: list[Imprint] = field(
        default_factory=list,
        metadata=dict(name=Imprint.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )
