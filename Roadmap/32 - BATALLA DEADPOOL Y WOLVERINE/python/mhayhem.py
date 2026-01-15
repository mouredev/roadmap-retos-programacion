# @Author Daniel Grande (Mhayhem)

import random
import os
from time import sleep

# EJERCICIO:
# ¡Deadpool y Wolverine se enfrentan en una batalla épica!
# Crea un programa que simule la pelea y determine un ganador.
# El programa simula un combate por turnos, donde cada protagonista posee unos
# puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
# de regeneración y evasión de ataques.
# Requisitos:
# 1. El usuario debe determinar la vida inicial de cada protagonista.
# 2. Cada personaje puede impartir un daño aleatorio:
#    - Deadpool: Entre 10 y 100.
#    - Wolverine: Entre 10 y 120.
# 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
# siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
# 4. Cada personaje puede evitar el ataque contrario:
#    - Deadpool: 25% de posibilidades.
#    - Wolverine: 20% de posibilidades.
# 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
# Acciones:
# 1. Simula una batalla.
# 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
# 3. Muestra qué pasa en cada turno.
# 4. Muestra la vida en cada turno.
# 5. Muestra el resultado final.

class Fighter:
    def __init__(self, name: str, life: int, damage: int, evasion_value: float):
        self.name = name.capitalize()
        self.life = life
        self.damage = damage
        self.evasion_value = evasion_value

    def attack(self, stunned: bool):
        stunt = False
        damage = random.randint(10, self.damage)
        if stunned:
            print(f"{self.name} esta regenerandose, no puede atacar.")
            damage = 0
        if damage == self.damage:
            stunt = True
        return damage, stunt

    def evasion(self):
        return random.random() < self.evasion_value

    def be_damaged(self, damage: int, evasion: bool, stunt: bool):
        stunned = False
        if evasion:
            print(f"{self.name} evade el ataque.")
        else:
            if stunt:
                stunned = True
            self.life -= damage
        if self.life < 0:
            self.life = 0
        return stunned


class SimFight:
    def turn_based_combat(self, fighter1: Fighter, fighter2: Fighter):
        turn = 1
        stunned1 = False
        stunned2 = False
        print(f"### {fighter1.name}: {fighter1.life} hp //  {fighter2.name}: {fighter2.life} hp ###")
        print("\n")
        while fighter1.life > 0 and fighter2.life > 0:
            print(f"### {fighter1.name}: {fighter1.life} hp //  {fighter2.name}: {fighter2.life} hp ###")
            print("\n")
            print(f"Turno {turn}")
            print("\n")

            if not stunned1:
                print(f"{fighter1.name} Ataca.")
                print("\n")
                damage, stunt = fighter1.attack(False)
                evaded = fighter2.evasion()
                stunned2 = fighter2.be_damaged(damage, evaded, stunt)
                if evaded:
                    print(f"{fighter2.name} no recibe daño.")
                else:
                    print(f"{fighter2.name} ha recivido {damage} puntos de daño.")
                print("\n")
            else:
                print(f"{fighter1.name} esta aturdido y se regenera.")
                stunned1 = False

            if not stunned2:
                print(f"{fighter2.name} Ataca.")
                print("\n")
                damage, stunt = fighter2.attack(False)
                evaded = fighter1.evasion()
                stunned2 = fighter1.be_damaged(damage, evaded, stunt)
                if evaded:
                    print(f"{fighter1.name} no recibe daño.")
                else:
                    print(f"{fighter1.name} ha recibido {damage} puntos de daño.")
            else:
                print(f"{fighter2.name} esta aturdido y se regenera.")
                print("\n")
                stunned2 = False

            print("\n")
            turn += 1
            sleep(1)
            os.system("clear")

        if fighter1.life < 0:
            print(f"### {fighter1.name}: {fighter1.life} hp //  {fighter2.name}: {fighter2.life} hp ###")
            print(f"{fighter2.name} WINNER!!!!!!")
        else:
            print(f"### {fighter1.name}: {fighter1.life} hp //  {fighter2.name}: {fighter2.life} hp ###")
            print(f"{fighter1.name} WINNER!!!!!!")

dead = Fighter("deadpool", 1200, 100, 0.25)
wolf = Fighter("wolverine", 1200, 120, 0.2)

combat = SimFight()
combat.turn_based_combat(dead, wolf)
