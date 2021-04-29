key_list = open("key", "r").read()
cipher = int(open("encoding_result", "r").read())
p, q = int(key_list.split()[0]), int(key_list.split()[1])
n = p*q


def stepin (x, d, n):
    d2 = []
    while (d!=0):
        d2.append(d%2)
        d=d//2
    d2.reverse()
    z = 1
    for k in range(len(d2)):
        z= z*z
        if (d2[k]==1): z= z*x
        z=z%n
    return z


def gcdex(a, b):
    if b == 0:
        return a, 1, 0
    d, y, x = gcdex(b, a % b)
    return d, x, y - (a // b) * x


m1 = stepin(cipher,(p+1)/4,p)
m2 = p-stepin(cipher,(p+1)/4,p)
m3 = stepin(cipher,(q+1)/4,q)
m4 = q-stepin(cipher,(q+1)/4,q)

a = q*(gcdex(p, q)[2]%n)
b = p*(gcdex(p, q)[1]%n)

M1 = (a*m1 + b*m3) % n
M2 = (a*m1 + b*m4) % n
M3 = (a*m2 + b*m3) % n
M4 = (a*m2 + b*m4) % n

print(M1, M2, M3, M4)
open("decoding_result", "w").write("%s %s %s %s" % (M1, M2, M3, M4))