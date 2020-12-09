def gcdex(a, b):
    if b == 0:
        return 1, 0
    y, x = gcdex(b, a % b)
    return x, y - (a // b) * x


def decrypt(char):
    return chr((a1 * ord(char) + s1) % m)


a, s, m = map(int, open("key.txt", "r").read().split())
a1 = gcdex(a, m)[0]
s1 = (-a1 * s) % m


open("decoding_result.txt", "w").write("".join(map(decrypt, open("encoding_result.txt", "r").read())))