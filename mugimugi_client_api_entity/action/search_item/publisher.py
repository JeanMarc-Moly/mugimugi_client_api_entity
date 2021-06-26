from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...main import Publisher
from ...root import ValidRoot


@dataclass
class SearchPublisher(ValidRoot[Publisher]):
    elements: list[Publisher] = field(
        default_factory=list,
        metadata=dict(name=Publisher.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )
