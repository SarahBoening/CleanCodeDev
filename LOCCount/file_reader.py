import os


def list_py_files_from_directory(directory):
    all_py_files = []
    try:
        for root, dirs, files in os.walk(directory):
            for filename in files:
                if filename.endswith(".py"):
                    all_py_files.append(os.path.join(root, filename))
    except IOError:
        print("Error reading directory {}".format(directory))
    return all_py_files


def read_py_files_to_list(files):
    py_files = []
    for file in files:
        try:
            with open(file, 'r', encoding="utf-8", errors="replace") as f:
                py_files.append([file, f.read()])
        except IOError:
            print("Error reading file {}, skipping this file...".format(file))
    return py_files
