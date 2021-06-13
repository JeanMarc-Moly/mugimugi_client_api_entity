from mugimugi_client_api_entity.enum.position import Position
from mugimugi_client_api_entity.main.book import Circle

from .......configuration import SAMPLE
from ....abstract import Sample


class BookCircleDigitalLover(Sample):
    file_path = SAMPLE / "book/item/circle/digital_lover.xml"
    type = Circle
    object = Circle(
        english_name="Digital Lover",
        japanese_name="Digital Lover",
        romaji_name="デジタルラバー",
        other_names=[],
        mugimugi_id="C180",
        version=17,
        objects_count=421,
        parent=0,
        position=Position.MAIN,
    )
