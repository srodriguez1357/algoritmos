print("1- Triángulo")
print("2- Círculo")
op = int(input("Dame una opción"))

if op == 1:
    base = eval(input("Ingresa el valor de la base: "))
    h = eval(input("Ingresa el valor de la balturaase: "))
    area = (base*h) /2
    print(area)
elif op == 2:
    radio = eval(input("Ingresa el radio: "))
    area=(3.14*(radio*radio))/2
    print(area)
else:
    print("Opción no válida")
