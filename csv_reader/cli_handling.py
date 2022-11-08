import sys

import csv_reader.table_utils as table_util

DEFAULT_LINES_PER_PAGE = 10
sorted_ = False
sort_column = ""


def get_sorted():
    return sorted_


def get_col_to_sort():
    return sort_column


def print_page(lines, page_no, max_page):
    print(lines)
    print("Page {} of {}".format(page_no, max_page))
    print("F)irst page, P)revious page, N)ext page, L)ast page, J)ump to page S)ort E)xit")


def handle_input(page_no, last_page):
    global sorted_
    sorted_ = False
    do_exit = False
    user_input = input().lower()
    if user_input == "e":
        do_exit = True
    elif user_input == "n":
        page_no += 1
    elif user_input == "f":
        page_no = 1
    elif user_input == "p":
        page_no -= 1
    elif user_input == "l":
        page_no = last_page
    elif user_input == "j":
        page_no = __read_page_jump()
    elif user_input == "s":
        page_no = page_no
        sorted_ = True
        global sort_column
        sort_column = __read_sort_column()
    else:
        print("invalid input, try again")
    return page_no, do_exit


def prepare_start(table, lines_per_page):
    return False, 1, table_util.get_no_of_pages(table, lines_per_page)


def bound_page(page_no, last_page):
    if page_no > last_page:
        return last_page
    elif page_no < 1:
        return 1
    return page_no


def parse_args():
    args = sys.argv
    lines_page = DEFAULT_LINES_PER_PAGE
    if len(args) < 2:
        raise ValueError("You need to provide a filename")
    elif len(args) > 2:
        lines_page = int(args[2])
    return args[1], lines_page


def __read_page_jump():
    print("enter page number to jump to")
    page_num = 0
    try:
        page_num = int(input())
    except ValueError:
        print("Invalid. Number has to be an integer")
        __read_page_jump()
    return page_num


def __read_sort_column():
    print("Enter column name to sort: ")
    return input()
