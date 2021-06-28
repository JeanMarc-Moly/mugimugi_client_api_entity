from dataclasses import dataclass

from ...common import CollectionCommon
from .abstract import Item


@dataclass(eq=False)
class Collection(Item, CollectionCommon):
    ...
