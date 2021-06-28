from mugimugi_client_api_entity import Publisher
from mugimugi_client_api_entity.enum import ItemType

from ......configuration import SAMPLE
from ...abstract import Sample


class PublisherUnknown(Sample[Publisher]):
    file_path = SAMPLE / "item/publisher/unknown.xml"
    object = Publisher(
        english_name="Unknown",
        japanese_name="不詳",
        katakana_name="",
        other_names=[],
        _id="L1",
        version=1,
        objects_count=70513,
        _type_validator=Publisher.Type.TYPE,
    )
