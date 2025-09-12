from src.sx2python.common import SxError
from src.sx2python.enums import SxErrorType
from src.sx2python.parsers.parser import SxParser
from src.sx2python.parsers.symbols_parsers import BracketParser, OperatorExpressionParser
from src.sx2python.parsers.word_paser import WordParser
from src.sx2python.text import Text
from src.sx2python.words.expresions import Integer, Variable, ExpressionABC, BracketExpression, Expression


class IntegerParser(SxParser[Integer]):

    _instance = None

    def read(self, text: "Text") -> Integer:
        int_word = WordParser.i().read(text)
        a_int = int_word.content
        if not a_int.isdigit():  raise SxError.create(SxErrorType.EXPECTED_INT, text.position, text.line)

        return Integer(a_int, int_word)


class VariableParser(SxParser[Variable]):

    def read(self, text: "Text") -> Variable:
        name =  WordParser.i().read(text)
        return Variable(name)


# class DataTypeParser(ReservedWordAbstractParser[DataType]):
#
#     @property
#     def reserved_word(self) -> ReservedWordGroupEnum:
#         return ReservedWordGroupEnum.DATA_TYPE
#
#     @property
#     def sx_error_type(self) -> SxErrorType:
#         return SxErrorType.EXPECTED_DATA_TYPE
#


class SimpleExpressionParser(SxParser[ExpressionABC]):

    def read(self, text: "Text") -> ExpressionABC:
        if text.is_prefix_int(): return IntegerParser.i().read(text);
        if text.is_prefix_variable(): return VariableParser.i().read(text)
        # if (tC.isPrefixCommand() ) return Readers.command().read(tC);  TODO: it's statement
        raise SxError.create(SxErrorType.UNEXPECTED_PREFIX, text.position, text.line)


class ExpressionParser(SxParser[ExpressionABC]):

    def read(self, text: "Text") -> ExpressionABC:
        expr = (
            BracketExpressionParser.i().read(text)
            if text.is_prefix_bracket_open()
            else SimpleExpressionParser.i().read(text)
        )
        if text.is_end_of_file(): return expr

        if text.is_prefix_operator():
            op = OperatorExpressionParser.i().read(text)
            return Expression(expr, op, ExpressionParser.i().read(text))

        if not text.is_end_of_file(): self._check_end_of_expression(text)

        return expr

    def _check_end_of_expression(self, text: "Text") :
        ...
#     if  ( !tC.isPrefixOperator() && !tC.isPrefixComma() && !tC.isPrefixBracketClosed() )
#         throw SxException.create(SxExTyp.EXPECTED_OPERATOR, tC);


class BracketExpressionParser(SxParser[ExpressionABC]):

    def read(self, text: "Text") -> ExpressionABC:
        z1 = BracketParser.i().read(text)
        ex = ExpressionParser.i().read(text)
        z2 = BracketParser.i().read(text)
        return BracketExpression(z1, ex, z2)
