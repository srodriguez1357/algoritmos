#Anmol, Nelly, Salvador

m1 = input()
s1 = input()
m2 = input()
s2 = input()

m3 = int(m1) + int(m2)
s3 = int(s1) + int(s2)

me = int(s3)/60
m1 = int(m3) + int(me)
s3 = int(s3)-(int(me)*60)

h3 = int(m3)/60
m3 = int(m3)-(int(h3)*60)
m3 = int(m3 + 1)


print(int(h3), ":", int(m3), ":", int(s3))