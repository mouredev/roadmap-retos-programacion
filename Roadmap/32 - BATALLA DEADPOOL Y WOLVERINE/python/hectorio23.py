# Autor:  Héctor Adán
# GitHub: https://github.com/hectorio23

'''
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
'''


import random
import time

class Character:
    def __init__(self, name, min_damage, max_damage, dodge_chance):
        self.name = name
        self.health = 0
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.dodge_chance = dodge_chance

    def attack(self):
        return random.randint(self.min_damage, self.max_damage)

    def evade(self):
        return random.random() < self.dodge_chance

    def is_alive(self):
        return self.health > 0

class Deadpool(Character):
    def __init__(self):
        super().__init__("Deadpool", 10, 100, 0.25)

class Wolverine(Character):
    def __init__(self):
        super().__init__("Wolverine", 10, 120, 0.20)

def simulate_battle(char1, char2):
    turn = 1
    skip_char1 = False
    skip_char2 = False

    while char1.is_alive() and char2.is_alive():
        print(f"\n**** Turno {turn} ****:")
        if not skip_char1:
            if not char2.evade():
                damage = char1.attack()
                char2.health -= damage
                print(f"[+] - {char1.name} ataca a {char2.name} causando {damage} de daño.")
                if damage == char1.max_damage:
                    print(f"[+] - {char2.name} debe regenerarse y pierde el siguiente turno.")
                    skip_char2 = True
            else:
                print(f"[+] - {char2.name} evade el ataque de {char1.name}.")
        else:
            skip_char1 = False

        if not skip_char2 and char2.is_alive():
            if not char1.evade():
                damage = char2.attack()
                char1.health -= damage
                print(f"[+] - {char2.name} ataca a {char1.name} causando {damage} de daño.")
                if damage == char2.max_damage:
                    print(f"[+] - {char1.name} debe regenerarse y pierde el siguiente turno.")
                    skip_char1 = True
            else:
                print(f"[+] - {char1.name} evade el ataque de {char2.name}.")
        else:
            skip_char2 = False

        print(f"{char1.name} Vida: {char1.health}, {char2.name} Vida: {char2.health}\n")
        time.sleep(1)
        turn += 1

    if char1.is_alive():
        print(f"{char1.name} gana la batalla!")
    else:
        print(f"{char2.name} gana la batalla!")

if __name__ == "__main__":
    deadpool_health = int(input("Ingrese la vida inicial de Deadpool: "))
    wolverine_health = int(input("Ingrese la vida inicial de Wolverine: "))

    deadpool = Deadpool()
    wolverine = Wolverine()

    deadpool.health = deadpool_health
    wolverine.health = wolverine_health

    simulate_battle(deadpool, wolverine)
