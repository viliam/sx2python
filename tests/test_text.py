from unittest import TestCase

from src.sx2python.common import SxError
from src.sx2python.enums import SxErrorType
from src.sx2python.position import Position
from src.sx2python.text import Text


class TestText(TestCase):

# ----------------------------------------------  next_char_position
    def test_next_char_position_simple_text(self):
        text = Text(["Hello", "World"])
        result = text.next_char_position()
        self.assertIsNotNone(result)
        self.assertEqual(result.x, 0)
        self.assertEqual(result.y, 0)

    def test_next_char_position_empty_text(self):
        text = Text([])
        result = text.next_char_position()
        self.assertIsNone(result)

    def test_next_char_position_whitespace_text(self):
        text = Text(["   ", "  ", "Hello"])
        result = text.next_char_position()
        self.assertIsNotNone(result)
        self.assertEqual(result.x, 0)
        self.assertEqual(result.y, 2)

# ----------------------------------------------  is_valid_position
    def test_is_valid_position_incorrect(self):
        positions = [
            ((0, -1), "y_negative"),
            ((-1, 0), "x_negative"),
            ((0, 2),  "y_out_of"),
            ((2, 0),  "x_out_of")
        ]
        for (x, y), test_name in positions:
            with self.subTest(test_name):
                self.assertFalse(Text(["la"])._is_valid_position(x, y))

    def test_is_valid_position(self):
        self.assertTrue(Text(["la"])._is_valid_position(0, 0))
        self.assertTrue(Text(["la", "lo"])._is_valid_position(1, 1))


# ----------------------------------------------  next_char
    def test_next_char_simple_text(self):
        text = Text(["    Hello", "World"])
        result = text.next_char()
        self.assertIsNotNone(result)
        self.assertEqual(result, "H")
        self.assertEqual(text.position.x, 0)
        self.assertEqual(text.position.y, 0)

    def test_next_char_empty_text(self):
        text = Text([])
        with self.assertRaises(SxError) as context:
            text.next_char()

        self.assertEqual(SxErrorType.END_OF_FILE, context.exception._typ)

    # ----------------------------------------------  _look_ahead
    def test_look_ahead_finds_word(self):
        text = Text(["TestWord example"])
        result = text.look_ahead()
        self.assertEqual("TestWord", result)

    def test_look_ahead_empty_string(self):
        text = Text([""])
        result = text.look_ahead()
        self.assertEqual("", result)

    def test_look_ahead_start_index_beyond_length(self):
        text = Text(["ShortWord"])
        text.position = Position(len("ShortWord"), 0)
        result = text.look_ahead()
        self.assertEqual("", result)

    def test_look_ahead_non_word_character(self):
        text = Text(["Test1@Word"])
        text.position= Position(5,0)
        result = text.look_ahead()
        self.assertEqual("", result)

    # ----------------------------------------------  _find_end_of_word
    def test_find_end_of_word_correct_index(self):
        line = "OpenAI Language Model"
        result = Text._find_end_of_word(line, 7)
        self.assertEqual(15, result)

    def test_find_end_of_word_no_word_characters(self):
        line = "!@#$%^&*"
        result = Text._find_end_of_word(line, 0)
        self.assertEqual(0, result)

    def test_find_end_of_word_index_out_of_bounds(self):
        line = "TextExample"
        result = Text._find_end_of_word(line, len(line))
        self.assertEqual(len(line), result)
