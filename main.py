import sys
from stats import count_words, count_chars, prepare_dict_for_printing, print_report

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def handle_stdin():
    args = sys.argv[1:]

    if len(args) == 0:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return args[0]

def main():
    filepath = handle_stdin()
    text = get_book_text(filepath)
    chars_dict = count_chars(text)
    print_report(count_words(text), prepare_dict_for_printing(chars_dict))

main()