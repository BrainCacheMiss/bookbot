def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    characters = {}
    for i in text:
        character_lower = i.lower()
        if character_lower in characters:
            characters[character_lower] += 1
        else:
            characters[character_lower] = 1
    return characters

def sort_on(d):
    return d["num"]

def character_sort(characters_dict):
    char_list = []
    for key, value in characters_dict.items():
        char_dict = {"char": key, "num": value}
        char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list
