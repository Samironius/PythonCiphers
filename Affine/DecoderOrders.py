import numpy as np

alphabet = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']


def conwertor(a = str):
    print(a, "S")
    if a.isalpha():
        print(a, "S")
        return alphabet.index(a)
    if a.isnumeric():
        print(a, "S")
        return alphabet[a]


def gcdex(a, b):
    if b == 0:
        return 1, 0
    y, x = gcdex(b, a % b)
    return x, y - (a // b) * x


a, s, m = [[1, 2], [3, 4]], [[5], [6]], 33
text = open("encoding_result.txt", "r", encoding='utf-8').read()
ss =list(map(conwertor, text))
print(ss)
det = int(np.linalg.det(a))
a1 = (np.linalg.inv(a) * det * int(gcdex(det, m)[0])) % m
s1 = (-a1 @ s) % m
x = np.array(list(map(conwertor, text))).reshape(len(a1), int(len(text)/2))
print(x,"ss")
# x = [[10, 4, 23,], [32, 25, 27]]

zash_matrix = (a1 @ x + s1) % m
print(zash_matrix)


encod_result = "".join(list(map(conwertor, [int(char) for row in zash_matrix for char in row])))
open("decoding_result.txt", "w", encoding='utf-8').write(encod_result)

enc = [[[115,  97, 109],
        [105, 114, 120]],
[[74,  74,  98],
[3, 113,  45]]]

dec = [[[74,  74,  98],
       [3, 113,  45]],
[[102,  66,  90],
[82, 100, 112]]
]