import re

#set up 1-gram list of lists


def get_ngram_words(file_name):
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


#def remove_extra_ngrams(file_name):
#    with open(file_name) as f:


get_ngram_words("one_gram_a.txt")

#remove_extra_ngrams("new_one_gram_a.txt")
#test_line = "A.Briggs_NOUN	1885	7	3\n"
#words = []
#ngram_info = re.match('(.+?)(_.*|)\t[0-9]*\t([0-9]*)\t[0-9]*\n', test_line)
#ngram_info_words = ngram_info.groups()
#new_word = ngram_info_words[0]
#new_word_frequency = ngram_info_words[2]
#words.append([new_word, new_word_frequency])
#print words
