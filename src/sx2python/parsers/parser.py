from _typing import Generic
from abc import ABC
from typing import TypeVar

from src.sx2python.text import Text
from src.sx2python.words.word import WordABC, Word

TWord = TypeVar('TWord', bound=Word)
TWordABC = TypeVar('TWordABC', bound=WordABC)

class SxParser(ABC, Generic[TWord]):

    _instance = None

    """Subclass must override _instance property."""
    def __init_subclass__(cls):
        super().__init_subclass__()
        if not hasattr(cls, "_instance"):
            raise NotImplementedError(f"{cls.__name__} must override '_instance'")

        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def i(cls):  return cls._instance

    def read(self, text: "Text") -> TWord:  ...

