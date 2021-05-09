import numpy as np
from math import gcd


def decoding():
    count = 4
    keys = list(map(int, open("key.txt", "r").readline().split()))
    a, s, m = np.array(keys[-count-1::-1][::-1]).reshape(count, count), np.array(keys[-count:]).reshape(count, 1), 128
    text = open("encoding_result.txt", "r").read()
    det = int(np.linalg.det(a))
    a1 = np.matrix.round((np.linalg.inv(a) * det * int(gcd(det, m))) % m)
    s1 = (-a1 @ s) % m
    x = np.array(list(map(ord, text))).reshape(len(a1), int(len(text)/count))
    zash_matrix = (a1 @ x + s1) % m
    decoded_result = "".join(list(map(chr, [round(char) for row in zash_matrix for char in row])))
    open("decoding_result.txt", "w").write(decoded_result.strip("x"))