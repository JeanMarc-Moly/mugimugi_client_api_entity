from mugimugi_client_api_entity.main.book import Imprint

from .......configuration import SAMPLE
from ....abstract import Sample


class BookImprintNo(Sample):
    file_path = SAMPLE / "book/item/imprint/no.xml"
    type = Imprint
    object = Imprint(
        english_name="No Imprint",
        japanese_name="レーベルなし",
        romaji_name="",
        other_names=[],
        mugimugi_id="I2",
        version=2,
        objects_count=848115,
    )
