from mugimugi_client_api_entity import Genre
from mugimugi_client_api_entity.enum import ItemType

from ......configuration import SAMPLE
from ...abstract import Sample


class GenreUnknown(Sample[Genre]):
    file_path = SAMPLE / "item/genre/unknown.xml"
    object = Genre(
        english_name="Unknown",
        japanese_name="不詳",
        katakana_name="",
        other_names=[],
        _id="G1",
        version=2,
        objects_count=174,
        _type_validator=Genre.Type.TYPE,
    )
