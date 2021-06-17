from typing import get_type_hints

from mugimugi_client_api_entity.enum import Ratio
from mugimugi_client_api_entity.main.book import Content

from .......configuration import SAMPLE
from ....abstract import Sample


class BookContentFemdom(Sample[Content]):
    file_path = SAMPLE / "book/item/content/femdom.xml"
    object = Content(
        english_name="Domination (Femdom)",
        japanese_name="女性支配・女王様・ドミナ",
        katakana_name="",
        other_names=[],
        _id="K48",
        version=2,
        objects_count=7083,
        ratio=Ratio.NOT_SET,
        _type_validator=Content.Type.TYPE,
    )
