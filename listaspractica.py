lista = [1, 2, 3, 4, 5,6, 7, 8, 9]
long = len(lista)
print(long)

print(lista[3])
print(lista[-1])

lista2 = lista[3:9:1]
print(lista2)

print(lista[::-1])

lista = lista + [10]
lista = [0] + lista
lista3 = 10*[0]

print(lista)
print(lista3)

lista.append(11)
print(lista)

lista.insert(3, 20)
lista[4] = "cinco"
print(lista)

lista3.clear()
print(lista3)

lista.pop(3)
print(lista)

del(lista[0:8:2])
print(lista)

lista.reverse()
print(lista)

lista.sort()
print(lista)

print(lista.count(1))



