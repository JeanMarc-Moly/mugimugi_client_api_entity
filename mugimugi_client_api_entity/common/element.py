from abc import ABC
from dataclasses import dataclass, field
from typing import ClassVar

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

    @property
    def number(self):
        return int(self._id[1:])

    @property
    def prefix(self):
        return ElementPrefix(self._id[0])
