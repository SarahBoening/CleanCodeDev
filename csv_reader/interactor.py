import csv_reader.cli_handling as cli
import csv_reader.table_utils as table_util


def run(table, lines_per_page):
    do_exit, page_no, last_page = cli.prepare_start(table, lines_per_page)
    max_widths = table_util.calculate_column_widths(table)
    while not do_exit:
        page_no = cli.bound_page(page_no, last_page)
        lines = table_util.get_page(table, lines_per_page, page_no)
        do_sort = cli.get_sorted()
        col_to_sort = cli.get_col_to_sort()
        page_str = table_util.table_to_str(lines, max_widths, do_sort, col_to_sort)
        cli.print_page(page_str, page_no, last_page)
        page_no, do_exit = cli.handle_input(page_no, last_page)


def start():
    file_name, lines_per_page = cli.parse_args()
    table = table_util.read_csv_to_list(file_name)
    run(table, lines_per_page)
