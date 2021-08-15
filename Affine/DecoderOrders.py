import numpy as np

def gcdex(a, b):
    if b == 0:
        return a, 1, 0
    d, y, x = gcdex(b, a % b)
    return d, x, y - (a // b) * x


def decoding():
    count = 4
    keys = list(map(int, open("key.txt", "r").readline().split()))
    a, m = np.array(keys[-count-1::-1][::-1]).reshape(count, count), 128
    s = np.array(keys[-count:]).reshape(count, 1)
    text = open("encoding_result.txt", "r").read()
    det1 = int(np.linalg.det(a))
    ob_det = int(gcdex(det1, m)[1])
    print(ob_det)
    if ob_det < 0: ob_det = ob_det + m
    print(ob_det)
    print(a)
    a1 = np.matrix.round((np.linalg.inv(a) * det1 * ob_det) % m)
    print(a1)
    s1 = (-a1 @ s) % m
    print(s1)
    text_of_num = np.array(list(map(ord, text))).reshape(len(a1), int(len(text) / count))
    zash_matrix = (a1 @ text_of_num + s1) % m
    decoded_result = "".join(
        list(map(chr, [round(char) for row in zash_matrix for char in row])))
    open("decoding_result.txt", "w").write(decoded_result.strip("x"))

decoding()
