#import time
import json

def break_into_words(keystrokes):
    words = []
    word = ""
    for keystroke in keystrokes:
        if keystroke == " " or keystroke == " ": #keeping residual "double option" because it could be either thumb that hits the "keyboard"
            words.append(word)
            word = ""
        else:
            word += keystroke
    #don't lose the last word in a sentence that doesn't have a space after it
    if word != []:
        words.append(word)
    return words

def get_dictionary(file_name):
#reads in wordlist (dictionary) data structure and turns from text into data structure
    with open(file_name, "r") as read_f:
        dictionary_line = read_f.readline()
        dictionary_structure = json.loads(dictionary_line) #can install yaml and do yaml.load() instead of json.loads().  will print prettier, no unicode
        return dictionary_structure


def find_next_word(keystrokes, dictionary):
#takes keystrokes for next typed word and returns the list of possible words meant by keystroke combination
    word_length = len(keystrokes)
    if keystrokes in dictionary[word_length - 1].keys():
        possible_words = dictionary[word_length - 1][keystrokes]
    else:
        possible_words = ["NOT FOUND"]
    return possible_words

def parse_keystrokes(keystrokes):
    dictionary = get_dictionary("RZ_edit_data_structure.txt")
#    dictionary = get_dictionary("intersecting_words_data_structure.txt")
    #words_data_structure.txt is a list (separated by wordlength) of key-value pairs of keystrokes and list of possibly intended words
    #with each list sorted by frequency of use, according to Google 1-grams (see other files for how the 1-grams were pre-processed)

#    keystrokes = raw_input("type words here: (q to quit) ")
    words = break_into_words(keystrokes)

    sentence = []
    for word in words:
        sentence.append(find_next_word(word, dictionary))
    return sentence