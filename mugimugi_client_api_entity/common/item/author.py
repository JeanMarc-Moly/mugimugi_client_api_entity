from dataclasses import dataclass, field
from enum import Enum

from xsdata.formats.dataclass.models.elements import XmlType

from ...enum import ElementPrefix, ItemType
from .abstract import ItemCommon


@dataclass
class AuthorCommon(ItemCommon):
    class Type(Enum):
        TYPE = ItemType.AUTHOR

    _id: str = field(
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.AUTHOR.value}\d+",
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
