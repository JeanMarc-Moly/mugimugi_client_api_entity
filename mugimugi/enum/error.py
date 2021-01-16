from enum import IntEnum


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