from stats import count_words as get_num_words, count_letters, sort_letters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        filecontents = f.read()
    return filecontents

def main():
    # print("sys.argv", sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python main.py <filepath>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = get_num_words(book_text)
    print("============ BOOKBOT =============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    letter_counts = count_letters(book_text)
    print("----------- Character Count ----------")
    sorted_letters = sort_letters(letter_counts)
    for letter in sorted_letters:
        if letter["char"].isalpha():
            print(f"{letter['char']}: {letter['count']}")
main()
