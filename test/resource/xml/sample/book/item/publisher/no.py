from typing import get_type_hints

from mugimugi_client_api_entity.main.book import Publisher

from .......configuration import SAMPLE
from ....abstract import Sample


class BookPublisherNo(Sample[Publisher]):
    file_path = SAMPLE / "book/item/publisher/no.xml"
    object = Publisher(
        english_name="No Publisher",
        japanese_name="出版社なし",
        katakana_name="",
        other_names=[],
        _id="L3",
        version=2,
        objects_count=1492741,
        type=Publisher.Type.TYPE,
    )
