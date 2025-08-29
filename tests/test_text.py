from unittest import TestCase

from src.sx2python.text import Text


class TestText(TestCase):

# ----------------------------------------------  next_char
    def test_next_char_simple_text(self):
        text = ["Hello", "World"]
        context = Text(text)
        result = context.next_char()
        self.assertIsNotNone(result)
        self.assertEqual(result.x, 0)
        self.assertEqual(result.y, 0)

    def test_next_char_empty_text(self):
        text = []
        context = Text(text)
        result = context.next_char()
        self.assertIsNone(result)

    def test_next_char_whitespace_text(self):
        text = ["   ", "  ", "Hello"]
        context = Text(text)
        result = context.next_char()
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