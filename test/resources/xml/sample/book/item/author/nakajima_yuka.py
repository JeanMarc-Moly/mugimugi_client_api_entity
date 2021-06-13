from mugimugi_client_api_entity.main.book import Author
from mugimugi_client_api_entity.enum.position import Position

from .......configuration import SAMPLE
from ....abstract import Sample


class BookAuthorNakajimaYuka(Sample):
    file_path = SAMPLE / "book/item/author/nakajima_yuka.xml"
    type = Author
    object = Author(
        english_name="Nakajima Yuka",
        japanese_name="なかじまゆか",
        romaji_name="ナカジマユカ",
        other_names=["かなじまゆか", "Digital Lover"],
        mugimugi_id="A924",
        version=15,
        objects_count=485,
        parent=0,
        position=Position.MAIN,
    )
