#from separate_one_grams_into_datastructure import get_character_keystrokes

KEYSTROKE_CHARACTERS = {"a": ["a", "q", "z"], "s": ["s", "w", "x"], "d": ["d", "e"], "f": ["b","c","f","g","r","t","v"], "j": ["h","j","m","n","u","y"], "k":["i","k"], "l":["l","o"], ";":["p"]}


def get_character_keystrokes(KEYSTROKE_CHARACTERS):
    character_keystrokes = {}
    for keystroke in KEYSTROKE_CHARACTERS.keys():
        for letter in KEYSTROKE_CHARACTERS[keystroke]:
            character_keystrokes[letter] = keystroke
    return character_keystrokes

character_keystrokes = get_character_keystrokes(KEYSTROKE_CHARACTERS)
word = "qwertyuiop"
word_keystrokes = ""
for letter in word:
    word_keystrokes += character_keystrokes[letter]
print word_keystrokes