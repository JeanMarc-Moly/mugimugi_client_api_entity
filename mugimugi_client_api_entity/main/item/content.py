from dataclasses import dataclass

from ...common import ContentCommon
from .abstract import Item


@dataclass
class Content(Item, ContentCommon):
    ...
