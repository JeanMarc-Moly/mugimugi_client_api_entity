from dataclasses import dataclass, field
from typing import Iterator, Union

from xsdata.formats.dataclass.models.elements import XmlType

from mugimugi_client_api_entity.common.named import Named

from ...common import CircleCommon
from ..abstract_linker import AbstractLinker
from .abstract import LinkableItem
from .sub import SubAuthor, SubContent

LI = Union[SubAuthor, SubContent]


@dataclass(eq=False)
class Circle(Named, CircleCommon, LinkableItem[LI]):
    @dataclass
    class Linker(AbstractLinker):
        items: list[LI] = field(
            default_factory=list,
            metadata=dict(
                name=LinkableItem.Meta.name, type=XmlType.ELEMENT, min_occurs=0
            ),
        )

    _links: Linker = field(
        default_factory=Linker,
        metadata=dict(
            name=AbstractLinker.Meta.name, type=XmlType.ELEMENT, min_occurs=0
        ),
    )

    @property
    def contents(self) -> Iterator[SubContent]:
        for e in self._links.items:
            if isinstance(e, SubContent):
                yield e

    @property
    def authors(self) -> Iterator[SubAuthor]:
        for e in self._links.items:
            if isinstance(e, SubAuthor):
                yield e
