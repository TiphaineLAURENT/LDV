from enum import IntEnum, unique

@unique
class STATUS_CODE(IntEnum):
    OK = 200
    UNAUTHORIZED = 401
    NOT_FOUND = 404
    REDIRECTED = 302
    FORBIDDEN = 403
