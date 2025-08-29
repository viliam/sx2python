from unittest import TestCase

from src.sx2python.parsers.word_paser import WordParser

class TestWordParser(TestCase):

    # ----------------------------------------------  _look_ahead
    def test_look_ahead_finds_word(self):
        line = "TestWord example"
        result = WordParser._look_ahead(line, 0)
        self.assertEqual("TestWord", result)

    def test_look_ahead_empty_string(self):
        result = WordParser._look_ahead("", 0)
        self.assertEqual("", result)

    def test_look_ahead_start_index_beyond_length(self):
        line = "ShortWord"
        result = WordParser._look_ahead(line, len(line))
        self.assertEqual("", result)

    def test_look_ahead_non_word_character(self):
        line = "Test1@Word"
        result = WordParser._look_ahead(line, 5)
        self.assertEqual("", result)

    # ----------------------------------------------  _find_end_of_word
    def test_find_end_of_word_correct_index(self):
        line = "OpenAI Language Model"
        result = WordParser._find_end_of_word(line, 7)
        self.assertEqual(15, result)

    def test_find_end_of_word_no_word_characters(self):
        line = "!@#$%^&*"
        result = WordParser._find_end_of_word(line, 0)
        self.assertEqual(0, result)

    def test_find_end_of_word_index_out_of_bounds(self):
        line = "TextExample"
        result = WordParser._find_end_of_word(line, len(line))
        self.assertEqual(len(line), result)
