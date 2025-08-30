from src.sx2python.common import SxError
from src.sx2python.enums import SxErrorTypes
from src.sx2python.parsers.parser import SxParser
from src.sx2python.parsers.word_paser import WordParser
from src.sx2python.text import Text
from src.sx2python.words.expresions import Integer


class IntegerParser(SxParser[Integer]):

    _instance = None

    def read(self, text: "Text") -> Integer:
        position = text.position
        a_int = WordParser.instance().read(text).content
        if not a_int.isdigit():  raise SxError.create( SxErrorTypes.EXPECTED_INT, text)

        return Integer(a_int, position)
