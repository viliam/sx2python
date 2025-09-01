from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def add_x(self, by: int) -> "Position":
        return Position(self.x + by, self.y)

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    @classmethod
    def create(cls, pos: "Position") -> "Position":
        return cls(pos.x, pos.y)

