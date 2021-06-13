from dataclasses import dataclass, field
from enum import IntEnum

from xsdata.formats.dataclass.models.elements import XmlType

from ...enum import ElementNode
from .api_key_not_found import ApiKeyNotFound
from .id_not_found import IdNotFound
from .image_not_found import ImageNotFound
from .image_not_received import ImageNotReceived
from .image_not_uploaded import ImageNotUploaded
from .image_server_down import ImageServerDown
from .image_too_big import ImageTooBig
from .invalid_score import InvalidScore
from .no_query_left import NoQueryLeft
from .object_not_found import ObjectNotFound
from .unknown import Unknown
from .user_not_found import UserNotFound


@dataclass
class ErrorCommon:
    class Meta:
        name = ElementNode.ERROR.value

    class Error(IntEnum):
        UNKNOWN = 0
        NO_QUERY_LEFT = 2
        INVALID_SCORE = 11
        API_KEY_NOT_FOUND = 1
        ID_NOT_FOUND = 9
        OBJECT_NOT_FOUND = 10
        USER_NOT_FOUND = 8
        IMAGE_NOT_FOUND = 5
        IMAGE_NOT_RECEIVED = 7
        IMAGE_NOT_UPLOADED = 3
        IMAGE_SEARCH_SERVER_DOWN = 6
        IMAGE_TOO_BIG = 4

    CONVERTER = {
        Error.UNKNOWN: Unknown,
        Error.NO_QUERY_LEFT: NoQueryLeft,
        Error.INVALID_SCORE: InvalidScore,
        Error.API_KEY_NOT_FOUND: ApiKeyNotFound,
        Error.ID_NOT_FOUND: IdNotFound,
        Error.OBJECT_NOT_FOUND: ObjectNotFound,
        Error.USER_NOT_FOUND: UserNotFound,
        Error.IMAGE_NOT_FOUND: ImageNotFound,
        Error.IMAGE_NOT_RECEIVED: ImageNotReceived,
        Error.IMAGE_NOT_UPLOADED: ImageNotUploaded,
        Error.IMAGE_SEARCH_SERVER_DOWN: ImageServerDown,
        Error.IMAGE_TOO_BIG: ImageTooBig,
    }

    id: int = field(
        metadata=dict(name="code", type="Attribute", required=True, min_inclusive=0)
    )
    description: str = field(metadata=dict(name="EXACT", type=XmlType.ELEMENT))
    declaration: str = field(metadata=dict(name="TYPE", type=XmlType.ELEMENT))
    exception: Error = field(metadata=dict(name="CODE", type=XmlType.ELEMENT))

    def blow(self):
        raise self.CONVERTER[self.exception](self.description)
