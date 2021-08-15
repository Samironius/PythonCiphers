from math import gcd
import random

m = 128
a, s = random.choice([text_of_num for text_of_num in range(m) if gcd(text_of_num, m) == 1]), random.choice([text_of_num for text_of_num in range(m)])
open("key.txt", "w").write(str(a) + " " + str(s) + " " + str(m))


def encrypt(char):
    return chr((a * ord(char) + s) % m)


open("encoding_result.txt", "w").write("".join(map(encrypt, open("text.txt", "r").read())))