import re

with open("one_gram55thresh_frequency_sorted.txt", "r") as one_grams_f:
    word_list = []
    for i in range(30):
        word_list.append([])
    for line in one_grams_f:
        word_info = re.match('(.*)\t[0-9]*\n', line)
        word_info_words = word_info.groups()
        word = word_info_words[0]
        word_len = len(word)
        word_list[word_len-1].append(line)
    for num in range(1, 30):
        file_name = "one_gram_len_" + str(num) + ".txt"
        pseudo_file_name = "len_" + str(num) + ".txt"
        with open(file_name, "w") as pseudo_file_name:
            for word_in_list in word_list[num-1]:
                pseudo_file_name.write(word_in_list)