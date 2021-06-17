from abc import ABC
from dataclasses import dataclass, field
from typing import Iterator

from xsdata.formats.dataclass.models.elements import XmlType


@dataclass
class Named(ABC):
    english_name: str = field(
        metadata=dict(name="NAME_EN", type=XmlType.ELEMENT, required=True)
    )
    japanese_name: str = field(
        metadata=dict(name="NAME_JP", type=XmlType.ELEMENT, required=True)
    )
    katakana_name: str = field(
        metadata=dict(name="NAME_R", type=XmlType.ELEMENT, required=True)
    )
    other_names: list[str] = field(
        default_factory=list,
        metadata=dict(name="NAME_ALT", type=XmlType.ELEMENT, min_occurs=0),
    )

    @property
    def names(self) -> Iterator[str]:
        if name := self.japanese_name:
            yield name
        if name := self.katakana_name:
            yield name
        if name := self.english_name:
            yield name
        for name in self.other_names:
            if name:
                yield name
