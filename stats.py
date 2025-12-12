def number_of_words(book_contents):
    total_words = len(book_contents.split())
    return total_words

def number_of_a_specific_char(book_contents, character):
    total_char = book_contents.lower().count(character.lower())
    return total_char

def dict_of_char_counts(book_contents):
    char_count = {}
    for char in book_contents:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in char_count:
                char_count[char_lower] += 1
            else:
                char_count[char_lower] = 1
        elif char.isspace():
            continue
        else:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_dict(char_count_dict, descending=True):
    sorted_char_counts = dict(sorted(char_count_dict.items(), key=lambda item: item[1], reverse=descending))
    return sorted_char_counts