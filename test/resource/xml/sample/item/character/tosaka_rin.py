from typing import get_type_hints

from mugimugi_client_api_entity.enum import Ratio, Sex
from mugimugi_client_api_entity.main.book import Character

from ......configuration import SAMPLE
from ...abstract import Sample


class BookCharacterTosakaRin(Sample[Character]):
    file_path = SAMPLE / "book/item/character/tosaka_rin.xml"
    object = Character(
        english_name="Tōsaka Rin",
        japanese_name="遠坂凛",
        katakana_name="トオサカリン",
        other_names=["Tosaka Rin", "Tousaka Rin", "Tohsaka Rin"],
        _id="H211",
        version=19,
        objects_count=979,
        sex=Sex.FEMALE,
        age="",
        ratio=Ratio.NOT_SET,
        _type_validator=Character.Type.TYPE,
    )
