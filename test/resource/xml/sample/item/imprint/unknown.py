from typing import get_type_hints

from mugimugi_client_api_entity import Imprint
from mugimugi_client_api_entity.enum import ItemType

from ......configuration import SAMPLE
from ...abstract import Sample


class ImprintUnknown(Sample[Imprint]):
    file_path = SAMPLE / "item/imprint/unknown.xml"
    object = Imprint(
        english_name="Unknown",
        japanese_name="不詳",
        katakana_name="",
        other_names=[],
        _id="I1",
        version=1,
        objects_count=15083,
        _type_validator=Imprint.Type.TYPE,
    )
