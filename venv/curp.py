nom = input("Escriba su nombre: ").upper()
ap= input("Escriba su apellido paterno: ").upper()
am = input("Escriba su apellido materno: ").upper()

ano = "0"
while len(ano) != 2:
    ano = input("Inserte los dos últimos dígitos de su año de nacimiento: ")

print("Su clave de identificación única es:", ap[0], ap[1], am[0], am[2], nom[0], nom[-1], ano , sep="")