from abc import ABC, abstractmethod

from src.sx2python.text import Position


class WordABC(ABC):
    def __init__(self, position: Position):
        self._position = position

    @property
    @abstractmethod
    def content(self) -> str:
        ...

    @property
    def position(self):
        return self._position

class Word(WordABC):
    def __init__(self, position: Position, content: str=None):
        super().__init__(position)
        self._content = content

    @classmethod
    def from_word(cls, word: "Word"):
        return cls(word.position, word.content)

    def __str__(self):
        return self._content if self._content is not None else ""

    @property
    def content(self):
        return self._content
