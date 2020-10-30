import random

J1 = 0
J2 = 0
secretNum = 9

def printtablero():
    for i in range(fil):
        print()
        for j in range(col):
            print(tablero[i][j], end=" ")
    print()
    return

def test(x):
    while(x<0 or x>6):
        x=int(input("Valor invalido, vuelve a intentar: \n ~>"))
    return x

def turno():
    x1 = int(input("Jugador, ingresa ordenada X: \n ~>"))
    x1 = test(x1)
    y1 = int(input("Jugador, ingresa ordenada Y: \n ~>"))
    y1 = test(y1)
    showsecret(x1, y1)
    printtablero()
    x2 = int(input("Jugador, ingresa otra ordenada X: \n ~>"))
    x2 = test(x2)
    y2 = int(input("Jugador, ingresa otra ordenada Y: \n ~>"))
    y2= test(y2)
    showsecret(x2, y2)
    printtablero()
    if secret[y1-1][x1-1] != secret[y2-1][x2-1]:
        hidesecret(x1, y1)
        hidesecret(x2, y2)
        print("Error!")
        printtablero()
    else:
        print("Correcto! Tu puntuación aumentó 1")
        return 1
    return 0

def showsecret(x,y):
    tablero[y][x] = secret[y-1][x-1]
    return

def hidesecret(x,y):
    tablero[y][x] = n
    return

col = 7
fil = 7
n = "-"
tablero = [[" ",1,2,3,4,5,6],[1,n,n,n,n,n,n],[2,n,n,n,n,n,n],[3,n,n,n,n,n,n],[4,n,n,n,n,n,n],[5,n,n,n,n,n,n,n],[6,n,n,n,n,n,n]]
printtablero()

secret = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
for i in range(1,19):
    a = random.randint(0,5)
    b = random.randint(0,5)
    while secret[a][b] != 0:
        a = random.randint(0,5)
        b = random.randint(0,5)
    secret[a][b] = i

    c = random.randint(0,5)
    d = random.randint(0,5)
    while secret[c][d] != 0:
        c = random.randint(0,5)
        d = random.randint(0,5)
    secret[c][d] = i

#imprimir secret
#for i in range(0,6):
#    print()
#    for j in range(0,6):
#        print(secret[i][j], end=" ")

while secretNum > 0:
    print("Turno de jugador 1:")
    if (turno()):
        J1 += 1
        secretNum -= 1

    print("Turno de jugador 2:")
    if(turno()):
        J2 += 1
        secretNum -= 1
if J1 == J2:
    print("Empate")
elif J1 > J2:
    print("Gana J1 con:", J1, "puntos")
elif J2 > J1:
    print("Gana J2 con:", J2, "puntos")
