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
    list_of_Prime_Number = [x for x in range(100) if PrimeNumber(x)]
    p = random.choice(list_of_Prime_Number)
    p = 13
    print("p:",p)
    q = random.choice(list_of_Prime_Number)
    q = 19
    print("q:",q)
    n = p * q
    el = (p - 1) * (q - 1)
    x = 0

    while x!=1:
        e = random.randint(1, 100)
        e = 59
        x = gcdex(el, e)[0]
    print("e:",e)
    return e, n


def decrypting(text, open_key_e, open_key_n):
    f = open("encrypted.txt", "w")
    f.write(str((int(text) ** open_key_e) % open_key_n))
    f.close()


text = open("text.txt", "r").read()


open_key_e, open_key_n = key_gen()
decrypting(text, open_key_e, open_key_n)
print()