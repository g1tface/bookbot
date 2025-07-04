def count_words(contents):
    num_words = 0
    for word in contents.split():
        num_words += 1
    return num_words

def char_count(contents):
    characters = {}
    for ch in contents:
        ch = ch.lower()
        if ch not in characters:
            characters[ch] = 1
        else:
            characters[ch] += 1
    return characters

def sort_chars(char_dict):
    def sort_on(items):
        return items["value"]
    list_of_dicts = []
    for k, v in char_dict.items():
        list_of_dicts.append({"char": k, "value": v})
    
    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts
