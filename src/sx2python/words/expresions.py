from abc import abstractmethod

from src.sx2python.enums import ExpType
from src.sx2python.text import Position
from src.sx2python.words.word import WordABC, Word


class Expression(WordABC):

    @property
    @abstractmethod
    def exp_type(self) -> ExpType:
        pass

    # @abstractmethod
    # def visit(self, visitor):
    #     pass


class Variable(Expression):

    def __init__(self, name: Word):
        super().__init__(name.position)
        self._name = name
        self._expType = ExpType.UNKNOWN

    @property
    def exp_type(self) -> ExpType:
        return self._expType



class Integer(Expression):

    def __init__(self, integer: int, position: Position):
        super().__init__(position)
        self._integer = integer

    @property
    def integer(self) -> int:
        return self._integer

    @property
    def exp_type(self) -> ExpType:
        return ExpType.INT