from dataclasses import dataclass

from ....common import ParodyCommon
from .abstract import SubItem


@dataclass(eq=False)
class SubParody(SubItem, ParodyCommon):
    ...
