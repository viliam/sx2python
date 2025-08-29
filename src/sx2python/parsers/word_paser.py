from src.sx2python.text import Text
from src.sx2python.text_context_gen import Word

"""###
public Word read(TextContext tC)  {
    tC.findNextCharacter();
    Position inx= tC.getPosition();
    int beginX =inx.getX();

    String line = tC.getLine();
    String word = lookAhead(line, beginX);
    if ("".equals(word) )
    throw SxException.create(SxExTyp.EMPTY_WORD, tC);

    int endX = beginX + word.length();
    tC.setPosition(new Position(endX, inx.getY()));
    return new Word(inx, word);
}
"""

class WordParser:

    def read(self, text: "Text") -> Word:
        text.next_char()
        inx = text.position
        return None # TODO


    @staticmethod
    def _look_ahead(line: str, x: int) -> str:
        end_x = WordParser._find_end_of_word(line, x)
        return line[x:end_x] if x < end_x else ""

    @staticmethod
    def _find_end_of_word(line: str, x: int) -> int:
        return next(
            (i for i, ch in enumerate(line[x:], start=x) if not ch.isalnum()),
            len(line)
        )
