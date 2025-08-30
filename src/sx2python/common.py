from typing import Optional

from src.sx2python.enums import SxErrorTypes
from src.sx2python.text import Position
from src.sx2python.text import Text


class SxError(Exception):


    def __init__(self, typ: SxErrorTypes, message: str, position: Optional[Position]):
        super().__init__(message)
        self._typ = typ
        self._position = position


    @classmethod
    def create(cls, typ: SxErrorTypes, text: Text) -> "SxError":
        return cls.create_with_message(typ, None, text)


    @classmethod
    def create_with_message(cls, typ: SxErrorTypes, message: Optional[str], text: Text) -> "SxError":
        pos = text.position
        if message is None:
            if text.is_end_of_file():
                return cls(typ, str(typ), pos)
            message = cls._make_message(typ, pos, text)
        return cls(typ, message, pos)


    @classmethod
    def create_with_position(cls, typ: SxErrorTypes, position: Position) -> "SxError":
        return cls(typ, str(typ), position)


    @staticmethod
    def _make_message(typ: SxErrorTypes, position: Position, text: Text) -> str:
        row = position.y
        col = position.x
        line = text.line_at(row)
        a_char = line[col] if len(line) > col else ' '

        return f"{typ}  : {line}    \n char = {a_char}"


    def __str__(self) -> str:
        base = super().__str__()
        if self._position is not None:
            return f"{base}  \n row = {self._position.y} ,   column = {self._position.x}"
        return base