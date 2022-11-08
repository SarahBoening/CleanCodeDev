import unittest

import csv_reader.cli_handling as cli
import csv_reader.table_utils as table_ut


class TestCSVViewer(unittest.TestCase):
    def test_load_file(self):
        read_table = table_ut.read_csv_to_list("data\\besucher.csv")
        self.assertEqual(read_table[0], ["No.", "Name", "Alter", "Letzter Besuch", "Ort"])

    def test_wrong_file(self):
        self.assertRaises(FileNotFoundError, table_ut.read_csv_to_list, "data\\123456.csv")

    def test_get_page(self):
        table = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.assertEqual(table_ut.get_page(table, 2, 1), [["1", "2", "3"], ["4", "5", "6"]])

    def test_calculate_column_widths(self):
        self.assertEqual(table_ut.calculate_column_widths([["1", "2", "3"], ["11", "222", "3333"]]), [2, 3, 4])

    def test_table_to_str(self):
        table = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        table_str = "|1|2|3|\n|-+-+-|\n|4|5|6|\n|7|8|9|\n"
        self.assertEqual(table_ut.table_to_str(table, [1,1,1], False, ""), table_str)

    def test_table_sort(self):
        table = [["4", "5", "6"], ["7", "8", "9"], ["1", "2", "3"]]
        table_str = "|4|5|6|\n|-+-+-|\n|1|2|3|\n|7|8|9|\n"
        self.assertEqual(table_ut.table_to_str(table, [1, 1, 1], True, "5"), table_str)

    def test_wrong_sort_column(self):
        table = [["4", "5", "6"], ["7", "8", "9"], ["1", "2", "3"]]
        self.assertRaises(ValueError, table_ut.table_to_str, table, [1,1,1], True, "abc")

    def test_upper_bound_page_no(self):
        self.assertEqual(cli.bound_page(22, 20), 20)

    def test_lower_bound_page_no(self):
        self.assertEqual(cli.bound_page(-22, 20), 1)


if __name__ == "__main__":
    unittest.main()
