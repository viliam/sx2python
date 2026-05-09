from sx2python.parsers.parser import SxParser
from sx2python.words.statements.assign_statement import Assign


class AssignParser(SxParser[Assign]):

    def read(self, text: "Text") -> Assign:
        # TODO nacitaj slovo ako NameTarget + '=" + expression
        pass

