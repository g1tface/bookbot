from stats import count_words, char_count, sort_chars
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)
    chars = char_count(file_contents)
    sorted_chars = sort_chars(chars)
    print(sorted_chars)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(file_contents)} total words")
    print("--------- Character Count -------")

    for i in sorted_chars:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['value']}")

    
    print("============= END ===============")


main()