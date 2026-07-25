"""
EJERCICIO:
¡Deadpool y Wolverine se enfrentan en una batalla épica!
Crea un programa que simule la pelea y determine un ganador.
El programa simula un combate por turnos, donde cada protagonista posee unos
puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
de regeneración y evasión de ataques.

Requisitos:
1. El usuario debe determinar la vida inicial de cada protagonista.
2. Cada personaje puede impartir un daño aleatorio:
    - Deadpool: Entre 10 y 100.
    - Wolverine: Entre 10 y 120.
3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
4. Cada personaje puede evitar el ataque contrario:
    - Deadpool: 25% de posibilidades.
    - Wolverine: 20% de posibilidades.
5. Un personaje pierde si sus puntos de vida llegan a cero o menos.

Acciones:
1. Simula una batalla.
2. Muestra el número del turno (pausa de 1 segundo entre turnos).
3. Muestra qué pasa en cada turno.
4. Muestra la vida en cada turno.
5. Muestra el resultado final.

by adra-dev
"""
import random
import time

deadpool_health = int(input("Introduce la vida de Deadpool: "))
wolverine_health = int(input("Introduce la vida de Wolverine: "))

turn = 0
regenerate = False

while deadpool_health > 0 and wolverine_health > 0:

    turn +=1
    print(f"\nTurno {turn}")

    # Wolverine ataca a Deadpool
    if regenerate:
        print("Wolverine se esta regenerado y no ataca.")
        regenerate = False
    elif random.random() > 0.25:
        wolverine_damage = random.randint(10,120)
        print(f"Wolverine ataca a Deadpool con {wolverine_damage}.")
        if wolverine_damage == 120:
            regenerate = True
            print("Wolverine critico! Deadpool no atacara en el siguiente turno.")
        
        deadpool_health -= wolverine_damage

        if deadpool_health <= 0:
            print(f"La vida de Deadpool ha llegado a 0.")
            break
        else:
            print(f"Vida restante de Deadpool: {deadpool_health}")
    else: 
        print("Deadpool esquiva el ataque de Wolverine!")

    # Deadpool ataca a Wolverinel
    if regenerate:
        print("Deadpool se esta regenerado y no ataca.")
        regenerate = False
    elif random.random() > 0.2:
        deadpool_damage = random.randint(10,100)
        print(f"Deadpool ataca a Wolverine con {deadpool_damage}.")
        if deadpool_damage == 80:
            regenerate = True
            print("Deadpool critico! Wolverine no atacara en el siguiente turno.")
        
        wolverine_health -= deadpool_damage

        if wolverine_health <= 0:
            print(f"La vida de Wolverine ha llegado a 0.")
            break
        else:
            print(f"Vida restante de Wolverine: {wolverine_health}")
    else: 
        print("Wolverine esquiva el ataque de Deadpool!")

    time.sleep(1)


if deadpool_health > 0:
    print("Deadpool gana la batalla.")
else:
    print("Wolverine gana la batalla.")