from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...enum import Ratio

from ...common import ContentCommon
from .abstract import LinkedPartialItem


@dataclass
class Content(ContentCommon, LinkedPartialItem):
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
