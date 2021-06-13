from dataclasses import dataclass, field
from typing import Generic, Iterator, TypeVar

from xsdata.formats.dataclass.models.elements import XmlType

from ..common import ItemCommon
from .abstract_linker import AbstractLinker
from .sub import SubItem

LI = TypeVar("LI", bound=SubItem)


class LinkableItem(ItemCommon, Generic[LI]):
    _links: AbstractLinker

    @property
    def items(self) -> Iterator[LI]:
        for e in self._links.items:
            yield e


@dataclass
class Item(ItemCommon):
    @dataclass
    class Linker(AbstractLinker):
        ...

    # Useless but present.
    _: Linker = field(
        default_factory=dict,
        metadata=dict(name=Linker.Meta.name, type=XmlType.ELEMENT),
    )
