from dataclasses import dataclass

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

    @property
    def line(self):
        return self._lines[self._position.y]


    def next_char(self):
        """Move cursor to a next not empty character"""
        inx = self._position
        x = inx.x
        y = inx.y

        for y, line in enumerate(self._lines, start=inx.y):
            if len(line.lstrip()) > 0:
                x = len(line) - len(line.lstrip())
                break
            else:
                y += 1

        if not self._is_valid_position(x, y) :
            return None

        self._lines = Position(x, y )
        return self._lines


    def _is_valid_position(self, x: int, y: int) -> bool:
        """
        Returns True if the position (x, y) is within the bounds of the text.
        """
        if y < 0 or y >= len(self._lines):
            return False
        if x < 0 or x >= len(self._lines[y]):
            return False

        return True


