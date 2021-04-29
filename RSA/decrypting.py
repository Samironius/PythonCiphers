import random

def gcdex(a, b):
    if b == 0:
        return a, 1, 0
    d, y, x = gcdex(b, a % b)
    return d, x, y - (a // b) * x


def PrimeNumber(n):
    count = 1
    for i in range(2,int(n**0.5)):
        if n % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False


def key_gen():

    p = 13
    print("p:",p)
    q = 19
    print("q:",q)
    n = p * q
    el = (p - 1) * (q - 1)
    x = 0

    while x!=1:
        e = random.randint(1, 100)
        e = 59
        x, open_key = gcdex(el, e)[0], gcdex(el, e)[2]
    open_key = open_key + el
    print("e:",e)

    return e, open_key, n


def decrypting(text, close_key, open_key):
    f = open("decrypted.txt", "w")
    f.write(str((text ** close_key) % open_key))
    f.close()


text, open_key_e, open_key_n = key_gen()
decrypting(text, open_key_e, open_key_n)
print()