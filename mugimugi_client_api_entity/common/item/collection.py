from dataclasses import dataclass, field
from enum import Enum

from xsdata.formats.dataclass.models.elements import XmlType

from ...enum import ElementPrefix, ItemType
from .abstract import ItemCommon


@dataclass
class CollectionCommon(ItemCommon):
    class Type(Enum):
        TYPE = ItemType.COLLECTION

    _id: str = field(
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.COLLECTION.value}\d+",
        ),
    )
    _type_validator: Type = field(
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )
