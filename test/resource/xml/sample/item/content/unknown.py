from mugimugi_client_api_entity import Content
from mugimugi_client_api_entity.enum import ItemType

from ......configuration import SAMPLE
from ...abstract import Sample


class ContentUnknown(Sample[Content]):
    file_path = SAMPLE / "item/content/unknown.xml"
    object = Content(
        english_name="Unknown",
        japanese_name="不詳",
        katakana_name="",
        other_names=[],
        _id="K1",
        version=1,
        objects_count=1590669,
        _type_validator=Content.Type.TYPE,
    )
