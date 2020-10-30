c = int(input("Ingresa la cantidad de ciudades: "))
tot = 0
totc = 0
tott = 0
tote = 0
for n in range(c):
    t = int(input("Ingresa la cantidad de tiendas: "))
    for i in range(t):
        e = int(input("Ingresa la cantidad de empleados: "))
        for x in range(e):
            v = int(input("Ingresa la csntidad de ventas: "))
            tote = 0
            for y in range(v):
                din = int(input("Ingresa la cantidad de a venta: $"))
                tote = tote + din
            tott = tott + tote
        totc = totc + tott
        print("Los Ingresos por tienda son de: $", tott)
        tott = 0
    tot = tot + totc
    print("Los Ingresos por ciudad son de: $", totc)
    totc = 0

print("Los Ingresos Totales son de $",tot)
