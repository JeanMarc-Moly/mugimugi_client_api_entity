from mugimugi_client_api_entity.main.book import Type

from ......configuration import SAMPLE
from ...abstract import Sample


class BookTypeDoujinshi(Sample[Type]):
    file_path = SAMPLE / "book/item/type/doujinshi.xml"
    object = Type(
        english_name="Doujinshi",
        japanese_name="同人誌",
        katakana_name="",
        other_names=[],
        _id="T1",
        version=1,
        objects_count=1329929,
        _type_validator=Type.Type.TYPE,
    )
