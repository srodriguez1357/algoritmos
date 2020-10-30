alumnos = int(input("Ingrese cantidad de alumnos: "))

if alumnos >= 100:
    costo = alumnos*65
else:
    if alumnos >= 50:
        costo = alumnos*70
    else:
        if alumnos >= 30:
            costo=alumnos*95
        else:
            total=4000
print(total)
