from src.sx2python.common import SxError
from src.sx2python.enums import SxErrorType
from src.sx2python.parsers.parser import SxParser
from src.sx2python.text import Text, Position
from src.sx2python.words.word import Word


class WordParser(SxParser[Word]):

    _instance = None

    @classmethod
    def instance(cls) -> SxParser[Word]:
        if cls._instance is None:
            cls._instance = cls()

        return cls._instance


    def read(self, text: "Text") -> Word:
        text.next_char_position()
        position = text.position
        begin_x = position.x
        word = text.look_ahead()

        if "" == word:  raise SxError.create(SxErrorType.EMPTY_WORD, text.position, text.line)

        end_x = begin_x + len(word)
        text.position = Position(end_x, position.y)
        return Word(position, word)



