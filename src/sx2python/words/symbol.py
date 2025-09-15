from src.sx2python.common import SxError
from src.sx2python.words.word import WordABC
from src.sx2python.enums import SymbolEnum, ExpType, SxErrorType

from src.sx2python.text import Position

class Symbol(WordABC) :

    def __init__(self, position: Position, symbol_enum: SymbolEnum):
        super().__init__(position)
        self._symbol_enum = symbol_enum

    @property
    def content(self) -> str:
        return self._symbol_enum.symbol


class Bracket(Symbol):

    def __init__(self, position: Position, symbol_enum: SymbolEnum):
        super().__init__(position, symbol_enum)

class Operator(Symbol):

    def __init__(self, position: Position, symbol_enum: SymbolEnum):
        super().__init__(position, symbol_enum)

    def exp_type(self) -> ExpType:
        match self._symbol_enum:
            case SymbolEnum.PLUS | SymbolEnum.MINUS | SymbolEnum.TIMES | SymbolEnum.MODULO \
                 | SymbolEnum.DIVIDE  | SymbolEnum.FLOOR_DIVISION | SymbolEnum.EXPONENT:
                return ExpType.INT
            case SymbolEnum.AND | SymbolEnum.OR | SymbolEnum.AND_STRONG | SymbolEnum.OR_STRONG:
                return ExpType.BOOL
            case SymbolEnum.SMALLER | SymbolEnum.GREATER | SymbolEnum.SMALLER_EQUAL \
                 | SymbolEnum.GRATER_EQUAL | SymbolEnum.EQUAL | SymbolEnum.UNEQUAL:
                return ExpType.COMPARISON
            case SymbolEnum.ASSIGN:
                return ExpType.UNKNOWN
        raise SxError.create_with_message(SxErrorType.UNKNOWN_OPERATOR, self._symbol_enum.__str__(), self._position, "")
