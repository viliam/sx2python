from typing import Protocol

from src.sx2python.text import Text
from typing import TypeVar

from src.sx2python.words.word import WordABC

TWord = TypeVar('TWord', bound=WordABC)

class SxParser(Protocol[TWord]):

    _instance = None

    """Subclass must override _instance property."""
    def __init_subclass__(cls):
        super().__init_subclass__()
        if not hasattr(cls, "_instance"):
            raise NotImplementedError(f"{cls.__name__} must override '_instance'")

    # """Singleton pattern. Initialization of singleton instance"""
    # def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def instance(cls):  return cls._instance


    def read(self, text: Text) -> TWord:  ...

