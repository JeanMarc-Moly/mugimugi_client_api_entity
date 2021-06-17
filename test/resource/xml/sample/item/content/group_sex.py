from mugimugi_client_api_entity.enum import Ratio
from mugimugi_client_api_entity.main.book import Content

from ......configuration import SAMPLE
from ...abstract import Sample


class BookContentGroupSex(Sample[Content]):
    file_path = SAMPLE / "book/item/content/group_sex.xml"
    object = Content(
        english_name="Group Sex",
        japanese_name="グループセックス",
        katakana_name="",
        other_names=["乱交"],
        _id="K66",
        version=4,
        objects_count=39263,
        ratio=Ratio.NOT_SET,
        _type_validator=Content.Type.TYPE,
    )
