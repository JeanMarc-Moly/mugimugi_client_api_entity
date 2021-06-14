from mugimugi_client_api_entity.main.book import Collection

from ......configuration import SAMPLE
from ...abstract import Sample


class BookCollectionDLAction(Sample):
    file_path = SAMPLE / "book/item/collection/dlaction.xml"
    type = Collection
    object = Collection(
        english_name="D.L. action",
        japanese_name="D.L. action",
        romaji_name="",
        other_names=[],
        mugimugi_id="O25",
        version=1,
        objects_count=109,
    )
