from dataclasses import dataclass

from ....common import ContentCommon
from .abstract import SubItem


@dataclass(eq=False)
class SubContent(SubItem, ContentCommon):
    ...
