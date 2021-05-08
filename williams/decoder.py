key_list = open("key", "r").read()
chiper = open("encoding_result", "r").read().split()
c, c1, c2 = int(chiper[0]), int(chiper[1]), int(chiper[2])
S, n = int(key_list.split()[0]), int(key_list.split()[1])
k = int(open("key_2", "r").read())


M2 = (c**k)%n

if M2%2==0 and c2==1 or M2%2==1 and c2==0:
    M2=n-M2


M = ((S**-c1)*M2)%n



open("decoding_result", "w").write(str(int(M)))