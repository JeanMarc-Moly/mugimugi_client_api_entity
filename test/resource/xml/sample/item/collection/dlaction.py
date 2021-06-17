from mugimugi_client_api_entity.main.book import Collection

from ......configuration import SAMPLE
from ...abstract import Sample


class BookCollectionDLAction(Sample[Collection]):
    file_path = SAMPLE / "book/item/collection/dlaction.xml"
    object = Collection(
        english_name="D.L. action",
        japanese_name="D.L. action",
        katakana_name="",
        other_names=[],
        _id="O25",
        version=1,
        objects_count=109,
        type=Collection.Type.TYPE,
    )
