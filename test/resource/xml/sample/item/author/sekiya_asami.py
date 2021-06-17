from typing import get_type_hints

from mugimugi_client_api_entity import Author
from mugimugi_client_api_entity.enum import ItemType
from mugimugi_client_api_entity.main.item.sub import SubContent

from ......configuration import SAMPLE
from ...abstract import Sample


class BookAuthorSekiyaAsami(Sample[Author]):
    file_path = SAMPLE / "item/author/sekiya_asami.xml"
    object = Author(
        _id="A1484",
        english_name="Sekiya Asami",
        japanese_name="関谷あさみ",
        katakana_name="セキヤアサミ",
        version=14,
        parent=0,
        objects_count=217,
        type=Author.Type.TYPE,
        _links=Author.Linker(
            items=[
                SubContent(
                    _id="K12",
                    english_name="Incest",
                    japanese_name="近親姦",
                    katakana_name="",
                    other_names=["近親相姦"],
                    version=5,
                    objects_count=13054,
                    type=SubContent.Type.TYPE,
                ),
                SubContent(
                    _id="K15",
                    english_name="Loli",
                    japanese_name="ロリ",
                    katakana_name="",
                    other_names=["lolicon", "lolikon", "rorikon", "ロリコン"],
                    version=3,
                    objects_count=74960,
                    type=SubContent.Type.TYPE,
                ),
                SubContent(
                    _id="K601",
                    english_name="School Girl",
                    japanese_name="女子生徒",
                    katakana_name="",
                    version=3,
                    objects_count=20327,
                    type=SubContent.Type.TYPE,
                ),
            ]
        ),
    )
