from dataclasses import dataclass

from ...common import ContentCommon
from .abstract import Item


@dataclass(eq=False)
class Content(Item, ContentCommon):
    ...
