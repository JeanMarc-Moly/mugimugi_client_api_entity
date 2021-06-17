from abc import ABC
from dataclasses import dataclass, field
from typing import Generic, Iterator, TypeVar

from xsdata.formats.dataclass.models.elements import XmlType

from ...common import ItemCommon, Named
from ..abstract_linker import AbstractLinker
from .sub import SubItem

LI = TypeVar("LI", bound=SubItem)


class LinkableItem(ItemCommon, Generic[LI]):
    _links: AbstractLinker

    @property
    def items(self) -> Iterator[LI]:
        for e in self._links.items:
            yield e


@dataclass
class Item(Named, ItemCommon, ABC):
    @dataclass
    class Linker(AbstractLinker, ABC):
        ...

    # Useless but present.
    _: Linker = field(
        default_factory=Linker,
        metadata=dict(name=Linker.Meta.name, type=XmlType.ELEMENT),
    )
