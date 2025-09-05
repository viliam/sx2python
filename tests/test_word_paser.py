import unittest

from src.sx2python.common import SxError
from src.sx2python.enums import SxErrorType
from src.sx2python.parsers.word_paser import WordParser

from src.sx2python.text import Text, Position
from tests.commons import PositiveTestBuilder


class TestWordParser(unittest.TestCase):

    def test_read_single_word(self):
         (PositiveTestBuilder()
            .with_unit_test(self)
            .with_lines(["Hello"])
            .with_expected_position(Position(5, 0))
            .with_expected_word_content("Hello")
            .with_do_the_test(lambda: WordParser.instance())
         ).build().do_the_test()

    def test_read_multiple_words(self):
        (PositiveTestBuilder()
         .with_unit_test(self)
         .with_lines(["Hello World"])
         .with_expected_position(Position(5, 0))
         .with_expected_word_content("Hello")
         .with_do_the_test(lambda: WordParser.instance())
         ).build().do_the_test()

    def test_read_second_word(self):
        (PositiveTestBuilder()
         .with_unit_test(self)
         .with_lines(["Hello World"])
         .with_position(Position(5, 0))
         .with_expected_position(Position(11, 0))
         .with_expected_word_position(Position(6, 0))
         .with_expected_word_content("World")
         .with_do_the_test(lambda: WordParser.instance())
         ).build().do_the_test()

    def test_read_handles_leading_whitespace(self):
        (PositiveTestBuilder()
         .with_unit_test(self)
         .with_lines(["   Hello"])
         .with_expected_position(Position(8, 0))
         .with_expected_word_position(Position(3, 0))
         .with_expected_word_content("Hello")
         .with_do_the_test(lambda: WordParser.instance())
         ).build().do_the_test()

    def test_read_empty_text(self):
        """Test that 'read' raises SxError when text is empty."""
        text = Text([""])

        with self.assertRaises(SxError) as context:
            WordParser.instance().read(text)

        self.assertEqual(SxErrorType.EMPTY_WORD, context.exception._typ)
