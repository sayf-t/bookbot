def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for char in text:
        lower_char = char.lower()
        letters[lower_char] = letters.get(lower_char, 0) + 1
    return letters
        
def sort_letters(letters):
    # return a lists of dictionaries, each dictionary contains 2 key-value pairs: one for the character and one for the count
    # create a list of dictionaries
    list = []
    for char, count in letters.items():
        list.append({"char": char, "count": count})

    # sort the list from greatest to least by the count
    list.sort(reverse=True,key=sort_on_count)
    return list

def sort_on_count(dict):
    return dict["count"]