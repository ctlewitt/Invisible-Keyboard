with open("dictionary.txt", "r") as one_gram_f:
    with open("old_dictionary.txt", "r") as internet_list_f:
        with open("intersecting_words.txt", "w") as intersecting_words_f:
            one_grams = one_gram_f.readlines()
            internet_words = internet_list_f.readlines()
            for word in one_grams:
                if word in internet_words:
                    intersecting_words_f.write(word)