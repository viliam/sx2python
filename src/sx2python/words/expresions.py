from abc import abstractmethod, ABC

from src.sx2python.enums import ExpType
from src.sx2python.words.symbol import Bracket, Operator
from src.sx2python.words.word import WordABC, Word


class ExpressionABC(WordABC):

    @property
    @abstractmethod
    def exp_type(self) -> ExpType:
        pass

    # @abstractmethod
    # def visit(self, visitor):
    #     pass

class WordExpression(ExpressionABC, ABC):

    def __init__(self, word: Word):
        super().__init__(word.position)
        self._content = word.content

    @property
    def content(self) -> str:
        return self._content


class Variable(WordExpression):

    def __init__(self, word: Word):
        super().__init__(word)
        self._expType = ExpType.UNKNOWN

    @property
    def exp_type(self) -> ExpType:
        return self._expType


class DataType(WordExpression):

    def __init__(self, word: Word):
        super().__init__(word)
        self._expType = ExpType.VOID

    @property
    def exp_type(self) -> ExpType:
        return self._expType


class Integer(WordExpression):

    def __init__(self, integer: int, word: Word):
        super().__init__(word)
        self._integer = integer

    @property
    def integer(self) -> int:
        return self._integer

    @property
    def exp_type(self) -> ExpType:
        return ExpType.INT


class Expression(ExpressionABC):

# (IExpression v1, Operator op, IExpression v2)
    def __init__(self, v1: ExpressionABC, op: Operator, v2: ExpressionABC):
        super().__init__(v1.position)
        self._v1 = v1
        self._op = op
        self._v2 = v2

    @property
    def exp_type(self) -> ExpType:
        return self._op.exp_type()

    @property
    def content(self) -> str:
        return self._v1.content + self._op.content + self._v2.content


# public Enums.ExpType getExpType() { return op.getVyrazTyp(); }
# public IExpression getV1() { return v1; }
# public IExpression getV2() { return v2; }



class BracketExpression(ExpressionABC):

    def __init__(self, z1: Bracket, expression: ExpressionABC, z2: Bracket):
        super().__init__(z1.position)
        self._z1 = z1
        self._z2 = z2
        self._expression = expression

    @property
    def exp_type(self) -> ExpType:
        return self._expression.exp_type

    @property
    def content(self) -> str:
        return self._z1.content + self._expression.content + self._z2.content