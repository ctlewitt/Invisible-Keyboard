import re

#set up 1-gram list of lists


def get_ngram_words(file_name):
#reads file in and turns into list of lists
    words = []
    with open(file_name) as f:
        for line in f:
            ngram_info = re.match('(.+?)(_.*|)\t[0-9]*\t([0-9]*)\t[0-9]*\n', line)
            ngram_info_words = ngram_info.groups()
            new_word = ngram_info_words[0]
            new_word_frequency = ngram_info_words[2]
            words.append([new_word, new_word_frequency])
    return words

#for each line of 1-gram file
    #grab word (either up to the underscore or up to the tab
    #ignore the year
    #grab the frequency count
    #ignore the volume count
    #append the mini list of word and frequency to the 1-gram list of lists


#remove duplicates, either by reprocessing the list or by getting it right the first time, using "old word" and "total count"
#update list when "old word" is not equal to "new word".  otherwise, add to total count and keep going.
#make empty no duplicates 1-gram list of lists
#for mini list in 1-gram list of lists, if

one_gram_a_words = get_ngram_words("one_gram_a.txt")
#test_line = "A.Briggs_NOUN	1885	7	3\n"
#words = []
#ngram_info = re.match('(.+?)(_.*|)\t[0-9]*\t([0-9]*)\t[0-9]*\n', test_line)
#ngram_info_words = ngram_info.groups()
#new_word = ngram_info_words[0]
#new_word_frequency = ngram_info_words[2]
#words.append([new_word, new_word_frequency])
#print words
print one_gram_a_words[0]
print one_gram_a_words[len(one_gram_a_words)-1]