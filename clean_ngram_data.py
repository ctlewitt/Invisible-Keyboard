import re
import string

WORD_INDEX = 0
FREQUENCY_INDEX = 1

def remove_junk(read_file, write_file):
#remove ., ', and numbers from end of words.  If there are remaining punctuation in the words, remove them.
# Otherwise, add word&frequency to write_file
    with open(read_file, "r") as read_f:
        with open (write_file, "w") as write_f:
            for line in read_f:
                ngram_info = re.match('(.*)\t([0-9]*)\n', line)
                ngram_info_words = ngram_info.groups()
                ngram_word = ngram_info_words[0]
                ngram_frequency = ngram_info_words[1]
                for count in range(2):
                    ngram_word_info = re.match('(.+?)\'?\.?[0-9]*$', ngram_word)
                    ngram_word_words = ngram_word_info.groups()
                    ngram_word = ngram_word_words[0]
                if ngram_word.isalpha():
                    write_f.write(ngram_word.lower() + "\t" + ngram_frequency + "\n")
    return

def combine_words(read_file, write_file):
#sort words in list, combine identical words' frequencies, and write to file
    with open(read_file, "r") as read_f:
        lines = read_f.readlines()
        lines.sort()
        combined_lines = []
        combined_lines_index = 0
        for line in lines:
            #break each line into word and frequency
            line_info = re.match('(.*)\t([0-9]*)\n', line)
            line_words = line_info.groups()
            word = line_words[0]
            frequency = int(line_words[1])
            if len(combined_lines) == 0:
                combined_lines.append([word, frequency])
            else:
                if word == combined_lines[combined_lines_index][WORD_INDEX]:
                    combined_lines[combined_lines_index][FREQUENCY_INDEX] += frequency
                else:
                    combined_lines.append([word, frequency])
                    combined_lines_index += 1
    with open(write_file, "w") as write_f:
        for line in combined_lines:
            write_f.write(line[WORD_INDEX] + "\t" + str(line[FREQUENCY_INDEX]) + "\n")
    return

for letter in string.lowercase:
    read_file_name = "new_one_gram_" + letter + ".txt"
    write1_file_name = "clean_one_gram_" + letter + ".txt"
    remove_junk(read_file_name, write1_file_name)
    write2_file_name = "combined_one_gram_" + letter + ".txt"
    combine_words(write1_file_name, write2_file_name)