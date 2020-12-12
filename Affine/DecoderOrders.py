import numpy as np
import string

alphabet = string.ascii_lowercase


def conwertor(a = str):
    if str(a).isalpha():
        return alphabet.index(a)
    if str(a).isnumeric():
        return alphabet[int(a)]


def gcdex(a, b):
    if b == 0:
        return 1, 0
    y, x = gcdex(b, a % b)
    return x, y - (a // b) * x

count = 2
a, s, m = [[25, 20], [3, 24]], [[5], [6]], len(alphabet)
text = open("encoding_result.txt", "r").read()
det = int(np.linalg.det(a))

# x, m = [[10, 4, 23,], [32, 25, 27]], 33
a1 = np.array(np.array([round(char) for row in ((np.linalg.inv(a) * det * int(gcdex(det, m)[0])) % m) for char in row]).reshape(count,count))
s1 = np.array([round(char) for row in ((-a1 @ s) % m) for char in row])
x = list(map(conwertor, text))

x = [list(row) for row in np.array(x).reshape(count, len(text)/count)]
zash_matrix = (np.array(a1).dot(x) + s1) % m



print([round(char) for row in zash_matrix for char in row])

encod_result = "".join(list(map(conwertor, [round(char) for row in zash_matrix for char in row])))
open("decoding_result.txt", "w").write(encod_result)

enc = [[[115,  97, 109],
        [105, 114, 120]],
[[74,  74,  98],
[3, 113,  45]]]

dec = [[[74,  74,  98],
       [3, 113,  45]],
[[102,  66,  90],
[82, 100, 112]]
]