import WordCount.cli_handling as cli
import WordCount.file_handling as file
import WordCount.text_handling as txt


def get_word_count_from_text(text):
    word_list = txt.split_text(text)
    stopwords = file.read_file_to_list("stopwords.txt")
    filtered_word_list = txt.filter_words_from_list(word_list, stopwords)
    word_count = txt.count_words_in_list(filtered_word_list)
    return word_count


def main():
    text = cli.read_text()
    word_count = get_word_count_from_text(text)
    cli.print_wordcount(word_count)


if __name__ == '__main__':
    main()
