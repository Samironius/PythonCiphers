p, q, ka, kb = 17, 3, 7, 13
M = 2313123222222222224343

Ya = (q**ka) % p
print(Ya)
Yb = (q**kb) % p
print(kb)
Ykb = (Ya**kb) % p
print(Ykb)
C = bin(M ^ Ykb)


open("Encoding_result", "w").write("%s %s" % (Yb, C))
open("key", "w").write("%s %s" % (str(p), str(ka)))