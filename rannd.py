from random import randint

jugador1 = randint(1, 6)
jugador2 = randint(1, 6)

if jugador1 == jugador2:
    print("Empate")
else:
    if jugador1>jugador2:
        print("jugador 1")
    else:
        print("Jugador 2")
