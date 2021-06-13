from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...main import Circle
from ...root import ValidRoot

@dataclass
class SearchCircle(ValidRoot[Circle]):
    elements: list[Circle] = field(
        default_factory=list,
        metadata=dict(name=Circle.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )
