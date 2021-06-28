from mugimugi_client_api_entity.enum import Position
from mugimugi_client_api_entity.main.book import Circle

from .......configuration import SAMPLE
from ....abstract import Sample


class BookCircleDigitalLover(Sample[Circle]):
    file_path = SAMPLE / "book/item/circle/digital_lover.xml"
    object = Circle(
        english_name="Digital Lover",
        japanese_name="Digital Lover",
        katakana_name="デジタルラバー",
        other_names=[],
        _id="C180",
        version=17,
        objects_count=421,
        parent=0,
        position=Position.MAIN,
        _type_validator=Circle.Type.TYPE,
    )
