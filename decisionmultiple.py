calificacion = eval(input("Ingresa la calificación: "))

if calificacion < 0 or calificacion > 10:
    print("No válido")
elif calificacion <= 5.9:
    print("Cinco")
elif calificacion <= 6.49:
    print("Seis")
elif calificacion <= 7.49:
    print("Siete")
elif calificacion <= 8.49:
    print("Ocho")
elif calificacion <= 9.49:
    print("Nueve")
else:
    print("Diez")