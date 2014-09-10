KEYSTROKE_CHARACTERS = {"k1": ["a", "q", "z"], "k2": ["s", "w", "x"], "k3": ["d", "e"], "k4": ["b","c","f","g","r","t","v"], "k5": ["h","j","m","n","u","y"], "k6":["i","k"], "k7":["l","o"], "k8":["p"]}
VOWELS = ["a", "e", "i", "o", "u", "y"]


def break_into_words(keystrokes):
    words = []
    word = []
    for keystroke in keystrokes:
        if keystroke == "t1" or keystroke == "t2":
            words.append(word)
            word = []
        else:
            word.append(keystroke)
    #don't lose the last word in a sentence that doesn't have a space after it
    if word != []:
        words.append(word)
    return words


def get_possible_keystrokes(keystrokes):
    possible_keystrokes = []
    for keystroke in keystrokes:
        possible_keystrokes.append(KEYSTROKE_CHARACTERS[keystroke])
    return possible_keystrokes


def find_all_words(current_word, last_letter, possible_keystrokes, all_words):
    if last_letter == len(possible_keystrokes) - 1:
        all_words.append(current_word)
        return current_word
    else:
        next_letter = last_letter + 1
        current_words = []
        for possible_character in possible_keystrokes[next_letter]:
            current_words.append(current_word)

        for i, possible_character in enumerate(possible_keystrokes[next_letter]):
            current_words[i] += possible_character

        for i, current_word in enumerate(current_words):
            find_all_words(current_word, next_letter, possible_keystrokes, all_words)


def remove_impossible_words(all_words):
    words_with_vowels = []
    for word in all_words:
        remove = True
        if ("q" in word and "qu" in word) or "q" not in word:
            for vowel in VOWELS:
                if vowel in word:
                    words_with_vowels.append(word)
                    break
    return words_with_vowels


def get_dictionary(file_name):
#reads file in and turns into list of lists
    dictionary = []
    with open(file_name) as f:
        for line in f:
            dictionary.append(line.strip("\n"))
    return dictionary

def get_real_words(all_words, dictionary):
    real_words = []
    for word in all_words:
        if word in dictionary:
            real_words.append(word)
    return real_words


def find_next_word(keystrokes, dictionary):
    #do all the stuff that you wrote to do to a word
    #call this function repeatedly until you have done all the words
    #initialize variables
    possible_keystrokes = get_possible_keystrokes(keystrokes)
    all_words = []
    #index of starting letters and calling recursive function on each of the possible first letters
    next_letter = 0
    for first_possible_character in possible_keystrokes[next_letter]:
        find_all_words(first_possible_character, next_letter, possible_keystrokes, all_words)

    #print all possible words
#   print all_words

    #remove obviously non-English words (no vowels, "q" without "u")
    all_words = remove_impossible_words(all_words)

    #sort for easier dictionary searching
    all_words = sorted(all_words)

#    print all_words
    #read in dictionary, remove words not found in dictionary

    all_words = get_real_words(all_words, dictionary)
#    print all_words
    return all_words


dictionary = get_dictionary("dictionary.txt")
print len(dictionary)

#keystrokes = ["k3","k1","k4","t2","k4","k7","k5","k4","t2","k2","k1","k5","k1","k4","k3","t2","k5","k3","k1","k7","k2","t2","k1","t2","k3","k1","k5"]
#keystrokes = ["k6","t1","k7","k6","k6","k3","t1","k4","k4","k3","k1","k5","t1","k4","k5","k3","k3","k2","k3"]
keystrokes = ["k1"]

words = break_into_words(keystrokes)

sentence = []
for word in words:
    sentence.append(find_next_word(word, dictionary))
print sentence

