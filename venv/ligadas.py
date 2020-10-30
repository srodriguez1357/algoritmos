import csv
n = int(input('Escriba el total de alumnos:'))
i = 0
cal = []
nom = []
check = False
while i < n:
    nom.append(input("Ingrese el nombre del alumno: "))
    cal.append(int(input("Ingrese la calificación del alumno: ")))
    i = i+1

##nom, cal = zip(*sorted(zip(nom, cal, ), reverse=True))

for i in range(len(cal)):
    for x in range(i, len(cal)):
        if cal[i] < cal[x]:
            cal[i], cal[x] = cal[x], cal[i]
            nom[i], nom[x] = nom[x], nom[i]

print(f'El alumno con el promedio mayor fue {nom[0]} con {cal[0]}')
resp = input('Desea buscar un alumno? S/N')
if resp == 'S':
    alumno = input('Escriba el nombre del alumno:')
    for i in range(len(cal)):
        if alumno == nom[i]:
            print(f'El alumno {alumno} tiene promedio de {cal[i]}')
            check = True
            break
        else:
            check = False
    if not check:
        print('El alumno no pertenece a esta lista')
lines = [['Alumno', 'Calificación']]
for i in range(len(cal)):
    lines.append([nom[i], cal[i]])
with open('alumnos.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(lines)