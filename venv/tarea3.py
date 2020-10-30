xc = eval(input("Ingresa la coordenada x del centro del círculo"))
yc = eval(input("Ingresa la coordenada y del centro del círculo"))
x = eval(input("Ingresa la coordenada x del punto"))
y = eval(input("Ingresa la coordenada y del punto"))

dist = (((x-xc)^2)+((y-yc)^2))^-.5

if dist <= 10:
    print("Tu punto está dentro del círculo")
else:
    print("Tu punto est´s fuera del círculo")
