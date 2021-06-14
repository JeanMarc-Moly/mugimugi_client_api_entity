from mugimugi_client_api_entity import Author
from mugimugi_client_api_entity.main.sub import SubContent

from ......configuration import SAMPLE
from ...abstract import Sample


class BookAuthorSekiyaAsami(Sample):
    file_path = SAMPLE / "item/author/sekiya_asami.xml"
    type = Author
    object = Author(
        mugimugi_id="A1484",
        english_name="Sekiya Asami",
        japanese_name="関谷あさみ",
        romaji_name="セキヤアサミ",
        version=14,
        objects_count=217,
        _links=Author.Linker(
            items=[
                SubContent(
                    mugimugi_id="K12",
                    english_name="Incest",
                    japanese_name="近親姦",
                    other_names=["近親相姦"],
                    version=5,
                    objects_count=13054,
                ),
                SubContent(
                    mugimugi_id="K15",
                    english_name="Loli",
                    japanese_name="ロリ",
                    other_names=["lolicon", "lolikon", "rorikon", "ロリコン"],
                    version=3,
                    objects_count=74960,
                ),
                SubContent(
                    mugimugi_id="K601",
                    english_name="School Girl",
                    japanese_name="女子生徒",
                    version=3,
                    objects_count=20327,
                ),
            ]
        ),
    )
