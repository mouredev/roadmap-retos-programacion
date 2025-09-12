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
import random, time

class Simulator():

    deadpool_life = int(input("Introduce la vida inicial para deadpool: "))
    wolverine_life = int(input("Introduce la vida inicial para wolverine: "))

    
    wolverine_attack = random.randint(10, 120)

    deadpool_defense = 0.25
    wolverine_defense = 0.20

    turn = 0
    deadpool_regenerate = False
    wolverine_regenerate = False

    while deadpool_life > 0 and wolverine_life > 0:
        turn += 1
        print(f"Turno: {turn}")

        if deadpool_regenerate:
            print("Deadpool se esta regenerando")
            deadpool_regenerate = False
        elif random.random() > 0.2:
            deadpool_attack = random.randint(10, 100)
            print(f"Deadpool ataca con {deadpool_attack} de daño.")
            if deadpool_attack == 100:
                deadpool_regenerate = True
                print("¡Golpe Critico! Wolverine no ataca en el siguiente turno")
            wolverine_life -= deadpool_attack
            if wolverine_life <= 0:
                print("Wolverine ha sido eliminado.")
                break
            else:
                print(f"Vida restante de Wolverine: {wolverine_life}")
        else:
            print("Wolverine esquiva el ataque de Deadpool")
        
        if wolverine_regenerate:
            print("Wolverine se esta regerenando")
            wolverine_regenerate = False
        elif random.random() > 0.25:
            wolverine_attack = random.randint(10, 120)
            print(f"Wolverine ataca con {wolverine_attack} de daño.")
            if wolverine_attack == 120:
                wolverine_regenerate = True
                print("¡Golpe Critico! Deadpool no ataca en el siguiente turno")
            deadpool_life -= wolverine_attack
            if deadpool_life <= 0:
                print("Deadpool ha sido eliminado.")
                break
            else:
                print(f"Vida restante de Wolverine: {deadpool_life}")
        else:
            print("Deadpool esquiva el ataque de Wolverine")
    time.sleep(1)

    if deadpool_life > 0:
        print("Deadpool ha ganado")
    else:
        print("Wolverine ha ganado")
