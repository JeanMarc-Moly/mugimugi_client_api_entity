from dataclasses import dataclass

from ...common import PublisherCommon
from .abstract import Item


@dataclass
class Publisher(Item, PublisherCommon):
    ...
