from dataclasses import dataclass, field
from enum import Enum

from xsdata.formats.dataclass.models.elements import XmlType

from ...enum import ElementPrefix, ItemType
from ...util.converter import Date
from .abstract import ItemCommon


@dataclass
class ConventionCommon(ItemCommon):
    class Type(Enum):
        TYPE = ItemType.CONVENTION

    _id: str = field(
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.CONVENTION.value}\d+",
        ),
    )
    _type_validator: Type = field(
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )
    date_start: Date = field(
        metadata=dict(name="DATE_START", type=XmlType.ELEMENT, required=True),
    )
    date_end: Date = field(
        metadata=dict(name="DATE_END", type=XmlType.ELEMENT, required=True),
    )
