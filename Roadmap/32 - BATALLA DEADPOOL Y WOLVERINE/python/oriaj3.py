"""
32 - BATALLA DEADPOOL Y WOLVERINE
Autor de la solución: Oriaj3

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

import random
import time

class simulador():
    deadpool_health: int
    wolverine_health: int
    turn: int = 0

    #Porcentaje de esquiva 
    deeadpool_evade = 0.25
    wolverine_evade = 0.20

    #Flag para saber si el personaje se está regenerando
    deadpool_regenerate = False
    wolverine_regenerate = False

    def __init__(self):
        deadpool_hp = int(input("Introduce la vida inicial de Deadpool: "))
        wolverine_hp = int(input("Introduce la vida inicial de Wolverine: "))
        
        self.deadpool_health = deadpool_hp
        self.wolverine_health = wolverine_hp

    def iniciar(self):
        while(self.deadpool_health > 0 and self.wolverine_health > 0):
            self.turno()
            time.sleep(1)
        self.resultado()

    def turno(self):
        print(f"\nTurno {self.turn}")
        self.turn += 1

        # Calcula los daños 
        deadpool_damage = random.randint(10, 100)
        wolverine_damage = random.randint(10, 120)

        if self.deadpool_regenerate:
            print("Deadpool se está regenerando y no ataca.")
            self.deadpool_regenerate = False
            deadpool_damage = 0
    
        if self.wolverine_regenerate:
            self.wolverine_regenerate = False
            wolverine_damage = 0
        

        # Daños máximos
        if deadpool_damage == 100:
            print("¡Golpe crítico de Deadpool! Wolverine no atacará en el siguiente turno ya que tiene que regenerarse.")
            self.wolverine_regenerate = True
        elif wolverine_damage == 120:
            print("¡Golpe crítico de Wolverine! Deadpool no atacará en el siguiente turno ya que tiene que regenerarse.")
            self.deadpool_regenerate = True
        else:
            if deadpool_damage != 0:
                print(f"Deadpool ataca a Wolverine con {deadpool_damage} de daño.")
            else:
                print("Wolverine se está regenerando y no ataca.")
            if wolverine_damage != 0:
                print(f"Wolverine ataca a Deadpool con {wolverine_damage} de daño.")
            else:
                print("Deadpool se está regenerando y no ataca.")

        #Calculo si esquiva el ataque, random.random() devuelve un número entre 0 y 1 por tanto si es menor al porcentaje de esquiva, esquiva el ataque
        if random.random() < self.deeadpool_evade:
            print("¡Deadpool esquiva el ataque de Wolverine!")
        else:
            self.deadpool_health -= wolverine_damage
            print(f"Vida restante de Deadpool: {self.deadpool_health}")
        
        if random.random() < self.wolverine_evade:
            print("¡Wolverine esquiva el ataque de Deadpool!")
        else:
            self.wolverine_health -= deadpool_damage
            print(f"Vida restante de Wolverine: {self.wolverine_health}")
        
    def resultado(self):
        if self.deadpool_health <= 0 and self.wolverine_health <= 0:
            print("Ambos personajes han muerto.")
        elif self.deadpool_health <= 0:
            print("Wolverine ha ganado la batalla!")
        else:
            print("Deadpool ha ganado la batalla!")


simulador = simulador()
simulador.iniciar()
