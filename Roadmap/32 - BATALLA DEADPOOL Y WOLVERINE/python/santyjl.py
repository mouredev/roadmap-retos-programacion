# #32 BATALLA DEADPOOL Y WOLVERINE
#### Dificultad: Media | Publicación: 05/08/24 | Corrección: 12/08/24

"""
/*
 * EJERCICIO:
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista.
 * 2. Cada personaje puede impartir un daño aleatorio:
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario:
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 * Acciones:
 * 1. Simula una batalla.
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 * 3. Muestra qué pasa en cada turno.
 * 4. Muestra la vida en cada turno.
 * 5. Muestra el resultado final.
 */
"""

import os
import random
import time


def barra_de_vida(vida : float):
    for i in range(int(vida//10)):
        print("💗=" , end="")

    print("")

def daño(peleador: int) -> int:
    valor_daño = 0

    if peleador == 1 :
        valor_daño = random.randint(10 , 120)
        if valor_daño > 30:
            valor_daño //= 3

    else:
        valor_daño = random.randint(10 , 100)
        if valor_daño > 30:
            valor_daño //= 3

    return valor_daño

vida_Wolverine = float(input("Ingresa la vida de Wolverine: "))
vida_Deadpool = float(input(" Ingresa la vida de DeadPool: "))

turno = 0

print(" ¡Deadpool y Wolverine se enfrentan en una batalla épica!, algo indescriptible pero no imposible de crer.\n")
time.sleep(1)
print("Wolverine toma siempre la iniciativa y va con todo contra Deadpool")

while True:
    os.system("cls")
    turno += 1

    if vida_Deadpool <= 0 or vida_Wolverine <= 0:
        print("final de la batalla, El ganador a sido ......")
        time.sleep(2)

        print(f" :========== {" Deadpool🦴" if vida_Deadpool > vida_Wolverine else "Wolverine🐆"} ==========: ")
        break

    print(f"====== Ronda {turno} ======")
    evitar_golpe = random.randint(1 , 100)

    print("Vida de Wolverine : " , end="")
    barra_de_vida(vida_Wolverine)
    print("Vida Deadpool : ", end="")
    barra_de_vida(vida_Deadpool)




    if turno % 2 == 0 and evitar_golpe > 25:
        daño_infligido = daño(2)
        print(f"Deadpool le ha dado efectivamente a Wolverine un golpe con un daño de {daño_infligido}")

        vida_Wolverine -= daño_infligido

    elif turno % 2 == 0 :
        print(f"Deadpool fue con todo para darle a Wolverine pero fue equivado.")


    if turno % 2 != 0 and evitar_golpe > 20:
        daño_infligido = daño(1)
        print(f"Wolverine le ha dado efectivamente a Deadpool un golpe con un daño de {daño_infligido}")

        vida_Deadpool -= daño_infligido

    elif turno % 2 != 0 :
        print(f"Wolverine fue tan rapido como una pantera pero fue equivado por Deadpool en el último segundo. ")

    time.sleep(4.5)



