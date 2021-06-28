from dataclasses import dataclass

from ...common import PublisherCommon
from .abstract import Item


@dataclass(eq=False)
class Publisher(Item, PublisherCommon):
    ...
