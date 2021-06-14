from mugimugi_client_api_entity.main.book import Publisher

from ......configuration import SAMPLE
from ...abstract import Sample


class BookPublisherNo(Sample):
    file_path = SAMPLE / "book/item/publisher/no.xml"
    type = Publisher
    object = Publisher(
        english_name="No Publisher",
        japanese_name="出版社なし",
        romaji_name="",
        other_names=[],
        mugimugi_id="L3",
        version=2,
        objects_count=1492741,
    )
