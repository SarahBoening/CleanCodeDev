import re


def split_text(text):
    return [word.strip() for word in text.split(" ")]


def count_words_in_list(text):
    count = 0
    for word in text:
        if re.match(r"^[a-zA-Z]+$", word):
            count += 1
    return count


def filter_words_from_list(text, filter_list):
    return [word for word in text if word not in filter_list]
