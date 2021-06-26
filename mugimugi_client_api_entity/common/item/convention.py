from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar, Literal

from xsdata.formats.dataclass.models.elements import XmlType

from ...enum import ElementPrefix, ItemType
from ...util.converter import Date
from .abstract import ItemCommon


@dataclass
class ConventionCommon(ItemCommon):
    class Type(Enum):
        TYPE = ItemType.CONVENTION

    PREFIX: ClassVar[Literal[ElementPrefix.CONVENTION]] = ElementPrefix.CONVENTION

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
    date_start: Date = field(
        metadata=dict(name="DATE_START", type=XmlType.ELEMENT, required=True),
    )
    date_end: Date = field(
        metadata=dict(name="DATE_END", type=XmlType.ELEMENT, required=True),
    )
