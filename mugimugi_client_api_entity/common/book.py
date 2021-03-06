from dataclasses import dataclass, field
from typing import ClassVar, Literal

from xsdata.formats.dataclass.models.elements import XmlType

from ..enum import ElementNode, ElementPrefix, Language
from ..util.converter import Date
from .element import Element


@dataclass(eq=False)
class BookCommon(Element):
    class Meta:
        name = ElementNode.BOOK.value

    PREFIX: ClassVar[Literal[ElementPrefix.BOOK]] = ElementPrefix.BOOK

    _id: str = field(
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{PREFIX.value}\d+",
        ),
    )
    version: int = field(
        metadata=dict(
            name="VER", type=XmlType.ATTRIBUTE, required=True, min_inclusive=0
        ),
    )
    release_date: Date = field(
        metadata=dict(
            name="DATE_RELEASED", type=XmlType.ELEMENT, required=True, format="%Y-%m-%d"
        ),
    )
    isbn: str = field(
        metadata=dict(name="DATA_ISBN", type=XmlType.ELEMENT, required=True),
    )
    pages_count: int = field(
        metadata=dict(name="DATA_PAGES", type=XmlType.ELEMENT, required=True),
    )
    is_adult: bool = field(
        metadata=dict(name="DATA_AGE", type=XmlType.ELEMENT, required=True),
    )
    is_anthology: bool = field(
        metadata=dict(name="DATA_ANTHOLOGY", type=XmlType.ELEMENT, required=True),
    )
    is_copybook: bool = field(
        metadata=dict(name="DATA_COPYSHI", type=XmlType.ELEMENT, required=True),
    )
    magazine: bool = field(
        metadata=dict(name="DATA_MAGAZINE", type=XmlType.ELEMENT, required=True),
    )
    language: Language = field(
        metadata=dict(name="DATA_LANGUAGE", type=XmlType.ELEMENT, required=True),
    )
    info: str = field(
        metadata=dict(name="DATA_INFO", type=XmlType.ELEMENT, required=True),
    )
