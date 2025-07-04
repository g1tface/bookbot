from stats import count_words, char_count, sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    file_contents = get_book_text("books/frankenstein.txt")
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