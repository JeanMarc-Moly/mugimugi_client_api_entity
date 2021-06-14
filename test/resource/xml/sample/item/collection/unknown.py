from mugimugi_client_api_entity import Collection

from ......configuration import SAMPLE
from ...abstract import Sample


class CollectionUnknown(Sample):
    file_path = SAMPLE / "item/collection/unknown.xml"
    type = Collection
    object = Collection(
        english_name="UNKNOWN",
        japanese_name="不詳",
        romaji_name="",
        other_names=[],
        mugimugi_id="O1",
        version=2,
        objects_count=37,
    )
