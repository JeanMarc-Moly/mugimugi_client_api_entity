from abc import ABC

from ..enum import ElementNode


class AbstractLinker(ABC):
    class Meta:
        name = ElementNode.LINK.value

    items: list
