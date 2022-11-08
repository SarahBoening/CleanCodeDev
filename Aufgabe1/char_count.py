import typing
import unittest


def count_chars(input: str) -> typing.Dict[str, int]:
    chars = {}
    for ch in input:
        if ch not in chars.keys():
            chars[ch] = 0
        chars[ch] += 1
    return chars


def count_chars_lower(input: str) -> typing.Dict[str, int]:
    return count_chars(input.lower())


class TestCountChars(unittest.TestCase):
    def test_count_chars(self):
        results_dict = {'D': 1, 'a': 2, 's': 2, ' ': 3, 'd': 1, 'r': 1, 'f': 1, 'n': 2, 'i': 2, 'c': 1, 'h': 1, 't': 1,
                        'e': 1}
        test_dict = count_chars("Das darf nicht sein")
        self.assertEqual(test_dict, results_dict)

    def test_count_chars_empty(self):
        result_dict = {}
        test_dict = count_chars("")
        self.assertEqual(test_dict, result_dict)

    def test_count_chars_lower(self):
        results_dict = {'d': 2, 'a': 2, 's': 2, ' ': 3, 'r': 1, 'f': 1, 'n': 2, 'i': 2, 'c': 1, 'h': 1, 't': 1, 'e': 1}
        test_dict = count_chars_lower("Das darf nicht sein")
        self.assertEqual(test_dict, results_dict)


if __name__ == "__main__":
    unittest.main()
