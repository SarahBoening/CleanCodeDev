from math import ceil


def is_first_page(page_no):
    return page_no == 1


def get_no_of_pages(table, lines_per_page):
    return ceil(len(table) / lines_per_page)


def read_csv_to_list(filename):
    with open(filename, "r", encoding="utf-8") as f:
        csv_table = f.readlines()
    for i, row in enumerate(csv_table):
        row = row.replace("\n", "").split(';')
        if i == 0:
            row.insert(0, "No.")
        else:
            row.insert(0, str(i))
        csv_table[i] = row
    return csv_table


def get_page(table, lines_per_page, page):
    header = table[0]
    if page == 1:
        return table[0:lines_per_page]
    elif page == get_no_of_pages(table, lines_per_page):
        return [header] + table[(page - 1) * lines_per_page:]
    return [header] + table[(page - 1) * lines_per_page:page * lines_per_page]


def calculate_column_widths(table):
    widths = [0] * len(table[0])
    for row in table:
        for i, cell in enumerate(row):
            str_len = len(cell)
            if str_len > widths[i]:
                widths[i] = str_len
    return widths


def table_to_str(table, max_widths, do_sort, col_to_sort):
    table_str = ""
    if do_sort:
        table = __sort_table(table, col_to_sort)
    for i, row in enumerate(table):
        table_str += __add_row(row, max_widths)
        if i == 0:
            table_str += __add_line(max_widths)
    return table_str


def __sort_table(table, col_to_sort):
    header = table[0]
    if __verify_column(table, col_to_sort):
        index_ = table[0].index(col_to_sort)
        table = table[1:]
        table.sort(key=lambda x: x[index_])
        table = [header] + table
    else:
        raise ValueError("Entered name is not a column name")
    return table


def __add_line(max_widths):
    no_cols = len(max_widths)
    line_str = "|"
    for i, width in enumerate(max_widths):
        line_str += "-" * width
        if i < no_cols - 1:
            line_str += "+"
    line_str += "|\n"
    return line_str


def __add_row(row, max_widths):
    row_str = "|"
    for i, cell in enumerate(row):
        cell_str = cell + (" " * (max_widths[i] - len(cell)))
        row_str += cell_str
        row_str += "|"
    row_str += "\n"
    return row_str


def __verify_column(table, column):
    return column in table[0]
