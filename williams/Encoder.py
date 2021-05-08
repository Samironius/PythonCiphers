import math
import random


def jacobi_sym(a, n):
    if n % 2 == 0 or math.gcd(a, n) != 1 or a == 0:
        return 0
    e = 0
    while a % 2 == 0:
        e = e + 1
        a = a // 2
    s = 1
    if e % 2 != 0 and (n % 8 == 3 or n % 8 == 5):
        s = -1
    if n % 4 == 3 and a % 4 == 3:
        s = -s
    n1 = n % a
    if a == 1:
        return s
    else:
        return s * jacobi_sym(n1, a)


M = int(open("text", "r").read())
n = 0
while jacobi_sym(M, n) == 0:
    p, q = 0, 0
    while p%8!=3:
        p = int(input("input p:"))
    while q%8!=7:
        q = int(input("input q:"))
    # q = random.choice([x for x in range(100) if x%8==7])
    # p, q = 83, 79
    n = p * q

if jacobi_sym(M,n) == -1:
    c1 = 1
elif jacobi_sym(M,n) == 1:
    c1 = 0

# S = random.choice([s for s in range(100) if jacobi_sym(s,n) == -1])
# S = 5
S = 0
while jacobi_sym(S,n) != -1:
    S = int(input("input S"))
k = (1/2)*((1/4)*(p-1)*(q-1)+1)

if c1 == 0:
    M1 = M%n
else:
    M1 = S * M % n

c2 = M1%2
c = (M1**2)%n


open("Encoding_result", "w").write("%s %s %s" % (c, c1, c2))
open("key", "w").write("%s %s" % (S, n))
open("key_2", "w").write(str(int(k)))