import unittest

import LOCCount.args_parse as argsp
import LOCCount.file_reader as fr
import LOCCount.LOC_count as loc


class TextLOCCount(unittest.TestCase):
    # read_file
    def test_read_file_correct(self):
        self.assertEqual("./test", argsp.read_file(["", "./test"]))

    def test_read_file_error(self):
        self.assertEqual(".", argsp.read_file([]))

    # list_py_files_from_directory
    def test_list_py_files(self):
        self.assertEqual(['.\\args_parse.py', '.\\file_reader.py', '.\\interactors.py', '.\\LOC_count.py', '.\\main.py',
                          '.\\TestLOCCount.py', '.\\ui.py'], fr.list_py_files_from_directory("."))

    # count_for_files
    def test_count_for_files(self):
        self.assertEqual(([["1.py", 3, 3], ["2.py", 0, 3]], 3, 6),
                         loc.count_for_files([["1.py", "def main():\ni=100\ni+=1"],
                                              ["2.py", "# def main():\n  # i=100\n#i+=1"]]))

    # count_loc
    def test_count_loc(self):
        self.assertEqual((3, 3), loc.count_loc("def main():\ni=100\ni+=1"))

    def test_count_loc_no_loc(self):
        self.assertEqual((0, 3), loc.count_loc("# def main():\n  # i=100\n#i+=1"))

    # is_loc
    def test_is_loc(self):
        self.assertEqual(True, loc.is_loc("i += 1"))

    def test_is_not_loc_comment(self):
        self.assertEqual(False, loc.is_loc("# comment"))

    def test_is_not_loc_spaces(self):
        self.assertEqual(False, loc.is_loc("    "))

    # split_code_file
    def test_split_code_file(self):
        self.assertEqual(["def main():", "i=100", "i+=1"], loc.split_code_file("def main():\ni=100\ni+=1"))


if __name__ == "__main__":
    unittest.main()
