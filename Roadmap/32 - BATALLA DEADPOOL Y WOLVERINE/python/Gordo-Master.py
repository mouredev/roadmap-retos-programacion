# 32 - Batalla de Deadpool y Wolverine
import random
import time


class Fighter():

    def __init__(self, name: str, health: int, damage: tuple, regeneration: bool, evasion: int):
        self.name = name
        self.health = health
        self.damage = damage
        self.regeneration = regeneration
        self.evasion = evasion

    def take_damage(self, damage, critic):
        self.health -= damage
        self.regeneration = critic

wolverine_hp = int(input("Ingrese la vida de Wolverine: "))
deadpool_hp = int(input("Ingrese la vida de Deadpool: "))

wolverine =Fighter("Wolverine", wolverine_hp, (10, 120),False,20)
deadpool = Fighter("Deadpool", deadpool_hp, (10, 100),False,25)


def damage_dealt(attacker: Fighter, defender: Fighter) -> tuple :

    if not random.random() < (defender.evasion/100):
        damage = random.randint(attacker.damage[0],attacker.damage[1])
        if damage == attacker.damage[1]:
            return damage, True
        return damage, False
    return 0, False

def turn_to_attack(attacker: Fighter, defender: Fighter):
    
    if not attacker.regeneration:

        attacker_dam, attacker_crit = damage_dealt(attacker, defender)

        if attacker_crit == False:
            if attacker_dam == 0:
                print(f"{attacker.name} ataca a {defender.name}, pero este logra esquivarlo!")
            else:
                print(f"{attacker.name} ataca a {defender.name}, y le baja {attacker_dam} HP")
        else:
            print(f"{attacker.name} hace un golpe critico a {defender.name} y le baja {attacker_dam} HP, dejandolo incapacitado para el siguiente turno!")
        
        return attacker_dam, attacker_crit
    
    else:
        print(f"{attacker.name} se esta regenerando y no puede atacar!")
        attacker.regeneration = False
        return 0, False    
    

def fight():

    round = 0

    print("Comienza la pelea!!!")
    print(f"Wolverine HP: {wolverine.health}{" "*5}Deadpoll HP: {deadpool.health}")
    while True:
        round += 1
        print(f"\nRonda {round}:")
        wolv_dam, wolv_crit = turn_to_attack(wolverine, deadpool)
        dead_dam, dead_crit = turn_to_attack(deadpool, wolverine)
        deadpool.take_damage(wolv_dam, wolv_crit)
        wolverine.take_damage(dead_dam, dead_crit)


        print(f"Wolverine HP: {wolverine.health}{" "*5}Deadpoll HP: {deadpool.health}")
        if wolverine.health <= 0 or deadpool.health <= 0:
            if wolverine.health > 0 and deadpool.health <= 0:
                print("Wolverine gana")
            elif deadpool.health > 0 and wolverine.health <= 0:
                print("Deadpool gana")
            else:
                print("Ambos han perdido xd!")
            break
        time.sleep(2)

fight()


    