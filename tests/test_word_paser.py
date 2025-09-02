import unittest

from src.sx2python.common import SxError
from src.sx2python.enums import SxErrorType
from src.sx2python.parsers.word_paser import WordParser

from src.sx2python.text import Text, Position


class TestWordParser(unittest.TestCase):

    def test_read_single_word(self):
        """Test that 'read' correctly parses a single word."""
        text = Text(["Hello"])
        word =  WordParser.instance().read(text)

        self.assertEqual(Position(5, 0), text.position)
        self.assertEqual("Hello", word.content)
        self.assertEqual(Position(0, 0), word.position)

    def test_read_empty_text(self):
        """Test that 'read' raises SxError when text is empty."""
        text = Text([""])

        with self.assertRaises(SxError) as context:
            WordParser.instance().read(text)

        self.assertEqual(SxErrorType.EMPTY_WORD, context.exception._typ)

    def test_read_multiple_words(self):
        """Test that 'read' parses the first word in a line with multiple words."""
        text = Text(["Hello World"])
        word =  WordParser.instance().read(text)

        self.assertEqual(Position(5, 0), text.position)
        self.assertEqual("Hello", word.content)
        self.assertEqual(Position(0, 0), word.position)

    def test_read_handles_leading_whitespace(self):
        """Test that 'read' skips leading whitespace and parses the first word."""
        text = Text(["   Hello"])
        word =  WordParser.instance().read(text)

        self.assertEqual(Position(8, 0), text.position)
        self.assertEqual("Hello", word.content)
        self.assertEqual(Position(3, 0), word.position)

    def test_read_second_word(self):
        """Test that 'read' parses the second word in a line with multiple words."""
        text = Text(["Hello World"])
        text.position = Position(5, 0)
        word =  WordParser.instance().read(text)

        self.assertEqual(Position(11, 0), text.position)
        self.assertEqual("World", word.content)
        self.assertEqual(Position(6, 0), word.position)
