from _typing import Generic
from typing import Callable
from unittest import TestCase

from src.sx2python.parsers.parser import TWord, SxParser
from src.sx2python.text import Text, Position

class PositiveTest(Generic[TWord]):

    def __init__(self,
                 unit_test: TestCase,
                 lines: list[str],
                 position: Position,
                 expected_position : Position,
                 expected_word_position: Position,
                 expected_word_content: str,
                 do_the_test : Callable[[], SxParser]
                 ):
        super().__init__()
        self._unit_test = unit_test
        self._lines = lines
        self._position = position
        self._expected_position = expected_position
        self._expected_word_position = expected_word_position
        self._expected_word_content = expected_word_content
        self._do_the_test = do_the_test

    def do_the_test(self):
        text = Text(self._lines)
        text.position = self._position
        word =  self._do_the_test().read(text)

        self._unit_test.assertEqual(self._expected_position, text.position)
        self._unit_test.assertEqual(self._expected_word_content, word.content)
        self._unit_test.assertEqual(self._expected_word_position, word.position)


class PositiveTestBuilder:
    def __init__(self):
        self._unit_test = None
        self._lines = None
        self._position = Position(0, 0)
        self._expected_position = None
        self._expected_word_position = Position(0, 0)
        self._expected_word_content = None
        self._do_the_test = None

    def with_unit_test(self, unit_test: TestCase):
        self._unit_test = unit_test
        return self

    def with_lines(self, lines: list[str]):
        self._lines = lines
        return self

    def with_position(self, position: Position):
        self._position = position
        return self

    def with_expected_position(self, expected_position: Position):
        self._expected_position = expected_position
        return self

    def with_expected_word_position(self, expected_word_position: Position):
        self._expected_word_position = expected_word_position
        return self

    def with_expected_word_content(self, expected_word_content: str):
        self._expected_word_content = expected_word_content
        return self

    def with_do_the_test(self, do_the_test: Callable[[], TWord]):
        self._do_the_test = do_the_test
        return self

    def build(self) -> PositiveTest:
        return PositiveTest(
            unit_test=self._unit_test,
            lines=self._lines,
            position=self._position,
            expected_position=self._expected_position,
            expected_word_position=self._expected_word_position,
            expected_word_content=self._expected_word_content,
            do_the_test=self._do_the_test
        )
