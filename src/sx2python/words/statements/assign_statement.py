from __future__ import annotations

from sx2python.words.expresions import WordExpression
from sx2python.words.statements.statements import StatementABC
from sx2python.words.word import Word
from src.sx2python.words.expresions import Expression


# Statement
# ├── AssignStatement         a, b = foo()
# ├── AugAssignStatement      x += 1
# ├── AnnAssignStatement      x: int = 10
# └── WalrusExpression        if (x := foo()) > 0:

# Target
# ├── NameTarget               x = 10
# ├── AttributeTarget          obj.x = 10
# ├── SubscriptTarget          arr[0] = 5
# ├── TODO: Assignable_exp      la().arr[0] = 5
# ├── TupleTarget              a, b = values
# ├── ListTarget               [a, b] = values
# └── StarTarget               a, *rest = values

class Assign(StatementABC):

    def __init__(self, target: NameTarget, value: Expression):
        super().__init__(target.position)
        self._target = target
        self._value = value

    @property
    def content(self) -> str:
        return f"{self._target.content} = {self._value.content}"


class Target:
    pass


class NameTarget(Word, Target):

    def __init__(self, word: Word):
        super().__init__(word.position, word.content)
