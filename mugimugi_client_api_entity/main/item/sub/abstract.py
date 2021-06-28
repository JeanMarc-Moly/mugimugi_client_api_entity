from dataclasses import dataclass

from ....common import ItemCommon, Named


@dataclass(eq=False)
class SubItem(Named, ItemCommon):
    ...
