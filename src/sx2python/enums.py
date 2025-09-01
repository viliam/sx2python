from enum import Enum, auto
from typing import Optional


class SxErrorTypes(Enum):
    EMPTY_WORD = auto()
    END_OF_FILE = auto()
    EXPECTED_INT = auto()
    UNEXPECTED_PREFIX = auto()

class ExpType(Enum):
    VOID = auto()
    INT = auto()
    BOOL = auto()
    COMPARISON = auto()
    UNKNOWN = auto()


class ReservedWordEnum(str, Enum):
    INT = "int"
    BOOL = "bool"
    RETURN = "return"
    IF = "if"
    VOID = "void"
    TRUE = "true"
    FALSE = "false"

    def matches(self, s: str) -> bool:
        return self.value == s

    @property
    def symbol(self) -> str:
        return self.value

    @staticmethod
    def make_symbol(reserved_word: str) -> Optional["ReservedWordEnum"]:
        try:
            return ReservedWordEnum(reserved_word)
        except ValueError:
            return None


    def __str__(self) -> str:  # keep Java toString behavior
        return self.value


# class ReservedWordGroup(Enum):
#     DATA_TYPE = (ReservedWordEnum.INT, ReservedWordEnum.BOOL)
#     INSTRUCTION_WORD = (ReservedWordEnum.RETURN, ReservedWordEnum.IF)
#     DATA_VALUE = (ReservedWordEnum.VOID, ReservedWordEnum.TRUE, ReservedWordEnum.FALSE)
#
#     def __init__(self, members: Tuple[ReservedWordEnum, ...]):
#         self.members: Tuple[ReservedWordEnum, ...] = members
#
#     def contains(self, word: ReservedWordEnum) -> bool:
#         return word in self.members
