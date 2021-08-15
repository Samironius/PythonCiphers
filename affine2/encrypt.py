import numpy as np
import random

#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']

n = len(alphabet)
text = "місто Львів"
k = 3


def b_matrix(text, k):
    b = []
    text = text.replace(" ", "")
    while len(text) % k != 0:
        text += "а"

    start = 0
    for index_array in range(k, len(text) + 1, k):
        segment = []
        for index in range(start, index_array):
            segment.append(alphabet.index(text[index].lower()))
        start = index_array
        b.append(segment)

    return b


def a_matrix_and_s(k):

    def a_matrix(k):
        a = []
        for matrix_row_count in range(k):
            segment = []
            for index in range(k):
                segment.append(random.randint(0, n))
            a.append(segment)

        return a

    a = a_matrix(k)
    determinant = round(np.linalg.det(a)) % n

    while np.gcd(determinant, n) != 1:
        a = a_matrix(k)

    s_key_file = open("s_key.txt", "a")
    s_key = []
    for x in range(k):
        s_key.append(random.randint(0, n))
    s_key_file.write(str(s_key) + "\n")
    s_key_file.close()
    return a, s_key


def replace_letter(a_and_s, b):

    key = open("key.txt", "a")
    for matrix_row in a_and_s[0]:
        key.write(str(matrix_row) + "\n")
    key.close()
    result = []
    for i in b:
        result.append(np.dot(a_and_s[0], i))

    result = np.transpose(result)

    replaced_k_gram_matrix = []
    for i, s_item in zip(result, a_and_s[1]):
        row_list = []
        for r in i:
            row_list.append((r + s_item) % n)
        replaced_k_gram_matrix.append(row_list)

    encrypted_text = open("encrypted_text.txt", "a")
    for matrix_row in replaced_k_gram_matrix:
        encrypted_text.write(str(matrix_row) + "\n")
    encrypted_text.close()

    text_result = ""
    replaced_k_gram_matrix = np.transpose(replaced_k_gram_matrix)
    for matrix_row in replaced_k_gram_matrix:
        for x in matrix_row:
            text_result += alphabet[x]

    return text_result


print(replace_letter(a_matrix_and_s(k), b_matrix(text, k)))
