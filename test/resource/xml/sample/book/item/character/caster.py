from mugimugi_client_api_entity.enum import Ratio
from mugimugi_client_api_entity.enum.gender import Sex
from mugimugi_client_api_entity.main.book import Character

from .......configuration import SAMPLE
from ....abstract import Sample


class BookCharacterCaster(Sample):
    file_path = SAMPLE / "book/item/character/caster.xml"
    type = Character
    object = Character(
        english_name="Caster",
        japanese_name="キャスター",
        romaji_name="キャスター",
        other_names=[],
        mugimugi_id="H3465",
        version=13,
        objects_count=125,
        sex=Sex.FEMALE,
        age="",
        ratio=Ratio.NOT_SET,
    )
