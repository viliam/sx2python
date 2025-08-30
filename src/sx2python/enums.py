from enum import Enum, auto

class SxErrorTypes(Enum):
    EMPTY_WORD = auto()
    EXPECTED_INT = auto()

class ExpType(Enum):
    VOID = auto()
    INT = auto()
    BOOL = auto()
    COMPARISON = auto()
    UNKNOWN = auto()

