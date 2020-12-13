import random
import numpy as np
import string

alphabet = string.ascii_lowercase
count = 4
text = open("text.txt", "r").read()
while len(text) % count != 0:
    text += "x"

a, s, m = [[1, 2], [3, 4]], [[5], [6]], 128
s = np.array([random.randint(0, m) for x in range(count)]).reshape(count, 1)
print(s)
while np.gcd(int(np.linalg.det(a)), m) != 1:
    a = np.array([random.choice([x for x in range(m)]) for x in range(count*count)]).reshape(count, count)
print(a)
open("key.txt", "w").write(" ".join([str(char) for row in a for char in row]) + " " + " ".join([str(char) for row in s for char in row]))
x = np.array(list(map(ord, text))).reshape(count, round(len(text)/count))
print(x)
zash_matrix = (a @ x + s) % m
print(zash_matrix)
encod_result = "".join(list(map(chr, [char for row in zash_matrix for char in row])))

open("encoding_result.txt", "w").write(encod_result)