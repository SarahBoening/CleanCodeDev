
def wrap(text: str, max_width: int) -> str:
    new_text = split_text(text)
    rows = build_rows(new_text, max_width)
    wrapped_text = build_text(rows)
    return wrapped_text


def split_text(text: str) -> list:
    return text.split()


def build_rows(words: list, max_width: int) -> list:
    rows = []
    row = ""
    for word in words:
        if len(row) == 0:
            row = word
        else:
            new_line = row + " " + word
            if len(new_line) > max_width:
                rows.append(row)
                row = word
                if len(word) > max_width:
                    part_1 = word[:max_width]
                    part_2 = word[max_width:]
                    rows.append(part_1)
                    row = part_2
            else:
                row = new_line
    return rows


def build_text(rows: list) -> str:
    return "\n".join(rows)
