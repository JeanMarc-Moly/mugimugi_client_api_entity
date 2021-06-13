from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...main import Genre
from ...root import ValidRoot


@dataclass
class SearchGenre(ValidRoot[Genre]):
    elements: list[Genre] = field(
        default_factory=list,
        metadata=dict(name=Genre.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )
