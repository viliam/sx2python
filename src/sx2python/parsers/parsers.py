from typing import Protocol

from src.sx2python.text import Text

class SxParser(Protocol):
    def read(self, text: "Text"):
        ...

class SxParserFactory:
    # def
    pass