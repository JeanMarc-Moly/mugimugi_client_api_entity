from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar, Literal

from xsdata.formats.dataclass.models.elements import XmlType

from ...enum import ElementPrefix, ItemType
from .abstract import ItemCommon


@dataclass(eq=False)
class CircleCommon(ItemCommon):
    class Type(Enum):
        TYPE = ItemType.CIRCLE

    PREFIX: ClassVar[Literal[ElementPrefix.CIRCLE]] = ElementPrefix.CIRCLE

    _id: str = field(
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{PREFIX.value}\d+",
        ),
    )
    _type_validator: Type = field(
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )
    parent: int = field(
        metadata=dict(
            name="PARENT", type=XmlType.ATTRIBUTE, required=True, min_inclusive=0
        ),
    )
