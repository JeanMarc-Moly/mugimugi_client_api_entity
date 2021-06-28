from dataclasses import dataclass

from ....common import CharacterCommon
from .abstract import SubItem


@dataclass(eq=False)
class SubCharacter(SubItem, CharacterCommon):
    ...
