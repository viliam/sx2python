from enum import Enum, auto
from typing import Optional, FrozenSet

class SxErrorType(Enum):
    UNCORRECTED_END_OF_EXPRESSION = auto()
    END_OF_FILE = auto()
    EXPECTED_INT = auto()
    UNEXPECTED_PREFIX = auto()
    EXPECTED_DATA_TYPE = auto()
    EXPECTED_BRACKET = auto()
    EXPECTED_OPERATOR = auto()
    EXPECTED_TOKEN = auto()
    UNKNOWN_OPERATOR = auto()

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
    AND = "and"
    OR = "or"

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
    DIVIDE = "/"
    MODULO = "%"
    FLOOR_DIVISION = "//"
    EXPONENT = "**"

    # BOOL
    AND = "and"
    OR = "or"
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

class SymbolGroupEnum(Enum):
    OP_ARITH = frozenset({SymbolEnum.PLUS, SymbolEnum.MINUS, SymbolEnum.TIMES,
                          SymbolEnum.MODULO, SymbolEnum.DIVIDE, SymbolEnum.FLOOR_DIVISION,
                          SymbolEnum.EXPONENT})
    OP_BOOL = frozenset({SymbolEnum.AND, SymbolEnum.AND_STRONG, SymbolEnum.OR, SymbolEnum.OR_STRONG})
    OP_COMPARISON = frozenset({SymbolEnum.SMALLER, SymbolEnum.SMALLER_EQUAL, SymbolEnum.GREATER,
                               SymbolEnum.GRATER_EQUAL, SymbolEnum.EQUAL, SymbolEnum.UNEQUAL})
    OP_EXP = frozenset({SymbolEnum.PLUS, SymbolEnum.MINUS, SymbolEnum.TIMES,
                        SymbolEnum.MODULO, SymbolEnum.DIVIDE, SymbolEnum.FLOOR_DIVISION,
                        SymbolEnum.EXPONENT, SymbolEnum.AND,
                        SymbolEnum.AND_STRONG, SymbolEnum.OR, SymbolEnum.OR_STRONG,
                        SymbolEnum.SMALLER, SymbolEnum.SMALLER_EQUAL, SymbolEnum.GREATER,
                        SymbolEnum.GRATER_EQUAL, SymbolEnum.EQUAL, SymbolEnum.UNEQUAL})
    OP_ASSIGNMENT = frozenset({SymbolEnum.ASSIGN})
    COMMAS = frozenset({SymbolEnum.COMMA,SymbolEnum.SEMICOLON,SymbolEnum.DOT})
    BRACKET = frozenset({SymbolEnum.BRACKET_NORM_OPEN, SymbolEnum.BRACKET_NORM_CLOSE,
                         SymbolEnum.PARENTHESIS_BLOCK_OPEN, SymbolEnum.PARENTHESIS_BLOCK_CLOSE})


    def __init__(self, members: FrozenSet[SymbolEnum]):
        self._members: FrozenSet[SymbolEnum] = members

    def contains(self, word: SymbolEnum) -> bool:
        return word in self.members

    def is_prefix(self, a: str) -> bool:
        for sy in self.members:
            if sy.is_prefix(a):
                return True
        return False

    @property
    def members(self) -> FrozenSet[SymbolEnum]:
        return self._members