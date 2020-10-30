import io

man = open("tabla.csv","w")
man.write("Asistencias\n")
base = int(input("Ingresa la base de la tabla"))
for i in range(1,11):
    man.write(str(i))
    man.write(",")
    man.write(str(base*i))
man.close()
