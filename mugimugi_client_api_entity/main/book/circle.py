from abc import ABC
from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...common import CircleCommon, Named
from ...enum import Position


@dataclass
class LinkedPartialCircle(CircleCommon, ABC):
    position: Position = field(
        metadata=dict(
            name="FRQ",
            type=XmlType.ATTRIBUTE,
            required=True,
            min_inclusive=0,
            max_inclusive=2,
        ),
    )


@dataclass
class Circle(Named, LinkedPartialCircle):
    ...
