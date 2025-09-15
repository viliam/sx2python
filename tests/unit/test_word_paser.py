import unittest
from typing import Callable, Any, Dict
from unittest import TestCase

from src.sx2python.common import SxError
from src.sx2python.enums import SxErrorType
from src.sx2python.parsers.parser import SxParser
from src.sx2python.parsers.word_paser import WordParser

from src.sx2python.text import Text, Position

class PositiveTest:

    def __init__(self,
                 unit_test: TestCase,
                 test_def: Dict[str, Any],
                 do_the_test : Callable[[], SxParser]
                 ):
        super().__init__()
        self._lines = test_def.get("lines")
        self._position = test_def.get("position", Position(0, 0))
        self._expected_position = test_def.get("expected_position")
        self._expected_word_position = test_def.get("expected_word_position", Position(0, 0))
        self._expected_word_content = test_def.get("expected_word_content")
        self._unit_test = unit_test
        self._do_the_test = do_the_test

    def do_the_test(self):
        text = Text(self._lines)
        text.position = self._position
        word =  self._do_the_test().read(text)

        self._unit_test.assertEqual(self._expected_position, text.position)
        self._unit_test.assertEqual(self._expected_word_content, word.content)
        self._unit_test.assertEqual(self._expected_word_position, word.position)

class TestWordParser(unittest.TestCase):

    def test_read_single_word(self):
        PositiveTest(self, {
            "lines": ["Hello"],
            "expected_position": Position(5, 0),
            "expected_word_content": "Hello"
        }, lambda: WordParser.i()).do_the_test()

    def test_read_multiple_words(self):
        PositiveTest(self, {
            "lines": ["Hello World"],
            "expected_position": Position(5, 0),
            "expected_word_content": "Hello"
        }, lambda: WordParser.i()).do_the_test()

    def test_read_second_word(self):
        PositiveTest(self, {
            "lines": ["Hello World"],
            "position": Position(5, 0),
            "expected_position": Position(11, 0),
            "expected_word_position": Position(6, 0),
            "expected_word_content": "World"
        }, lambda: WordParser.i()).do_the_test()

    def test_read_handles_leading_whitespace(self):
        PositiveTest(self, {
            "lines": ["   Hello"],
            "expected_position": Position(8, 0),
            "expected_word_position": Position(3, 0),
            "expected_word_content": "Hello"
        }, lambda : WordParser.i()).do_the_test()

    def test_read_empty_text(self):
        """Test that 'read' raises SxError when text is empty."""
        text = Text([""])

        with self.assertRaises(SxError) as context:
            WordParser.i().read(text)

        self.assertEqual(SxErrorType.EXPECTED_TOKEN, context.exception._typ)
