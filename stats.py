def get_num_words(text):
    words = text.split()
    return len(words)

def count_of_letters(text):
    text = text.lower()
    counted_letters = {}

    for letter in text:
        if letter not in counted_letters:
            counted_letters[letter] = 1
        else: 
             counted_letters[letter] += 1
    return counted_letters

def sort_on(dict):
    return dict["count"]
    
def dict_to_list(dict):
    list = []
    for char, count in dict.items():
        element = {
                "char": char,
                "count": count
                }
        list.append(element)
    list.sort(key=lambda x: (-x["count"]))
    return list
