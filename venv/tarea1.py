op = input("Ingresa 1 para cambiar de Dólar a RMB o 2 para ir de RMB  a dólar: ")
tasa= eval(input("Inresa la tasa de cambio de Dólar a RMB: "))
if op == "1":
    dolar = eval(input("Ingresa la cantidad de dólares: "))
    RMB = dolar*tasa
    print(RMB)
else:
    RMB = eval(input("Ingresa la cantidad de RMB: "))
    dolar = RMB/tasa
    print(dolar)