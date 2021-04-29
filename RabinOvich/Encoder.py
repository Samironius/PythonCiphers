import random
# true_number = [x for x in range(1000) if x%4==3]
# p = random.choice(true_number)
# q = random.choice(true_number)
# p = 23
# q = 167

text = int(open("text", "r").read())

p = 0
while p%4!=3:
    p = int(input("Введіть p:"))

q = 0
while q%4!=3:
    q = int(input("Введіть q:"))

n = p * q
cipher = (text**2)%n

open("Encoding_result", "w").write(str(cipher))
open("key", "w").write("%s %s" % (p, q))