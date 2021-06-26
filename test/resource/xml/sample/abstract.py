from pathlib import Path
from typing import Generic, TypeVar

from mugimugi_client_api_entity.common import Element

E = TypeVar("E", bound=Element)


class Sample(Generic[E]):
    file_path: Path
    object: E
