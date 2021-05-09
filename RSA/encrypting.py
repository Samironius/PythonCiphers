import random


def gcdex(a, b):
    if b == 0:
        return a, 1, 0
    d, y, x = gcdex(b, a % b)
    return d, x, y - (a // b) * x


def encrypting(letter):
    return str((letter ** public_key_e) % public_key_n)


p, q = 3, 13
el = (p - 1) * (q - 1)
public_key_n = p * q
public_key_e = random.choice([x for x in range(0, el) if gcdex(el, x)[0] == 1])
private_key = gcdex(el, public_key_e)[2] % el
open("encrypted.txt", "w").write(" ".join(list(map(encrypting, list(map(int, open("text.txt", "r").read()))))))
open("public_key.txt", "w").write("%s %s" % (str(public_key_e), str(public_key_n)))
open("private_key.txt", "w").write(str(private_key))