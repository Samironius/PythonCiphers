def decrypting(letter):
    return str((letter ** private_key) % open_key_n)


open_keys = list(map(int, open("public_key.txt", "r").read().split()))
text = list(map(int, open("encrypted.txt", "r").read().split(" ")))
private_key, open_key_e, open_key_n = int(open("private_key.txt", "r").read()), open_keys[0], open_keys[1]
open("decrypted.txt", "w").write("".join(list(map(decrypting, text))))
