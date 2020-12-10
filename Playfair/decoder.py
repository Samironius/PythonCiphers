import numpy


def split_text(text):
    splited_text = [text[letter_index:letter_index+2] for letter_index in range(0, len(text), 2)]
    print(splited_text)
    return splited_text


def convert_letter_to_index(splited_text):
    index_list = []
    for bigram in splited_text:
        for letter in bigram:
            for i in range(len(key_matrix)):
                for j in range(len(key_matrix)):
                    if key_matrix[i][j] == letter:
                        index_list.append([i, j])
    print(index_list)
    return index_list


def swap_index(index_list):
    couple_of_index_letters = list(zip([x for x in index_list[::2]], [x for x in index_list[1::2]]))
    for bigram in couple_of_index_letters:
        if bigram[0][0] == bigram[1][0]:
            bigram[0][1], bigram[1][1] = bigram[0][1] - 1, bigram[1][1] - 1
        if bigram[0][1] == bigram[1][1]:
            bigram[0][0], bigram[1][0] = bigram[0][0] - 1, bigram[1][0] - 1
        else: bigram[0][1], bigram[1][1] = bigram[1][1], bigram[0][1]
    print(couple_of_index_letters)
    return couple_of_index_letters


def convert_index_to_letter(index_list):
    letter_of_values = []
    for bigram in index_list:
        letter_of_values.append(key_matrix[bigram[0][0]][bigram[0][1]])
        letter_of_values.append(key_matrix[bigram[1][0]][bigram[1][1]])
    print(letter_of_values)
    return letter_of_values


def remove_extra_letters(text):
    result_text = ""
    for x in range(0, len(text) -1):
        if text[x - 1] != text[x + 1]:
            result_text += text[x]
    if text[-1] != "x":
        result_text += text[-1]
    return result_text


key = open("matrix_key.txt", "r").read()
key_matrix = numpy.array(list(key)).reshape(5, 5)

text_for_decod = open("encoding_result.txt", "r").read()
decod = remove_extra_letters("".join(convert_index_to_letter(swap_index(convert_letter_to_index(split_text(text_for_decod))))))
open("decoding_result.txt", "w").write(decod)


pidcazka = ""