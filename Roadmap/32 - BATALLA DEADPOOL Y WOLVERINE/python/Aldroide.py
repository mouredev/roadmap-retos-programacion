import time
import random


class Character:
    def __init__(self, name, max_damage, evasion):
        self.name = name
        self.max_damage = max_damage
        self.evasion = evasion
        self.healt = 0

    def set_healt(self, healt):
        self.healt = healt

    def attack(self):
        return random.randint(0, self.max_damage)

    def evade(self):
        return random.random() < self.evasion


def simulate_battle(deadpool_healt, wolverine_healt):
    deadpool = Character("Deadpool", 100, 0.25)
    wolverine = Character("Wolverine", 120, 0.20)

    deadpool.set_healt(deadpool_healt)
    wolverine.set_healt(wolverine_healt)

    turn = 1
    skip_next = {"Deadpool": False, "Wolverine": False}
    while deadpool.healt > 0 and wolverine_healt > 0:
        print(f"Turno {turn}")
        if not skip_next["Deadpool"]:
            if not wolverine.evade():
                damage = deadpool.attack()
                if damage == deadpool.max_damage:
                    skip_next["Wolverine"] = True
                wolverine.healt -= damage
                print(f"Deadpool ataca y causa {damage} de daño a Wolverine.")
            else:
                print("Wolverine evade el ataque de Deadpool")
        else:
            print("Deadpool se recupera y no puede atacar este turno")
            skip_next["Deadpool"] = False

        if wolverine.healt <= 0:
            print("Wolverine ha sido derrotado, Deadpool gana!")
            break

        if not skip_next["Wolverine"]:
            if not deadpool.evade():
                damage = wolverine.attack()
                if damage == wolverine.max_damage:
                    skip_next["Deadpool"] = True
                deadpool.healt -= damage
                print(f"Wolverine ataca y causa {damage} de daño a Deadpool.")
            else:
                print("Deadpool evade el ataque de Wolverine.")
        else:
            print("Wolverine se recupera y no puede atacar este turno")
            skip_next["Wolverine"] = False

        if deadpool.healt <= 0:
            print("Deadpool ha sido derrotado, Wolverine gana!")

        print(f"Vida de Deadpool: {deadpool.healt}")
        print(f"Vida de Wolverine: {wolverine.healt}")
        print()
        turn += 1
        time.sleep(1)

    if deadpool.healt > 0:
        print(f"Deadpool gana la batalla con {deadpool.healt} puntos de vida")
    elif wolverine.healt > 0:
        print(
            f"Wolverine gana la batalla con {wolverine.healt} puntos de vida")


simulate_battle(250, 250)
