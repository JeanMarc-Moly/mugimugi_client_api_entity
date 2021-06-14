from dataclasses import dataclass, field
from typing import Iterator, Union

from xsdata.formats.dataclass.models.elements import XmlType

from ..common import ConventionCommon
from .abstract_item import Item, LinkableItem
from .abstract_linker import AbstractLinker
from .sub import SubCharacter, SubContent, SubParody

LI = Union[SubContent, SubParody, SubCharacter]


@dataclass
class Convention(ConventionCommon, LinkableItem[LI]):
    @dataclass
    class Linker(AbstractLinker):
        items: list[LI] = field(
            default_factory=list,
            metadata=dict(name=Item.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
        )

    _links: Linker = field(
        default_factory=Linker,
        metadata=dict(name=AbstractLinker.Meta.name, type=XmlType.ELEMENT),
    )

    @property
    def contents(self) -> Iterator[SubContent]:
        for e in self._links.items:
            if isinstance(e, SubContent):
                yield e

    @property
    def parodies(self) -> Iterator[SubParody]:
        for e in self._links.items:
            if isinstance(e, SubParody):
                yield e

    @property
    def characters(self) -> Iterator[SubCharacter]:
        for e in self._links.items:
            if isinstance(e, SubCharacter):
                yield e
