from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar, Literal

from xsdata.formats.dataclass.models.elements import XmlType

from ...enum import ElementPrefix, ItemType, Sex
from .abstract import ItemCommon


@dataclass(eq=False)
class CharacterCommon(ItemCommon):
    class Type(Enum):
        TYPE = ItemType.CHARACTER

    PREFIX: ClassVar[Literal[ElementPrefix.CHARACTER]] = ElementPrefix.CHARACTER

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
    sex: Sex = field(
        metadata=dict(
            name="DATA_SEX",
            type=XmlType.ELEMENT,
            required=True,
            min_inclusive=0,
            max_inclusive=4,
        ),
    )
    age: str = field(
        metadata=dict(name="DATA_AGE", type=XmlType.ELEMENT, required=True),
    )
