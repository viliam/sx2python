from abc import abstractmethod
from typing import TypeVar

from src.sx2python.common import SxError
from src.sx2python.enums import ReservedWordGroupEnum, SxErrorType
from src.sx2python.parsers.parser import SxParser
from src.sx2python.parsers.word_paser import  WordParser
from src.sx2python.text import Text

E = TypeVar('E', bound='Word')

class ReservedWordAbstractReader(SxParser[E]):

    def read(self, text: Text) -> E:
        word = WordParser.instance().read(text).content
        if not self.reserved_word.contains(word):
            raise SxError(self.sx_error_type, text.position, text.line)

        return word

    @property
    @abstractmethod
    def reserved_word(self) -> ReservedWordGroupEnum:
        ...

    @property
    @abstractmethod
    def sx_error_type(self) -> SxErrorType:
        ...


