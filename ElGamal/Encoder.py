p, q, ka, kb = 23, 15, 18, 13
M = int(open("Text", "r").read())
Ya = (q**ka) % p
Yb = (q**kb) % p
Ykb = (Ya**kb) % p
C = bin(M ^ Ykb)
open("Encoding_result", "w").write("%s %s" % (Yb, C))
open("key", "w").write("%s %s" % (str(p), str(ka)))