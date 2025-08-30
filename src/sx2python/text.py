from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def add_x(self, by: int) -> "Position":
        return Position(self.x + by, self.y)

    def __str__(self) -> str:
        return f"({self.x},{self.y})"


class Text:
    """holds the text to analyze and provide basic functions to read it"""

    def __init__(self, lines: list[str]):
        self._lines = lines
        self._position = Position( 0, 0)


    @property
    def position(self):
        return self._position


    @position.setter
    def position(self, value):
        self._position = value


    @property
    def line(self):
        return self._lines[self._position.y]


    def line_at(self, row: int) -> str:
        return self._lines[row] if 0 <= row < len(self._lines) else ""


    def next_char(self) -> Optional[Position]:
        """Move cursor to a next not empty character"""
        position = self._position
        x = position.x
        y = position.y

        for y, line in enumerate(self._lines, start=position.y):
            if len(line[x:].lstrip()) > 0:
                x = len(line) - len(line[x:].lstrip())
                break
            else:
                x = 0
                y += 1

        if not self._is_valid_position(x, y) :
            return None

        self.position = Position(x, y)
        return self.position


    def _is_valid_position(self, x: int, y: int) -> bool:
        if y < 0 or y >= len(self._lines):
            return False
        if x < 0 or x >= len(self._lines[y]):
            return False

        return True


    def is_end_of_file(self) -> bool:
        return self.next_char() is None