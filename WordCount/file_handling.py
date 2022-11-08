def read_file_to_list(filename):
    lines = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]
    except IOError:
        print("Error reading file, using empty list")
    return lines
