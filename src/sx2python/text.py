from abc import ABC, abstractmethod
from typing import Optional

from src.sx2python.common import SxError
from src.sx2python.enums import SxErrorTypes
from src.sx2python.parsers.word_paser import WordParser
from src.sx2python.position import Position
from src.sx2python.words.word import Word


class Text:
    """holds the text to analyze and provide basic functions to read it"""

    def __init__(self, lines: list[str]):
        self._lines = lines
        self._position = Position( 0, 0)


    @property
    def position(self):
        return self._position


    @position.setter
    def position(self, value):
        self._position = value


    @property
    def line(self):
        return self._lines[self._position.y]


    def line_at(self, row: int) -> str:
        return self._lines[row] if 0 <= row < len(self._lines) else ""


    def next_char_position(self) -> Optional[Position]:
        """Move cursor to a next not empty character"""
        position = self._position
        x = position.x
        y = position.y

        for y, line in enumerate(self._lines, start=position.y):
            if len(line[x:].lstrip()) > 0:
                x = len(line) - len(line[x:].lstrip())
                break
            else:
                x = 0
                y += 1

        if not self._is_valid_position(x, y) :
            return None

        self.position = Position(x, y)
        return self.position


    def _is_valid_position(self, x: int, y: int) -> bool:
        if y < 0 or y >= len(self._lines):
            return False
        if x < 0 or x >= len(self._lines[y]):
            return False

        return True


    def next_char(self) -> str:
        """Move cursor to next character, read that character and return a cursor back"""
        actual = Position.create( self._position)
        self.next_char_position()
        self.ensure_not_eof()

        x, y = self._position.x, self._position.y
        p = self._lines[y][x]    # take a look and
        self._position = actual  # move position back
        return p


    def is_end_of_file(self) -> bool:
        return self.next_char_position() is None

    def ensure_not_eof(self):
        if self.is_end_of_file() :
            raise SxError.create_no_msg(SxErrorTypes.END_OF_FILE, self.position)

    def is_prefix_int(self) -> bool:
        return self.next_char().isdigit()

    def is_prefix_letter(self) -> bool:
        return self.next_char().isalpha() or self.next_char() == '_'

    def is_prefix_variable(self) -> bool:



class IsPrefixTemplateMethod(ABC):

    def __init__(self, text: Text):
        self._text = text

    @abstractmethod
    def is_prefix_word(self, word: Word) -> bool:
        pass

    def is_prefix(self) -> bool:
        text  = self._text
        pos = text.position
        try:
            print("do work")
            if not text.is_prefix_letter():
                return False
            word = WordParser.instance().read(text)
            return self.is_prefix_word(word)
        finally:
            text.position = pos


    # abstract class IsPrefixTemplateMetod {
    #     public boolean isPrefix()  {
    #         Position pos = getPosition();
    #         try {
    #             if (!isPrefixLetter() ) {
    #                return false;
    #             }
    #
    #             Word word = Readers.word().read(TextContext.this);
    #             return  isPrefix(word);
    #         } finally {
    #             setPosition(pos);
    #         }
    #     }
    #
    #     protected abstract boolean isPrefix(Word word);
    # }


    # abstract class IsPrefixDeclarationTemplateMetod {
    #     public boolean jePrefix()  {
    #         Position position = getPosition();
    #         try {
    #             if (isEndOfFile() || !isPrefixLetter() )
    #                 return false;
    #             Word word = Readers.word().read(TextContext.this);
    #             return RezervedWordsEnum.DATA_TYPE.is(word.getContent()) && isPrefixName();
    #         } finally {
    #             setPosition(position);
    #         }
    #     }
    #
    #     protected abstract boolean isPrefixName();
    # }