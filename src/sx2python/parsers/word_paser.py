from src.sx2python.common import SxError
from src.sx2python.enums import SxErrorType
from src.sx2python.parsers.parser import SxParser
from src.sx2python.text import Text, Position
from src.sx2python.words.word import Word


class WordParser(SxParser[Word]):

    _instance = None

    @classmethod
    def i(cls) -> SxParser[Word]:
        if cls._instance is None:
            cls._instance = cls()

        return cls._instance

    def _next_char_position(self, text: "Text"):
        text.next_char_position()

    def read(self, text: "Text") -> Word:
        self._next_char_position(text)
        position = text.position
        begin_x = position.x
        word = text.look_ahead()

        if "" == word:  raise SxError.create(SxErrorType.EXPECTED_TOKEN, text.position, text.line)

        end_x = begin_x + len(word)
        text.position = Position(end_x, position.y)
        return Word(position, word)

class WordExpressionParser(WordParser):

    def _next_char_position(self, text: "Text"):
        text.next_char_position_in_expression()
