from typing import get_type_hints

from mugimugi_client_api_entity.enum import Position
from mugimugi_client_api_entity.main.book import Author

from .......configuration import SAMPLE
from ....abstract import Sample


class BookAuthorNakajimaYuka(Sample[Author]):
    file_path = SAMPLE / "book/item/author/nakajima_yuka.xml"
    object = Author(
        english_name="Nakajima Yuka",
        japanese_name="なかじまゆか",
        katakana_name="ナカジマユカ",
        other_names=["かなじまゆか", "Digital Lover"],
        _id="A924",
        version=15,
        objects_count=485,
        parent=0,
        position=Position.MAIN,
        type=Author.Type.TYPE,
    )
