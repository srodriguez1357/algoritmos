import io

manejador = open("prueba.txt", "w")
frase="Bienvenidos"
manejador.write(frase)
manejador.close()

manejador=open("prueba.txt","r")
archivo = manejador.read()

manejador=open("prueba.txt","a")
manejador.write("al menajeo de archivos")

manejador.seek(11)
manejador.write("todos")

print(archivo)
manejador.close()


