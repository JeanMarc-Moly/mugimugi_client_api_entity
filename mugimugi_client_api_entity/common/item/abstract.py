from abc import ABC
from dataclasses import dataclass, field
from enum import Enum

from xsdata.formats.dataclass.models.elements import XmlType

from ...enum import ElementNode, ItemType
from ..element import Element


@dataclass
class ItemCommon(Element, ABC):
    class Meta:
        name = ElementNode.ITEM.value

    version: int = field(
        metadata=dict(
            name="VER", type=XmlType.ATTRIBUTE, required=True, min_inclusive=1
        )
    )
    objects_count: int = field(
        metadata=dict(
            name="OBJECTS", type=XmlType.ELEMENT, required=True, min_inclusive=1
        )
    )
