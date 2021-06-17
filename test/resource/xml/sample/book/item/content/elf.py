from typing import get_type_hints

from mugimugi_client_api_entity.enum import Ratio
from mugimugi_client_api_entity.main.book import Content

from .......configuration import SAMPLE
from ....abstract import Sample


class BookContentElf(Sample[Content]):
    file_path = SAMPLE / "book/item/content/elf.xml"
    object = Content(
        english_name="Elf",
        japanese_name="エルフ",
        katakana_name="",
        other_names=[],
        _id="K39",
        version=1,
        objects_count=2803,
        ratio=Ratio.NOT_SET,
        _type_validator=Content.Type.TYPE,
    )
