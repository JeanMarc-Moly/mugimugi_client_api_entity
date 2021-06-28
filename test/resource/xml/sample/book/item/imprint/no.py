from mugimugi_client_api_entity.main.book import Imprint

from .......configuration import SAMPLE
from ....abstract import Sample


class BookImprintNo(Sample[Imprint]):
    file_path = SAMPLE / "book/item/imprint/no.xml"
    object = Imprint(
        english_name="No Imprint",
        japanese_name="レーベルなし",
        katakana_name="",
        other_names=[],
        _id="I2",
        version=2,
        objects_count=848115,
        _type_validator=Imprint.Type.TYPE,
    )
