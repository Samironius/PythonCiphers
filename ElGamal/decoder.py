key = open("key", "r").read().split()
chiper = open("encoding_result", "r").read().split()
Yb, C, p, ka = int(chiper[0]), int(chiper[1], 2), int(key[0]), int(key[1])
Yka = (Yb**ka) % p
M = (Yka % p) ^ C
open("decoding_result", "w").write(str(M))