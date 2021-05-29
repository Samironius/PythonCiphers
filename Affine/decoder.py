from egcd import egcd


def decrypt(char):
    return chr((a1 * ord(char) + s1) % m)


def encrypt(char):
    return chr((a * ord(char) + s) % m)


a, s, m = map(int, open("key.txt", "r").read().split())
a1 = egcd(a, m)[1]
s1 = (-a1 * s) % m

open("encoding_result.txt", "w").write("".join(map(encrypt, open("text.txt", "r").read())))
open("decoding_result.txt", "w").write("".join(map(decrypt, open("encoding_result.txt", "r").read())))