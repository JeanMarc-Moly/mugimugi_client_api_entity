from __future__ import annotations
from abc import ABC
from dataclasses import dataclass, field
from typing import ClassVar
from functools import cached_property

from xsdata.formats.dataclass.models.elements import XmlType

from ..enum import ElementPrefix


@dataclass
class Element(ABC):

    PREFIX: ClassVar[ElementPrefix]

    _id: str = field(
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"[{''.join(ElementPrefix.values())}]\d+",
        ),
    )

    @cached_property
    def number(self):
        return int(self._id[1:])

    @cached_property
    def prefix(self):
        return ElementPrefix(self._id[0])

    def __hash__(self) -> int:
        return hash((self.prefix, self.number))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Element):
            return False
        return (self.prefix, self.number) == (other.prefix, other.number)
