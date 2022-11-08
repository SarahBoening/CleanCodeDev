import unittest

import WordCount.file_handling as file
import WordCount.text_handling as txt


class TestCSVViewer(unittest.TestCase):
    def test_split(self):
        self.assertEqual(txt.split_text("Mary had a"), ["Mary", "had", "a"])

    def test_countwords(self):
        self.assertEqual(txt.count_words_in_list("Mary had a little lamb".split(" ")), 5)

    def test_count_nowords(self):
        self.assertEqual(txt.count_words_in_list("a1.2 %".split(" ")), 0)

    def test_read_stopwords(self):
        self.assertEqual(file.read_file_to_list("stopwords.txt"), ["the", "a", "on", "off"])

    def test_filter(self):
        self.assertEqual(txt.filter_words_from_list("Mary had a".split(), ["a"]), ["Mary", "had"])


if __name__ == "__main__":
    unittest.main()
