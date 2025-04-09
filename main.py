from stats import * 
import sys


def main():
    if len(sys.argv) < 2:
        raise "Usage: python3 main.py <path_to_book>"

    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    letter_count = dict_to_list(count_of_letters(text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for letter in letter_count:
        if letter["char"].isalpha():
            print(f"{letter['char']}: {letter['count']}")


def get_book_text(book_path):
    with open(book_path) as target:
        return target.read()
    

main()
