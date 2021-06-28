from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...common import Named, PublisherCommon


@dataclass(eq=False)
class Publisher(Named, PublisherCommon):
    # FRQ present but useless
    _: int = field(
        init=False, default=0, metadata=dict(name="FRQ", type=XmlType.ATTRIBUTE)
    )
