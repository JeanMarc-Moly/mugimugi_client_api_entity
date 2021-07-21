from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...main import Book, MatchedBook
from .abstract import ValidRoot


@dataclass
class BookRoot(ValidRoot[Book]):
    elements: list[Book] = field(
        default_factory=list,
        metadata=dict(name=Book.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )


@dataclass
class MatchedBookRoot(ValidRoot[MatchedBook]):
    elements: list[MatchedBook] = field(
        default_factory=list,
        metadata=dict(name=MatchedBook.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )
