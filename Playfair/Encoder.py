import string
import numpy


def form_key_matrix(word):
    unique =""
    for x in word:
        if x not in unique:
            unique += x
    alphabet = list(string.ascii_lowercase)
    for x in unique:alphabet.remove(x)
    alphabet.remove("j")
    key_list = list(unique + "".join(alphabet))
    key_matrix = numpy.array(key_list).reshape(5, 5)
    print(key_matrix)
    return key_matrix


def split_text(text):
    text = text.lower().replace(" ", "")
    text2 = ""
    for x in text:
        if x.isalpha():
            text2 += x
    print(text2)
    for x in range(1, len(text2)):
        if text2[x] == text2[x - 1]:
            text2 = text2[0:x] + "x" + text2[x:]
    if len(text2) % 2 != 0: text2 += "x"
    splited_text = [text2[letter_index:letter_index + 2] for letter_index in range(0, len(text2), 2)]
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
            bigram[0][1], bigram[1][1] = bigram[1][1] + crutch(bigram[1][1]), bigram[0][1] + crutch(bigram[0][1])
        if bigram[0][1] == bigram[1][1]:
            bigram[0][0], bigram[1][0] = bigram[0][0] + crutch(bigram[0][0]), bigram[1][0] + crutch(bigram[1][0])
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


def crutch(count):
    if count < 4:
        return 1
    else:
        return -4


key_matrix = form_key_matrix("samire")
open("matrix_key.txt", "w").write("".join(letter for row in key_matrix for letter in row))

text = open("text.txt", "r").read()
encod = "".join(convert_index_to_letter(swap_index(convert_letter_to_index(split_text(text)))))
open("encoding_result.txt", "w").write(encod)