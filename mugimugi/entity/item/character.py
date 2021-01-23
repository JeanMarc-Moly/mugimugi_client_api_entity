from dataclasses import dataclass, field
from enum import Enum
from typing import Iterator

from ...enum import Ratio, Sex
from ..abstract import Element
from ..root import ValidRoot, XmlType
from .abstract import (
    AbstractLinker,
    ElementPrefix,
    Item,
    ItemType,
    LinkableItem,
    LinkedItem,
    LinkedPartialItem,
)
from .content import LinkedContent


@dataclass
class Linker(AbstractLinker[LinkedContent]):
    items: list[LinkedContent] = field(
        default_factory=list,
        metadata=dict(name=Item.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )


@dataclass
class AbstractCharacter(Element):
    class Type(Enum):
        TYPE = ItemType.CHARACTER

    _id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.CHARACTER.value}\d+",
        ),
    )
    # Used as discriminator
    _type: Type = field(
        default=Type.TYPE,
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )
    prefix: ElementPrefix = ElementPrefix.CHARACTER
    type: ItemType = ItemType.CHARACTER
    sex: Sex = field(
        default=None,
        metadata=dict(
            name="DATA_SEX",
            type=XmlType.ELEMENT,
            required=True,
            min_inclusive=0,
            max_inclusive=4,
        ),
    )
    age: str = field(
        default=None,
        metadata=dict(name="DATA_AGE", type=XmlType.ELEMENT, required=True),
    )


@dataclass
class Character(AbstractCharacter, LinkableItem[LinkedContent]):
    _links: Linker = field(
        default=None, metadata=dict(name="LINKS", type=XmlType.ELEMENT, min_occurs=0)
    )

    @property
    def contents(self) -> Iterator[LinkedContent]:
        yield from self._links.items


@dataclass
class CharacterRoot(ValidRoot[Character]):
    elements: list[Character] = field(
        default_factory=list,
        metadata=dict(name=Character.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )


@dataclass
class LinkedCharacter(AbstractCharacter, LinkedItem):
    ...


@dataclass
class LinkedPartialCharacter(AbstractCharacter, LinkedPartialItem):
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
