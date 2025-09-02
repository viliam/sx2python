from enum import Enum, auto
from typing import Optional, FrozenSet


class SxErrorType(Enum):
    EMPTY_WORD = auto()
    END_OF_FILE = auto()
    EXPECTED_INT = auto()
    UNEXPECTED_PREFIX = auto()
    EXPECTED_DATA_TYPE = auto()

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

    @staticmethod
    def is_word(value: str) -> bool:
        return value in ReservedWordEnum._value2member_map_

    def __str__(self) -> str:  # keep Java toString behavior
        return self.value


class ReservedWordGroupEnum(Enum):
    DATA_TYPE = frozenset({ReservedWordEnum.INT, ReservedWordEnum.BOOL})
    INSTRUCTION_WORD = frozenset({ReservedWordEnum.RETURN, ReservedWordEnum.IF})
    DATA_VALUE = frozenset({ReservedWordEnum.VOID, ReservedWordEnum.TRUE, ReservedWordEnum.FALSE})

    def __init__(self, members: FrozenSet[ReservedWordEnum]):
        self.members: FrozenSet[ReservedWordEnum] = members

    def contains(self, word: ReservedWordEnum) -> bool:
        return word in self.members



class SymbolEnum(str, Enum):
    # ARITM
    PLUS = "+"
    MINUS = "-"
    TIMES = "*"
    MODULO = "%"
    REST = "/"

    # BOOL
    AND = "&"
    OR = "|"
    AND_STRONG = "&&"
    OR_STRONG = "||"

    # COMPARISON
    SMALLER = "<"
    GREATER = ">"
    SMALLER_EQUAL = "<="
    GRATER_EQUAL = ">="
    EQUAL = "=="
    UNEQUAL = "!="

    ASSIGN = "="

    BRACKET_NORM_OPEN = "("
    BRACKET_NORM_CLOSE = ")"
    PARENTHESIS_BLOCK_OPEN = "{"
    PARENTHESIS_BLOCK_CLOSE = "}"

    COMMA = ","
    SEMICOLON = ";"
    DOT = ","

    @property
    def symbol(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.value

    @staticmethod
    def make_symbol(s: str) -> Optional["SymbolEnum"]:
        try:
            return SymbolEnum(s)
        except ValueError:
            return None

    def is_prefix(self, a: str) -> bool:
        if not a:
            return False
        return self.value[0] == a[0]