import string

READ_LETTER_FILE_NAME_START = "combined_one_gram_"
WRITE_LETTER_FILE_NAME = "one_gram_a_z.txt"

READ_LEN_FILE_NAME_START = "one_grams_by_length_RZ_edit/one_gram_len_"
WRITE_LEN_FILE_NAME = "one_gram_all_lengths.txt"

def combine_letter_files():
    with open(WRITE_LETTER_FILE_NAME, "a") as write_f:
        for letter in string.lowercase:
            read_file_name = READ_LETTER_FILE_NAME_START + letter + ".txt"
            with open(read_file_name, "r") as read_f:
                for line in read_f:
                    write_f.write(line)


def combine_word_len_files():
    with open(WRITE_LEN_FILE_NAME, "w") as write_f:
        for num in range(1, 25):
            read_file_name = READ_LEN_FILE_NAME_START + str(num) + ".txt"
            with open(read_file_name, "r") as read_f:
                for line in read_f:
                    write_f.write(line)

combine_word_len_files()
