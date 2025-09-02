import unittest

from src.sx2python.common import SxError
from src.sx2python.enums import SxErrorType
from src.sx2python.parsers.expresions_parsers import IntegerParser
from src.sx2python.text import Text, Position


class TestExpressionsParsers(unittest.TestCase):

    def test_read_valid_integer(self):
        """Test that 'read' correctly parses a valid integer."""
        text = Text(["123"])
        integer = IntegerParser.instance().read(text)

        self.assertEqual(Position(3, 0), text.position)
        self.assertEqual("123", integer.integer)
        self.assertEqual(Position(0, 0), integer.position)

    def test_read_invalid_integer_raises_error(self):
        """Test that 'read' raises an SxError when the input is not an integer."""
        text = Text(["abc"])

        with self.assertRaises(SxError) as context:
            IntegerParser.instance().read(text)

        self.assertEqual(SxErrorType.EXPECTED_INT, context.exception._typ)

    def test_read_integer_with_trailing_space(self):
        """Test that 'read' correctly parses an integer with trailing whitespace."""
        text = Text(["456   "])
        integer = IntegerParser.instance().read(text)

        self.assertEqual(Position(3, 0), text.position)
        self.assertEqual("456", integer.integer)
        self.assertEqual(Position(0, 0), integer.position)

    def test_read_integer_in_multiline_text(self):
        """Test that 'read' correctly parses an integer in multiline text."""
        text = Text(["Line1", "789", "Line3"])
        text.position = Position(0, 1)  # Set initial position to line 2
        integer = IntegerParser.instance().read(text)

        self.assertEqual(Position(3, 1), text.position)
        self.assertEqual("789", integer.integer)
        self.assertEqual(Position(0, 1), integer.position)

