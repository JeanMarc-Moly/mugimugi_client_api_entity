from dataclasses import dataclass

from ...common import ImprintCommon
from .abstract import Item


@dataclass
class Imprint(Item, ImprintCommon):
    ...
