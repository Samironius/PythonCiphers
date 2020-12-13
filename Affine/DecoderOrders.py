import numpy as np
import string


def gcdex(a, b):
    if b == 0:
        return 1, 0
    y, x = gcdex(b, a % b)
    return x, y - (a // b) * x


alphabet = string.ascii_lowercase
count = 4
keys = list(map(int, open("key.txt", "r").readline().split()))

a, s, m = np.array(keys[-count-1::-1][::-1]).reshape(count, count), np.array(keys[-count:]).reshape(count, 1), 128
print(a, s)
print(np.gcd(int(np.linalg.det(a)), m))
text = open("encoding_result.txt", "r").read()
det = int(np.linalg.det(a))
a1 = np.matrix.round((np.linalg.inv(a) * det * int(gcdex(det, m)[0])) % m)
s1 = (-a1 @ s) % m
x = np.array(list(map(ord, text))).reshape(len(a1), int(len(text)/count))
print(x)
zash_matrix = (a1 @ x + s1) % m
print(zash_matrix)
encod_result = "".join(list(map(chr, [round(char) for row in zash_matrix for char in row])))
open("decoding_result.txt", "w").write(encod_result)
