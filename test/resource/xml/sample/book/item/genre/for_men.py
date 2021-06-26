from typing import get_type_hints

from mugimugi_client_api_entity.enum import Ratio
from mugimugi_client_api_entity.main.book import Genre

from .......configuration import SAMPLE
from ....abstract import Sample


class BookGenreForMen(Sample[Genre]):
    file_path = SAMPLE / "book/item/genre/for_men.xml"
    object = Genre(
        english_name="For men",
        japanese_name="男性向け",
        katakana_name="",
        other_names=[],
        _id="G227",
        version=1,
        objects_count=346049,
        ratio=Ratio.NOT_SET,
        _type_validator=Genre.Type.TYPE,
    )
