from dataclasses import dataclass, field
from typing import Iterator, Union

from xsdata.formats.dataclass.models.elements import XmlType

from ...common import BookCommon, Named
from ..abstract_linker import AbstractLinker
from ..item.abstract import Item
from .author import Author
from .character import Character
from .circle import Circle
from .collection import Collection
from .content import Content
from .convention import Convention
from .genre import Genre
from .imprint import Imprint
from .parody import Parody
from .publisher import Publisher
from .type import Type

LI = Union[
    Author,
    Character,
    Circle,
    Collection,
    Content,
    Convention,
    Genre,
    Imprint,
    Parody,
    Publisher,
    Type,
]


@dataclass
class Book(Named, BookCommon):
    @dataclass
    class Linker:
        items: list[LI] = field(
            default_factory=list,
            metadata=dict(name=Item.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
        )

    _links: Linker = field(
        default_factory=Linker,
        metadata=dict(name=AbstractLinker.Meta.name, type=XmlType.ELEMENT),
    )

    @property
    def items(self) -> Iterator[LI]:
        for e in self._links.items:
            yield e
