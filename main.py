from stats import get_num_words, get_character_instances, print_full_report

def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)             # string
    word_count = get_num_words(book_text)               # int
    letter_count = get_character_instances(book_text)   # dictionary

    print_full_report(path_to_book, word_count, letter_count)    

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

main()