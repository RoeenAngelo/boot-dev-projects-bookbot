from stats import get_num_words, get_num_letters, chars_dict_to_sorted_list, sys



def main():
    if sys.argv.__len__() != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_num_letters(text)
    sorted_char_count_list = chars_dict_to_sorted_list(char_count)
    print_report(book_path, num_words, sorted_char_count_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, sorted_char_count_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count --------")
    for item in sorted_char_count_list:
        char = item["char"]
        count = item["num"]
        print(f"{char}: {count}")
    print("============= END ===============")

main()