from typing import get_type_hints

from mugimugi_client_api_entity.enum import Ratio
from mugimugi_client_api_entity.main.book import Parody

from .......configuration import SAMPLE
from ....abstract import Sample


class BookParodyFateStayNight(Sample[Parody]):
    file_path = SAMPLE / "book/item/parody/fate_stay_night.xml"
    object = Parody(
        english_name="Fate/stay night",
        japanese_name="Fate/stay night",
        katakana_name="フェイトステイナイト",
        other_names=[],
        _id="P16",
        version=29,
        objects_count=5268,
        ratio=Ratio.NOT_SET,
        _type_validator=Parody.Type.TYPE,
    )
