from mugimugi_client_api_entity import Imprint

from ......configuration import SAMPLE
from ...abstract import Sample


class ImprintUnknown(Sample):
    file_path = SAMPLE / "item/imprint/unknown.xml"
    type = Imprint
    object = Imprint(
        english_name="Unknown",
        japanese_name="不詳",
        romaji_name="",
        other_names=[],
        mugimugi_id="I1",
        version=1,
        objects_count=15083,
    )
