from src.sx2python.common import SxError
from src.sx2python.enums import SxErrorTypes
from src.sx2python.parsers.parser import SxParser
from src.sx2python.parsers.word_paser import WordParser
from src.sx2python.text import Text
from src.sx2python.words.expresions import Integer, Variable, Expression


class IntegerParser(SxParser[Integer]):

    _instance = None

    def read(self, text: "Text") -> Integer:
        position = text.position
        a_int = WordParser.instance().read(text).content
        if not a_int.isdigit():  raise SxError.create( SxErrorTypes.EXPECTED_INT, text.position, text.line)

        return Integer(a_int, position)


class VariableParser(SxParser[Variable]):

    def read(self, text: "Text") -> Variable:
        name =  WordParser.instance().read(text)
        return Variable(name)



class SimpleExprReader(SxParser[Expression]):

    def read(self, text: "Text") -> Expression:
        if text.is_prefix_int(): return IntegerParser.instance().read(text);
        if text.is_prefix_variable(): return VariableParser.instance().read(text)
        # if (tC.isPrefixDataType()) return Readers.dataType().read(tC);
        # if (tC.isPrefixCommand() ) return Readers.command().read(tC);
        raise SxError.create( SxErrorTypes.UNEXPECTED_PREFIX, text )


class ExprReader(SxParser[Expression]):
    ...


class BracketExpression(SxParser[Expression]):
    ...
    # Bracket z1 = Readers.bracket().read(tC);
    # IExpression expression = Readers.expression().read(tC);
    # Bracket z2 = Readers.bracket().read(tC);
    # return new sk.wlio.sx2.beans.expression.BracketExpression(z1, expression, z2);
