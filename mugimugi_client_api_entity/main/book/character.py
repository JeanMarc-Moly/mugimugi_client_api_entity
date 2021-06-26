from abc import ABC
from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...common import CharacterCommon, Named
from ...enum import Ratio


@dataclass
class LinkedPartialCharacter(CharacterCommon, ABC):
    ratio: Ratio = field(
        metadata=dict(
            name="FRQ",
            type=XmlType.ATTRIBUTE,
            required=True,
            min_inclusive=0,
            max_inclusive=5,
        ),
    )


@dataclass
class Character(Named, LinkedPartialCharacter):
    ...
