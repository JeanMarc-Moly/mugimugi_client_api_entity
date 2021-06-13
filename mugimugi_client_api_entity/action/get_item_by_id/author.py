from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...main import Author
from ...root import ValidRoot


@dataclass
class GetAuthorById(ValidRoot[Author]):
    elements: list[Author] = field(
        default_factory=list,
        metadata=dict(name=Author.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )
