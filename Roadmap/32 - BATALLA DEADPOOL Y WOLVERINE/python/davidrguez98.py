""" /*
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
 */ """

#EJERCICIO

import random
import time

deadpool_healt = 1000
wolverine_healt = 1000

turn = 0

regenerate = False

while deadpool_healt > 0 and wolverine_healt > 0:

    turn += 1
    print(f"\nTurno {turn}")

    """ Deadpool ataca a Wolverine """

    if regenerate:
        print("Deadpool se está regenerando y no ataca.")
        regenerate = False
    elif random.random() > 0.2:
        deadpool_damage = random.randint(10, 100)
        print(f"Deadpool ataca a Wolverine con {deadpool_damage} de daño.")
        if deadpool_damage == 100:
            regenerate = True
            print("¡Deadpool ataca con daño máximo a Wolverine! Wolverine no atacará en el siguiente turno.")
        
        wolverine_healt -= deadpool_damage
        
        if wolverine_healt <= 0:
            print("La vida de Wolverine ha llegado a 0.")
            break
        else:
            print(f"Vida restante de Wolverine es: {wolverine_healt}")
    else:
        print("Wolverine esquiva el ataque de Deadpool.")


    """ Wolverine ataca a Deathpool """

    if regenerate:
        print("Wolverine se está regenerando y no ataca.")
        regenerate = False
    elif random.random() > 0.25:
        wolverine_damage = random.randint(10, 120)
        print(f"Wolverine ataca a Deadpool con {wolverine_damage} de daño.")

        if wolverine_damage == 120:
            regenerate = True
            print("¡Wolverine ataca con daño máximo a Deadpool! Deadpool no atacará en el siguiente turno.")
        
        deadpool_healt -= wolverine_damage
        
        if deadpool_healt <= 0:
            print("La vida de Deadpool ha llegado a 0.")
            break
        else:
            print(f"Vida restante de Deadpool es: {deadpool_healt}")
    else:
        print("Deadpool esquiva el ataque de Wolverine.")

    time.sleep(1)

if deadpool_healt > 0:
    print("Deadpool gana la batalla.")
else:
    print("Wolverine gana la batalla.")
