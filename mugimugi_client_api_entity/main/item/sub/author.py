from dataclasses import dataclass

from ....common import AuthorCommon
from .abstract import SubItem


@dataclass(eq=False)
class SubAuthor(SubItem, AuthorCommon):
    ...
