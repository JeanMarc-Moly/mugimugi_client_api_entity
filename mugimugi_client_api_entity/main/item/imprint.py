from dataclasses import dataclass

from ...common import ImprintCommon
from .abstract import Item


@dataclass(eq=False)
class Imprint(Item, ImprintCommon):
    ...
