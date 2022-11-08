def print_loc(result_list, loc_count, line_count):
    for file in result_list:
        print("{}, {}, {}".format(file[0], file[1], file[2]))
    print("Total:\nLOC: {}\nLines: {}".format(loc_count, line_count))
