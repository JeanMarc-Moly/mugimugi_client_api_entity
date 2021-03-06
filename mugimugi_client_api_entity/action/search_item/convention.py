from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...main import Convention
from ...root import ValidRoot


@dataclass
class SearchConvention(ValidRoot[Convention]):
    elements: list[Convention] = field(
        default_factory=list,
        metadata=dict(name=Convention.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )
