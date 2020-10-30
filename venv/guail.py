num = eval(input("Ingresa un número: "))
suma = 0

while num != 0:
    suma = suma + num
    num = eval(input("Ingresa otro número: "))

print("La suma es igual a ", suma)