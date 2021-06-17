from dataclasses import dataclass, field
from typing import Iterator

from xsdata.formats.dataclass.models.elements import XmlType

from mugimugi_client_api_entity.common.named import Named

from ...common import AuthorCommon
from ..abstract_linker import AbstractLinker
from .abstract import LinkableItem
from .sub import SubContent


@dataclass
class Author(Named, AuthorCommon, LinkableItem[SubContent]):
    @dataclass
    class Linker(AbstractLinker):
        items: list[SubContent] = field(
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
        yield from self._links.items
