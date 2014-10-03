import json
import re

READ_FILE_NAME = "one_gram_RZ_edit_all_lengths_sorted.txt"
WRITE_FILE_NAME = "RZ_edit_data_structure.txt"

#READ_FILE_NAME = "intersecting_words.txt"
#WRITE_FILE_NAME = "intersecting_words_data_structure.txt"

#READ_FILE_NAME = "dictionary.txt"
#WRITE_FILE_NAME = "words_data_structure.txt"

#READ_FILE_NAME = "test_dictionary.txt"
#WRITE_FILE_NAME = "test_words_data_structure.txt"


KEYSTROKE_CHARACTERS = {"a": ["a", "q", "z"], "s": ["s", "w", "x"], "d": ["c", "d", "e"], "f": ["b","f","g","r","t","v"], "j": ["h","j","m","n","u","y"], "k":["i","k"], "l":["l","o"], ";":["p"]}

def get_character_keystrokes(KEYSTROKE_CHARACTERS):
    character_keystrokes = {}
    for keystroke in KEYSTROKE_CHARACTERS.keys():
        for letter in KEYSTROKE_CHARACTERS[keystroke]:
            character_keystrokes[letter] = keystroke
    return character_keystrokes

def get_max_word_length():
    max_word_length = 0
    first = True
    with open(READ_FILE_NAME) as read_f:
        for line in read_f:
            if len(line) > max_word_length:
                max_word_length = len(line)

    max_word_length -= 1 #line length includes new line character in each line, so subtract 1
    return max_word_length

def create_empty_data_struct(list_len):
    empty_list = []
    for i in range(list_len):
        empty_list.append({})
    return empty_list


max_word_len = get_max_word_length()
sorted_words = create_empty_data_struct(max_word_len)

#create dictionary of letter:keystroke relationships
character_keystrokes = get_character_keystrokes(KEYSTROKE_CHARACTERS)

with open(READ_FILE_NAME) as read_f:
    for line in read_f:
        #get word in line
#        line_info = re.match('(.*)\n', line)
        line_info = re.match('(.*)\t[0-9]*\n', line)
        line_words = line_info.groups()
        word = line_words[0]
        #find keystrokes that make word
        word_keystrokes = ""
        for letter in word:
            word_keystrokes += character_keystrokes[letter]
        #add word to sorted_words data structure
        index = len(word) - 1
        if word_keystrokes in sorted_words[index].keys():
            sorted_words[index][word_keystrokes].append(word)
        else:
            sorted_words[index][word_keystrokes] = [word]

#record organized word list once created
with open(WRITE_FILE_NAME, "w") as write_f:
    write_f.write(json.dumps(sorted_words))