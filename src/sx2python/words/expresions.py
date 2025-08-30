from abc import abstractmethod

from src.sx2python.enums import ExpType
from src.sx2python.text import Position
from src.sx2python.words.word import WordABC


class Expression(WordABC):

    @property
    @abstractmethod
    def exp_type(self) -> ExpType:
        pass

    # @abstractmethod
    # def visit(self, visitor):
    #     pass


class Integer(Expression):

    def __init__(self, integer: int, position: Position):
        super().__init__(position)
        self._integer = integer

    @property
    def exp_type(self) -> ExpType:
        return ExpType.INT

    @property
    def integer(self) -> int:
        return self._integer
