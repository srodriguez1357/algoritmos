input("Buenos días chicos, este es un juego para ver qué tan bien aprendieron los tipos de datos")
print("Dberán de escribir int, char, str o float, según el tipo de valor que aparezca en pantalla")
input("Presiona enter para continuar")

Score=0

op1 = input("A: ")
if op1 == "char":
    Score = Score+1
op2 = input("1: ")
if op2 == "int":
    Score = Score+1
op3 = input("4.7: ")
if op3 == "float":
    Score = Score+1
op4 = input("Aloooo: ")
if op4 == "str":
    Score = Score+1
op5 = input("6.8: ")
if op5 == "float":
    Score = Score+1
op6 = input("1000: ")
if op6 == "int":
    Score = Score+1
op7 = input(" '65': ")
if op7 == "str":
    Score = Score+1
op8 = input(" 20.6: ")
if op8 == "float":
    Score = Score+1
print("Felicidades! Tuviste",Score,"puntos")















