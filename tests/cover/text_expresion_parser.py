import unittest

from src.sx2python.common import SxError
from src.sx2python.enums import SxErrorType, ExpType
from src.sx2python.parsers.expresions_parsers import  ExpressionParser
from src.sx2python.text import Text

class TestExpressionsParsers(unittest.TestCase):

    def test_read_simple_positive(self):
        self._do_the_test([
            (["23"],      ExpType.INT),
            (["ahoj"],    ExpType.UNKNOWN)
        ])

    def test_read_simple_negative(self):
        self._do_the_test_negative([
            (["23dd"],    SxErrorType.EXPECTED_INT),
            (["ahoj+"],   SxErrorType.END_OF_FILE)
        ])

    def test_read_binary_positive(self):
        self._do_the_test([
            (["23+3"],    ExpType.INT),
            (["23+a"],    ExpType.INT),
            (["23*a"],    ExpType.INT),
            (["23/a"],    ExpType.INT),
            (["23**a"],   ExpType.INT),
            (["(23+a)"],  ExpType.INT)
        ])

    def test_read_complex_positive(self):
        self._do_the_test([
            (["(23+a)-4"],ExpType.INT)
        ])

    def test_read_multi_line(self):
        self._do_the_test([
            (["23+3+\\","4"], ExpType.INT),
            (["(23+3+","4)"], ExpType.INT)
        ])

    def test_read_multi_line_negative(self):
        self._do_the_test_negative([
            (["23+3+","4"], SxErrorType.EXPECTED_TOKEN)
        ])

    def _do_the_test(self, cases):
        for lines, expected_type in cases:
            with self.subTest(lines):
                text = Text(lines)
                result = ExpressionParser.i().read(text)
                self.assertEqual(expected_type, result.exp_type)

    def _do_the_test_negative(self, cases):
        for lines, expected_type in cases:
            with self.subTest(lines):
                text = Text(lines)
                with self.assertRaises(SxError) as context:
                    ExpressionParser.i().read(text)

                self.assertEqual(expected_type, context.exception._typ)