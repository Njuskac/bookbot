def get_num_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_characters(text):
    lowercase = text.lower()
    characters = set(lowercase)
    char_number = {}
    for character in characters:
        number = lowercase.count(character)
        char_number[character] = number
    return char_number

def sorting(count_characters):
    letters = []
    for key, value in count_characters.items():
        if key.isalpha():
            temp_dict = {"char": key, "num": value}
            letters.append(temp_dict)
    letters.sort(reverse=True, key=lambda d: d["num"])
    return letters