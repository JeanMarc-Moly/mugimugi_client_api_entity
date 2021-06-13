from mugimugi_client_api_entity import Publisher

from ......configuration import SAMPLE
from ...abstract import Sample


class PublisherUnknown(Sample):
    file_path = SAMPLE / "item/publisher/unknown.xml"
    type = Publisher
    object = Publisher(
        english_name="Unknown",
        japanese_name="不詳",
        romaji_name="",
        other_names=[],
        mugimugi_id="L1",
        version=1,
        objects_count=70513,
    )
