import re
from operator import itemgetter

READ_FILE_NAME = "one_gram_all_lengths.txt"
WRITE_FILE_NAME = "one_gram_RZ_edit_all_lengths_sorted.txt"

#READ_FILE_NAME = "one_gram55Kthresh_a_z.txt"
#WRITE_FILE_NAME = "one_gram55thresh_frequency_sorted.txt"


WORD_INDEX = 0
FREQUENCY_INDEX = 1

#read in lines from unsorted file
with open(READ_FILE_NAME, "r") as read_f:
    lines = read_f.readlines()
    for index, line in enumerate(lines):
        #break each line into word and frequency
        line_info = re.match('(.*)\t([0-9]*)\n', line)
        line_words = line_info.groups()
        word = line_words[0]
        frequency = int(line_words[1])
        lines[index] = [word, frequency]
        #sort by freqency
        sorted_lines = sorted(lines, key=itemgetter(FREQUENCY_INDEX), reverse = True)

with open(WRITE_FILE_NAME, "w") as write_f:
    for line in sorted_lines:
        write_f.write(line[WORD_INDEX] + "\t" + str(line[FREQUENCY_INDEX]) + "\n")
