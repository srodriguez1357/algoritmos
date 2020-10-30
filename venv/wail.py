for i in [3,5,6,4,9]:
    print (i)

for i in range(2, 31, 2):
    print(i, end=' ')

a =  int(input("Valor Inicial: "))
b =  int(input("Valor Final: "))
total = 0

for c in range(a, b):
    total = total+c
    print (total)

b = eval(input("Valor Base: "))
e = int(input("Exponente: "))
tot = b
for c in range(1, e):
    tot = tot*b
print(tot)