import re

#download each letter's 1-gram data from Google n-grams and save each file as
#one_gram_a.txt, one_gram_b.txt, etc
#run this file on each one to combine all the word counts from each year
#for example, we want the total usage for "are" throughout all the scans,
#not a separate count for "are" in 1917 and 1918 and 1919...
#will create a new file called new_one_gram_a.txt or new_one_gram_b.txt, etc.

def combine_ngram_words(file_name):
#reads file in and turns into list of lists
    words = []
    old_word = ""
    total_frequency = 0
    with open(file_name) as f:
        with open("new_one_gram_a.txt", "w") as new_f:
            for line in f:
                ngram_info = re.match('(.+?)(_.*|)\t[0-9]*\t([0-9]*)\t[0-9]*\n', line)
                ngram_info_words = ngram_info.groups()
                new_word = ngram_info_words[0]
                new_word_frequency = int(ngram_info_words[2])
#                .*[.'|\d]+.*
                if new_word == old_word:
                    total_frequency += new_word_frequency
                    old_word = new_word
                else:
                    new_f.write(old_word + "\t" + str(total_frequency) + "\n")#write old_word \t total_frequency to new_one_gram_a.txt
                    total_frequency = new_word_frequency
                    old_word = new_word
    return

combine_ngram_words("one_gram_a.txt")