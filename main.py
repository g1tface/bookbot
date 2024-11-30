def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = get_word_count(file_contents)
        character_count = get_character_count(file_contents)
        character_count = [{'key': k, 'value': v} for k, v in character_count.items()]
        character_count = sorted(character_count, key=sort_on, reverse=True)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document \n")
        for dict in character_count:
            print(f"The '{dict["key"]}' character was found {dict["value"]} times")
        print("--- End report ---")

def get_word_count(text):
    words = text.split()
    count = 0
    for word in words:
        count+=1
    return count

def get_character_count(text):
    words = text.lower().split()
    letter_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    for word in words:
        letters = list(word)
        for letter in letters:
            if letter in letter_dict:
                letter_dict[letter] += 1
    return letter_dict

main()
