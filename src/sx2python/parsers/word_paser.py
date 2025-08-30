from src.sx2python.common import SxError
from src.sx2python.enums import SxErrorTypes
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
        text.next_char()
        position = text.position
        begin_x = position.x
        word = self._look_ahead(text.line, begin_x)

        if "" == word:  raise SxError.create( SxErrorTypes.EMPTY_WORD, text)

        end_x = begin_x + len(word)
        text.position = Position(end_x, position.y)
        return Word(position, word)


    @staticmethod
    def _look_ahead(line: str, x: int) -> str:
        end_x = WordParser._find_end_of_word(line, x)
        return line[x:end_x] if x < end_x else ""

    @staticmethod
    def _find_end_of_word(line: str, x: int) -> int:
        return next(
            (i for i, ch in enumerate(line[x:], start=x) if not ch.isalnum()),
            len(line)
        )
