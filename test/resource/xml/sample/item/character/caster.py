from typing import get_type_hints

from mugimugi_client_api_entity.enum import Ratio, Sex
from mugimugi_client_api_entity.main.book import Character

from ......configuration import SAMPLE
from ...abstract import Sample


class BookCharacterCaster(Sample[Character]):
    file_path = SAMPLE / "book/item/character/caster.xml"
    object = Character(
        english_name="Caster",
        japanese_name="キャスター",
        katakana_name="キャスター",
        other_names=[],
        _id="H3465",
        version=13,
        objects_count=125,
        sex=Sex.FEMALE,
        age="",
        ratio=Ratio.NOT_SET,
        _type_validator=Character.Type.TYPE,
    )
