"""
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
"""
import random
import time

deadpool_health = 1000
wolwerine_health = 1000

turn = 0
regenerate = False
continuar = True
while continuar == True:
    
    turn += 1
    print(f"Turno: {turn}")
    # Deadpool ataca
    if regenerate:
        print("Deadpool se esta regenerando y no ataca")
        regenerate = False
    elif random.random() > 0.2:
        deadpool_damage = random.randint(10, 100)
        print(f"Deadpool inflinge {deadpool_damage} puntos de daño")
    
        if deadpool_damage == 100:
            regenerate = True
            print("Golpe crítico de Deadpool, wolwerine no atacara en el siguiente turno")
        wolwerine_health -= deadpool_damage
    
        if wolwerine_health <= 0:
            continuar = False
        else:
            print(f"Vida actual de Wolwerine {wolwerine_health}")
    else:
        print("Wolwerine ha esquivado el ataque!")
     
        
    # Wolwerine ataca
    if regenerate:
        print("Wolverine se esta regenerando y no ataca")
        regenerate = False
        
    elif random.random() > 0.25:
        wolwerine_damage = random.randint(10, 120)
        print(f"Wolverine inflinge {wolwerine_damage} puntos de daño")
    
        if wolwerine_damage == 120:
            regenerate = True
            print("Golpe crítico de Wolwerine, Deadpool no atacara en el siguiente turno")
        deadpool_health -= wolwerine_damage
    
        if deadpool_health <= 0:
             continuar = False
        else:
            print(f"Vida actual de Deadpool {deadpool_health}")
    else:
        print("Deadpool ha esquivado el ataque!")
    
    time.sleep(2)
    
if deadpool_health > 0:
    print("Deadpool gana la batalla")
else:
    print("Wolwerine gana la batalla")