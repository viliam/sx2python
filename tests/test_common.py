import unittest

from src.sx2python.common import SxError
from src.sx2python.enums import SxErrorType
from src.sx2python.position import Position


class TestMakeMessage(unittest.TestCase):

    def test_valid_message_creation(self):
        """Test that '_make_message' correctly creates an error message with a valid position and line."""
        position = Position(4, 0)
        line = "Example line"
        result = SxError._make_message(SxErrorType.UNEXPECTED_PREFIX, position, line)
        expected = f"UNEXPECTED_PREFIX  : Example line    \n char = p"
        self.assertEqual(expected, result)

