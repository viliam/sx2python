from typing import Optional

from src.sx2python.enums import SxErrorTypes
from src.sx2python.position import Position


class SxError(Exception):

    def __init__(self, typ: SxErrorTypes, message: str, position: Position):
        super().__init__(message)
        self._typ = typ
        self._position = position


    @classmethod
    def create_no_msg(cls, typ: SxErrorTypes, position: Position) -> "SxError":
        return cls(typ, str(typ), position)

    @classmethod
    def create(cls, typ: SxErrorTypes, position: Position, line: str) -> "SxError":
        return cls.create_with_message(typ, None, position, line)


    @classmethod
    def create_with_message(cls, typ: SxErrorTypes, message: Optional[str], position: Position, line: str) -> "SxError":
        if message is None:
            message = cls._make_message(typ, position, line)

        return cls(typ, message, position)


    @classmethod
    def create_with_position(cls, typ: SxErrorTypes, position: Position) -> "SxError":
        return cls(typ, str(typ), position)


    @staticmethod
    def _make_message(typ: SxErrorTypes, position: Position, line: str) -> str:
        col = position.x
        a_char = line[col] if len(line) > col else ' '

        return f"{typ.name}  : {line}    \n char = {a_char}"


    def __str__(self) -> str:
        base = super().__str__()
        if self._position is not None:
            return f"{base}  \n row = {self._position.y} ,   column = {self._position.x}"
        return base