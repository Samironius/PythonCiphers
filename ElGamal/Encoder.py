p, q, ka, kb = 23, 15, 18, 13
M = 2313123222222222224343

Ya = (q**ka) % p
Yb = (q**kb) % p
Ykb = (Ya**kb) % p
C = bin(M ^ Ykb)

open("Encoding_result", "w").write("%s %s" % (Yb, C))
open("key", "w").write("%s %s" % (str(p), str(ka)))