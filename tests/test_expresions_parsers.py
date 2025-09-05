import unittest

from src.sx2python.common import SxError
from src.sx2python.enums import SxErrorType
from src.sx2python.parsers.expresions_parsers import IntegerParser
from src.sx2python.text import Text, Position
from tests.commons import PositiveTestBuilder


class TestExpressionsParsers(unittest.TestCase):

    def test_read_valid_integer(self):
        (PositiveTestBuilder()
         .with_unit_test(self)
         .with_lines(["123"])
         .with_expected_position(Position(3, 0))
         .with_expected_word_content("123")
         .with_do_the_test(lambda: IntegerParser.instance())
         ).build().do_the_test()

    def test_read_integer_with_trailing_space(self):
        (PositiveTestBuilder()
         .with_unit_test(self)
         .with_lines(["456   "])
         .with_expected_position(Position(3, 0))
         .with_expected_word_content("456")
         .with_do_the_test(lambda: IntegerParser.instance())
         ).build().do_the_test()

    def test_read_integer_in_multiline_text(self):
        (PositiveTestBuilder()
         .with_unit_test(self)
         .with_lines(["Line1", "789", "Line3"])
         .with_position(Position(0, 1))
         .with_expected_position(Position(3, 1))
         .with_expected_word_content("789")
         .with_expected_word_position(Position(0, 1))
         .with_do_the_test(lambda: IntegerParser.instance())
         ).build().do_the_test()

    def test_read_invalid_integer_raises_error(self):
        text = Text(["abc"])  #not an integer

        with self.assertRaises(SxError) as context:
            IntegerParser.instance().read(text)

        self.assertEqual(SxErrorType.EXPECTED_INT, context.exception._typ)