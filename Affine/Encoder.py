from math import gcd
import random

m = 128
a, s = random.choice([x for x in range(m) if gcd(x, m) == 1]), random.choice([x for x in range(m)])
open("key.txt", "w").write(str(a) + " " + str(s) + " " + str(m))


def encrypt(char):
    return chr((a * ord(char) + s) % m)


open("encoding_result.txt", "w").write("".join(map(encrypt, open("text.txt", "r").read())))