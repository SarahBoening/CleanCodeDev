def count_for_files(files: list):
    loc_count_total = 0
    line_count_total = 0
    results = []
    for file in files:
        file_loc_count, file_total_count = count_loc(file[1])
        results.append([file[0], file_loc_count, file_total_count])
        loc_count_total += file_loc_count
        line_count_total += file_total_count
    return results, loc_count_total, line_count_total


def count_loc(code: str):
    loc_count = 0
    total_line_count = 0
    lines = split_code_file(code)
    for line in lines:
        if is_loc(line):
            loc_count += 1
        total_line_count += 1
    return loc_count, total_line_count


def split_code_file(text: str):
    return [line for line in text.split("\n")]


def is_loc(line: str):
    line = line.strip()
    return line != "" and not line.startswith("#")
