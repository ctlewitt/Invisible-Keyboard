import string
import re

THRESHOLD = 55000


def remove_low_count_words(read_file, write_file):
#checks each word's frequency.  if higher than THRESHOLD, adds word to new file.  otherwise, not included
    with open(read_file, "r") as read_f:
        with open(write_file, "w") as write_f:
            for line in read_f:
                ngram_info = re.match('.*\t([0-9]*)\n', line)
                ngram_info_words = ngram_info.groups()
                ngram_frequency = int(ngram_info_words[0])
                if ngram_frequency >= THRESHOLD:
                    write_f.write(line)
    return


for letter in string.lowercase:
    #set file names based on letters
    read_file_name = "combined_one_gram_" + letter + ".txt"
    write_file_name = "combined_one_gram_55Kthresh_" + letter + ".txt"
    #remove 1-gram words that don't have high enough frequencies
    remove_low_count_words(read_file_name, write_file_name)


