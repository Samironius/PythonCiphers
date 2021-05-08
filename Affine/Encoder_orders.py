import random
import numpy as np
import DecoderOrders


def encoding():
    count = 4
    a, s, m = [[1, 1], [1, 1]], [[1], [1]], 128
    s = np.array([random.randint(0, m) for x in range(count)]).reshape(count, 1)
    text = open("text.txt", "r").read()
    while np.gcd(int(np.linalg.det(a)), m) != 1:
        a = np.array([random.choice([x for x in range(m)]) for x in range(count*count)]).reshape(count, count)
    for x in range(4 - len(text) % count):text += "x"
    x = np.array(list(map(ord, text))).reshape(count, round(len(text)/count))
    zash_matrix = (a @ x + s) % m
    encod_result = "".join(list(map(chr, [char for row in zash_matrix for char in row])))
    open("key.txt", "w").write(" ".join([str(char) for row in a for char in row]) + " " +
                               " ".join([str(char) for row in s for char in row]))
    open("encoding_result.txt", "w").write(encod_result)
    DecoderOrders.decoding()


encoding()

























while open("text.txt", "r").read() != open("decoding_result.txt", "r").read():
    encoding()