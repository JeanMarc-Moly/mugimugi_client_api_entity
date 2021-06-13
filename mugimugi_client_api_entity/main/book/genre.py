from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...common import GenreCommon
from ...enum import Ratio
from .abstract import LinkedPartialItem


@dataclass
class Genre(GenreCommon, LinkedPartialItem):
    ratio: Ratio = field(
        default=None,
        metadata=dict(
            name="FRQ",
            type=XmlType.ATTRIBUTE,
            required=True,
            min_inclusive=0,
            max_inclusive=5,
        ),
    )
