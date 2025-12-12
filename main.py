import sys
from stats import number_of_words, dict_of_char_counts, sort_dict

def get_book_test(file_path):
    with open(file_path) as f:
        content = f.read()
    return content

def print_report(file_path, num_words, dict_counts):
    sorted_counts = sort_dict(dict_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count --------")
    for char, count in sorted_counts.items():
        print(f"{char}: {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    test_book = get_book_test(book_path)
    num_words = number_of_words(test_book)
    print(f"Found {num_words} total words")
    char_counts = dict_of_char_counts(test_book)
    print_report("./books/frankenstein.txt", num_words, char_counts)