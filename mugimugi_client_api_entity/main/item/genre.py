from dataclasses import dataclass

from ...common import GenreCommon
from .abstract import Item


@dataclass
class Genre(Item, GenreCommon):
    ...
