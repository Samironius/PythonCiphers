import numpy as np


def encoding():
    count = 4
    global a
    a, m = [[1, 1], [1, 1]], 128
    s = np.random.randint(m, size=(count, 1))

    text = open("text.txt", "r").read()
    for text_of_num in range(4 - len(text) % count): text += "x"
    while np.gcd(int(np.linalg.det(a)), m) != 1:
        a = np.random.randint(m, size=(count, count))
    text_of_num = np.array(list(map(ord, text))).reshape(count, round(len(text) / count))
    zash_matrix = (a @ text_of_num + s) % m
    encod_result = "".join(list(map(chr, [char for row in zash_matrix for char in row])))
    open("key.txt", "w").write(" ".join([str(char) for row in a for char in row])+ " " + " ".join(list(map(str,map(int, s)))))
    open("encoding_result.txt", "w").write(encod_result)




encoding()

