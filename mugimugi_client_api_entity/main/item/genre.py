from dataclasses import dataclass

from ...common import GenreCommon
from .abstract import Item


@dataclass(eq=False)
class Genre(Item, GenreCommon):
    ...
