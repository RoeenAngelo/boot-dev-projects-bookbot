from stats import get_num_words, get_num_letters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_num_letters(text)
    print(f"Found {num_words} total words")
    print(char_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()