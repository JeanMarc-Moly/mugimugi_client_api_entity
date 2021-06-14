from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...common import AuthorCommon
from ...enum import Position
from .abstract import LinkedPartialItem


@dataclass
class Author(AuthorCommon, LinkedPartialItem):
    position: Position = field(
        default=None,
        metadata=dict(
            name="FRQ",
            type=XmlType.ATTRIBUTE,
            required=True,
            min_inclusive=0,
            max_inclusive=2,
        ),
    )
