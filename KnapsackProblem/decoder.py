import numpy as np


def convert(a):
    l = ""
    for x in private_key[::-1]:
        if x <= a:
            a = a-x
            l += "1"
        else:
            l += "0"
    return l[::-1]


n, m = 31, 110
for x in range(m):
    if n*x%m == 1:
        n1 = x
cipher = np.array(list(map(int,open("encoding_result.txt", "r").read().split())))
private_key = np.array(list(map(int,open("private_key.txt", "r").read().split())))
open("decoding_result.txt", "w").write("".join(list(map(convert, cipher*n1%m))))