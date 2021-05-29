import numpy as np


m, n = 110, 31
private_key = [1, 2, 4, 8, 16]
while len(open("Text", "r").read())%len(private_key) != 0:
    private_key.append(private_key[-1]*2)
    print(private_key)
open_key = list(map(lambda x: (x*n)%m, private_key))
text = list(map(''.join, zip(*[iter(open("Text", "r").read())]*len(private_key))))
cipher = list(map(lambda x: sum(np.array(list(map(int, x))) * np.array(open_key)), text))
open("private_key.txt", "w").write(" ".join(map(str, private_key)))
open("encoding_result.txt", "w").write(" ".join(map(str,cipher)))