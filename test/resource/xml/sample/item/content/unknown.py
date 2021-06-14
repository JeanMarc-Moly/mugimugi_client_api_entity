from mugimugi_client_api_entity import Content

from ......configuration import SAMPLE
from ...abstract import Sample


class ContentUnknown(Sample):
    file_path = SAMPLE / "item/content/unknown.xml"
    type = Content
    object = Content(
        english_name="Unknown",
        japanese_name="不詳",
        romaji_name="",
        other_names=[],
        mugimugi_id="K1",
        version=1,
        objects_count=1590669,
    )
