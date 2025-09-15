import unittest

from src.sx2python.common import SxError
from src.sx2python.enums import SxErrorType, ExpType
from src.sx2python.parsers.expresions_parsers import IntegerParser, SimpleExpressionParser
from src.sx2python.text import Text

class TestExpressionsParsers(unittest.TestCase):

    def test_read_valid_integer(self):
        text = Text(["123"])
        result = SimpleExpressionParser.i().read(text)
        self.assertEqual(ExpType.INT, result.exp_type)


    def test_read_invalid_integer_raises_error(self):
        text = Text(["abc"])  #not an integer

        with self.assertRaises(SxError) as context:
            IntegerParser.i().read(text)

        self.assertEqual(SxErrorType.EXPECTED_INT, context.exception._typ)


    def test_read_simple_expression(self):
        positive_cases = {
            "23":   ExpType.INT,
            "ahoj": ExpType.UNKNOWN
        }
        for word, expected_type in positive_cases.items():
            with self.subTest(word):
                text = Text([word])
                result = SimpleExpressionParser.i().read(text)
                self.assertEqual(expected_type, result.exp_type)

