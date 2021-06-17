from dataclasses import dataclass

from ...common import CollectionCommon
from .abstract import Item


@dataclass
class Collection(Item, CollectionCommon):
    ...
