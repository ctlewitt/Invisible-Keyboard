import re
import string

actual_letter_frequency = {"a":"11.602%", "b":"4.702%", "c":"3.511%", "d":"2.670%", "e":"2.007%", "f":"3.779%", "g":"1.950%", "h":"7.232%", "i":"6.286%", "j":".597%", "k":".590%", "l":"2.705%", "m":"4.374%", "n":"2.365%", "o":"6.264%", "p":"2.545%", "q":".173%", "r":"1.653%", "s":"7.755%", "t":"16.671%", "u":"1.487%", "v":".649%", "w":"6.753%", "x":".017%", "y":"1.620%", "z":".034%"}
#data from: http://en.wikipedia.org/wiki/Letter_frequency#Relative_frequencies_of_the_first_letters_of_a_word_in_the_English_language
LETTER = 0
COUNT = 1
#letter_count is a list of lists [letter, count]

def check_each_word(all_letters_file_write, one_letter_file_read):
#get number of lines/words
#get min frequency
#get max frequency
#get total number count
#get average count per word
    num_words = 0
    min_frequency = 100000
    max_frequency = 0
    total_frequency = 0

    with open(one_letter_file_read) as f_read:
        for line in f_read:
            #get word frequency
            ###CHECK THIS REGULAR EXPRESSION###
            word_frequency_info = re.match('.*\t([0-9]*)\n', line)
            word_frequency_words = word_frequency_info.groups()
            word_frequency = int(word_frequency_words[0])

            #set stats
            num_words += 1
            total_frequency += word_frequency
            if min_frequency > word_frequency:
                min_frequency = word_frequency
            if max_frequency < word_frequency:
                max_frequency = word_frequency
    average_frequency = total_frequency / num_words

        #print results
    all_letters_file_write.write("num_words: " + str(num_words) + "\n")
    all_letters_file_write.write("min_frequency: " + str(min_frequency) + "\n")
    all_letters_file_write.write("max_frequency: " + str(max_frequency) + "\n")
    all_letters_file_write.write("total_frequency: " + str(total_frequency) + "\n")
    all_letters_file_write.write("average_frequency: " + str(average_frequency) + "\n")

    return num_words, total_frequency


def get_file_name(letter):
    return "combined_one_gram_55Kthresh_" + letter + ".txt"


letter_count = []
total_words = 0
sum_total_frequency = 0

#go through each 1-gram letter's file and collect stats on the word counts for each one
with open("combined_one_gram_55Kthresh_stats.txt", "w") as n_gram_stats:
    n_gram_stats.write("Stats on words starting with each letter\n")
    for letter in string.lowercase:
        n_gram_stats.write(letter + ":\n")
        num_words, frequency = check_each_word(n_gram_stats, get_file_name(letter)) #checks new_one_gram_[letter].txt data
        n_gram_stats.write("\n")
        letter_count.append([letter, num_words])
        total_words += num_words
        sum_total_frequency += frequency

    total_words += 0.0 #turn into double for future calculations.  sort of a hack....  :(

    #record percent stats to each letter's 1-gram data.  (ie, What percentage of the total words begin with this letter?)
    n_gram_stats.write("\n\n\n")
    n_gram_stats.write("AGGREGATE RESULTS:\n")
    for letter_stat in letter_count:
        n_gram_stats.write(letter_stat[LETTER] + ":\n")
        n_gram_stats.write("    count: " + str(letter_stat[COUNT]) + "\n")
        n_gram_stats.write("    prcnt: " + str(letter_stat[COUNT]*100/total_words) + "%\n")
        n_gram_stats.write("    want:  " + str(actual_letter_frequency[letter_stat[LETTER]]) + "\n")

    n_gram_stats.write("\n\n")
    n_gram_stats.write("Total Word Count: " + str(total_words) + "\n")
    n_gram_stats.write("Average Frequency: " + str(sum_total_frequency/total_words) + "\n")