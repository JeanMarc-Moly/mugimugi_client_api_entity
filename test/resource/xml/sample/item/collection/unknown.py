from mugimugi_client_api_entity import Collection
from mugimugi_client_api_entity.enum import ItemType

from ......configuration import SAMPLE
from ...abstract import Sample


class CollectionUnknown(Sample[Collection]):
    file_path = SAMPLE / "item/collection/unknown.xml"
    object = Collection(
        english_name="UNKNOWN",
        japanese_name="不詳",
        katakana_name="",
        other_names=[],
        _id="O1",
        version=2,
        objects_count=37,
        _type_validator=Collection.Type.TYPE,
    )
