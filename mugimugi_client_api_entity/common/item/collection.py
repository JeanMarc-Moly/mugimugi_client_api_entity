from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar, Literal

from xsdata.formats.dataclass.models.elements import XmlType

from ...enum import ElementPrefix, ItemType
from .abstract import ItemCommon


@dataclass(eq=False)
class CollectionCommon(ItemCommon):
    class Type(Enum):
        TYPE = ItemType.COLLECTION

    PREFIX: ClassVar[Literal[ElementPrefix.COLLECTION]] = ElementPrefix.COLLECTION

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
