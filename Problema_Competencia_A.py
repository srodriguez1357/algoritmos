#Anmol, Nelly, Salvador

cat,sueldo , horas = input().split()

if int(cat) >= 4:
    print(sueldo)

else:
    if int(horas) > 30:
        horas = 30
    else:
        horas = horas

    if int(cat) == 1:
        sueldo = int(sueldo)+(int(horas)*400)
        print(sueldo)
    elif int(cat) == 2:
        sueldo = int(sueldo)+(int(horas)*500)
        print(sueldo)
    elif int(cat) == 3:
        sueldo = int(sueldo) + (int(horas) * 850)
        print(sueldo)