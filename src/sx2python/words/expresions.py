from abc import abstractmethod

from src.sx2python.enums import ExpType
from src.sx2python.words.word import WordABC, Word


class Expression(WordABC):

    @property
    @abstractmethod
    def exp_type(self) -> ExpType:
        pass

    # @abstractmethod
    # def visit(self, visitor):
    #     pass

class WordExpression(Expression):

    def __init__(self, name: Word):
        super().__init__(name.position)
        self._content = name.content

    @property
    def content(self) -> str:
        return self._content


class Variable(WordExpression):

    def __init__(self, name: Word):
        super().__init__(name)
        self._expType = ExpType.UNKNOWN

    @property
    def exp_type(self) -> ExpType:
        return self._expType


class DataType(WordExpression):

    def __init__(self, name: Word):
        super().__init__(name)
        self._expType = ExpType.VOID

    @property
    def exp_type(self) -> ExpType:
        return self._expType


class Integer(WordExpression):

    def __init__(self, integer: int, name: Word):
        super().__init__(name)
        self._integer = integer


    @property
    def integer(self) -> int:
        return self._integer

    @property
    def exp_type(self) -> ExpType:
        return ExpType.INT