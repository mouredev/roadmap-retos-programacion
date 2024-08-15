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
import json

class Character:
    def __init__(self, name, min_damage, max_damage, evade_chance):
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.evade_chance = evade_chance
        self.health = 0

    def set_health(self, health):
        self.health = health

    def attack(self):
        return random.randint(self.min_damage, self.max_damage)

    def evade(self):
        return random.random() < self.evade_chance

def simulate_battle(deadpool, wolverine):
    turn = 1
    while deadpool.health > 0 and wolverine.health > 0:
        print(f"Turno {turn}")
        if turn % 2 != 0:
            attacker, defender = deadpool, wolverine
        else:
            attacker, defender = wolverine, deadpool

        if defender.evade():
            print(f"{defender.name} evade el ataque de {attacker.name}!")
        else:
            damage = attacker.attack()
            defender.health -= damage
            print(f"{attacker.name} ataca a {defender.name} y causa {damage} puntos de daño.")
            if damage == attacker.max_damage:
                print(f"{defender.name} está aturdido y no puede atacar en el siguiente turno.")
                turn += 1

        print(f"Vida de {deadpool.name}: {deadpool.health}")
        print(f"Vida de {wolverine.name}: {wolverine.health}")
        time.sleep(1)
        turn += 1

    if deadpool.health <= 0:
        print("¡Wolverine gana la batalla!")
    elif wolverine.health <= 0:
        print("¡Deadpool gana la batalla!")

def main():
    deadpool = Character("Deadpool", 10, 100, 0.25)
    wolverine = Character("Wolverine", 10, 120, 0.20)

    deadpool_health = int(input("Introduce la vida inicial de Deadpool: "))
    wolverine_health = int(input("Introduce la vida inicial de Wolverine: "))

    deadpool.set_health(deadpool_health)
    wolverine.set_health(wolverine_health)

    simulate_battle(deadpool, wolverine)

    data = {
        "Deadpool": deadpool.health,
        "Wolverine": wolverine.health
    }

    with open("battle_results.json", "w") as file:
        json.dump(data, file)

    print("Los resultados de la batalla se han guardado en 'battle_results.json'.")

if __name__ == "__main__":
    main()
