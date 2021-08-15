import random


def gcdex(a, b):
    if b == 0:
        return a, 1, 0
    d, y, x = gcdex(b, a % b)
    return d, x, y - (a // b) * x


def encrypting(letter):
    return str((int(letter) ** public_key_e) % public_key_n)


p, q = 11, 47
el = (p - 1) * (q - 1)
public_key_n = p * q
# public_key_n = 517
public_key_e = random.choice([text_of_num for text_of_num in range(1, el) if gcdex(el, text_of_num)[0] == 1])
print([text_of_num for text_of_num in range(1, el) if gcdex(el, text_of_num)[0] == 1])
# public_key_e = 3
private_key = gcdex(el, public_key_e)[2] % el
text_of_num = "".join(list(map(str, map(ord, open("text", "r").read()))))
text_of_num = "100"
print(" ".join(list(map(encrypting, text_of_num))))
open("encrypted", "w").write(" ".join(list(map(encrypting, text_of_num))))
open("public_key", "w").write("%s %s" % (str(public_key_e), str(public_key_n)))
open("private_key", "w").write(str(private_key))