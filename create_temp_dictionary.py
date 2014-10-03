import re

READ_FILE_NAME = "one_gram55thresh_frequency_sorted.txt"
WRITE_FILE_NAME = "dictionary.txt"

with open(READ_FILE_NAME, "r") as read_f:
    with open(WRITE_FILE_NAME, "w") as write_f:
        for line in read_f:
            line_info = re.match('(.*)\t[0-9]*\n', line)
            line_words = line_info.groups()
            word = line_words[0]
            write_f.write(word + "\n")