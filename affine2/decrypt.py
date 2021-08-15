import numpy as np
#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']

n = len(alphabet)


def convert(matrix):
    result = []
    for i in matrix:
        if matrix.index(i) != len(matrix) - 1:
            i = i[0: len(i) - 1]
        i = eval(i)
        result.append(i)

    return result


key = open("key.txt", "r").readlines()

key = convert(key)
# key = [[ 34,  17, 101,  42,],
#  [ 18, 117,  42,  19],
#  [ 16,  55,  81, 117,],
#  [127,  76, 112,  24]]
print(key)

determinant = round(np.linalg.det(key))

encrypted_text = open("encrypted_text.txt", "r").readlines()
encrypted_text = convert(encrypted_text)


def evklid(a, b):
    r1 = a
    r2 = b
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    r = r1 % r2
    while r != 0:
        q = r1 // r2
        s = s1 - q * s2
        t = t1 - q * t2
        r1 = r2
        r2 = r
        s1 = s2
        s2 = s
        t1 = t2
        t2 = t
        r = r1 % r2
    return r2, t2, s2


func = evklid(determinant, n)  # w n
inverse_matrix = np.linalg.inv(key)


matrix = []
for i in inverse_matrix:
    matrix_row = []
    for x in i:
        matrix_row.append(round(x * func[2] * determinant) % n)
    matrix.append(matrix_row)

print(matrix)

s_key = open("s_key.txt", "r").readlines()

s_key = convert(s_key)

s_key = s_key[0]

s_key = np.transpose(s_key)
# s_key = [[92],
#  [36],
#  [53],
#  [37]]
S = np.dot(-np.array(matrix), np.array(s_key))
s = []
for i in S:
    s.append(i % n)

decrypted_text = np.dot(matrix, encrypted_text)

matrix_index_with_s = []

for i, s_item in zip(decrypted_text, s):
    row_list = []
    for r in i:
        row_list.append((r + s_item) % n)
    matrix_index_with_s.append(row_list)

decrypted_text_string = ""
for i in np.transpose(matrix_index_with_s):
    for x in i:
        decrypted_text_string += alphabet[x]

print(decrypted_text_string)
