from abc import abstractmethod, ABC

from src.sx2python.common import SxError
from src.sx2python.position import Position
from src.sx2python.text import Text
from src.sx2python.enums import SymbolEnum, SxErrorType, SymbolGroupEnum
from typing import TypeVar, Optional, FrozenSet
from src.sx2python.parsers.parser import SxParser
from src.sx2python.words.symbol import Bracket, Operator

E = TypeVar('E', bound='Symbol')

class SymbolAbstractParser(SxParser[E], ABC):

    def _next_char_position(self, text: "Text"):
        return text.next_char_position()

    def read(self, text: Text) -> E:
        try:
            poz = self._next_char_position(text)
            s_symbol = self._take_symbol(text)
            e_symbol = SymbolEnum.make_symbol( s_symbol)
            return self.create(poz, e_symbol)
        except SxError as ex:
            raise SxError.create(ex.typ, text.position, text.line)

    @abstractmethod
    def get_symbols(self) -> FrozenSet[str]:
        pass

    @abstractmethod
    def create(self, position: Position, enum: Optional[SymbolEnum]) -> E:
        pass

    @abstractmethod
    def get_exception_type(self) -> SxErrorType:
        pass

    def _take_symbol(self, text: Text) -> str:
        s = text.take_end_of_line()
        # Sort symbols by length in descending order to find the longest match first.
        symbols = sorted(self.get_symbols(), key=len, reverse=True)

        for sym in symbols:
            if s.startswith(sym):
                text.position = text.position.add_x(len(sym))
                return sym

        raise SxError.create(self.get_exception_type(), text.position, text.line)


class BracketParser(SymbolAbstractParser[Bracket]):

    _instance = None

    def get_symbols(self) -> FrozenSet[SymbolEnum]:
        return SymbolGroupEnum.BRACKET.members

    def create(self, position: Position, enum: Optional[SymbolEnum]) -> E:
        if enum is None:
            raise SxError.create(self.get_exception_type(), position, "")
        return Bracket(position, enum)

    def get_exception_type(self) -> SxErrorType:
        return SxErrorType.EXPECTED_BRACKET


class OperatorExpressionParser(SymbolAbstractParser[Operator]):

    _instance = None


    def _next_char_position(self, text: "Text"):
        return text.next_char_position_in_expression()

    def get_symbols(self) -> FrozenSet[str]:
        return SymbolGroupEnum.OP_EXP.members

    def create(self, position: Position, enum: Optional[SymbolEnum]) -> E:
        return Operator(position, enum)

    def get_exception_type(self) -> SxErrorType:
        return SxErrorType.EXPECTED_OPERATOR