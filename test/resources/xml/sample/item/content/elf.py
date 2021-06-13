from mugimugi_client_api_entity.main.book import Content
from mugimugi_client_api_entity.enum import Ratio

from ......configuration import SAMPLE
from ...abstract import Sample


class BookContentElf(Sample):
    file_path = SAMPLE / "book/item/content/elf.xml"
    type = Content
    object = Content(
        english_name="Elf",
        japanese_name="エルフ",
        romaji_name="",
        other_names=[],
        mugimugi_id="K39",
        version=1,
        objects_count=2803,
        ratio=Ratio.NOT_SET,
    )
