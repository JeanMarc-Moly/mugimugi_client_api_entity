from mugimugi_client_api_entity import Genre

from ......configuration import SAMPLE
from ...abstract import Sample


class GenreUnknown(Sample):
    file_path = SAMPLE / "item/genre/unknown.xml"
    type = Genre
    object = Genre(
        english_name="Unknown",
        japanese_name="不詳",
        romaji_name="",
        other_names=[],
        mugimugi_id="G1",
        version=2,
        objects_count=174,
    )
