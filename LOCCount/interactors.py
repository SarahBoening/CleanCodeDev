import LOCCount.args_parse as argsp
import LOCCount.file_reader as fr
import LOCCount.LOC_count as loc
import LOCCount.ui as ui


def start(args):
    """
    Start interaction.
    Reads the directory from sys.args, counts the number of lines and prints the results.
    This is the only interaction, thus everything is handled in here.

    :param args: sys.args
    :return:
    """
    directory = argsp.read_file(args)
    py_files = fr.list_py_files_from_directory(directory)
    py_files = fr.read_py_files_to_list(py_files)
    locs_per_files, total_loc, total_lines = loc.count_for_files(py_files)
    ui.print_loc(locs_per_files, total_loc, total_lines)
