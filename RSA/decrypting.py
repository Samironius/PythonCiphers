def decrypting(letter):
    return str((int(letter) ** private_key) % n)


open_keys = list(map(int, open("public_key", "r").read().split()))
cod = list(map(int, open("encrypted", "r").read().split(" ")))
private_key, e, n = int(open("private_key", "r").read()), open_keys[0], open_keys[1]
splited_cod = list(map(int, map("".join, zip(*[iter(list(map(decrypting, cod)))] * 2))))
open("decrypted", "w").write("".join(list(map(chr, splited_cod))))

