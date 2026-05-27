# @Author Daniel Grande (Mhayhem)

# EJERCICIO:
# ¡El último videojuego de Dragon Ball ya está aquí!
# Se llama Dragon Ball: Sparking! ZERO.
#
# Simula un Torneo de Artes Marciales, al más puro estilo
# de la saga, donde participarán diferentes luchadores, y el
# sistema decidirá quién es el ganador.
#
# Luchadores:
# - Nombre.
# - Tres atributos: velocidad, ataque y defensa
#   (con valores entre 0 a 100 que tú decidirás).
# - Comienza cada batalla con 100 de salud.
# Batalla:
# - En cada batalla se enfrentan 2 luchadores.
# - El luchador con más velocidad comienza atacando.
# - El daño se calcula restando el daño de ataque del
#   atacante menos la defensa del oponente.
# - El oponente siempre tiene un 20% de posibilidad de
#   esquivar el ataque.
# - Si la defensa es mayor que el ataque, recibe un 10%
#   del daño de ataque.
# - Después de cada turno y ataque, el oponente pierde salud.
# - La batalla finaliza cuando un luchador pierde toda su salud.
# Torneo:
# - Un torneo sólo es válido con un número de luchadores
#   potencia de 2.
# - El torneo debe crear parejas al azar en cada ronda.
# - Los luchadores se enfrentan en rondas eliminatorias.
# - El ganador avanza a la siguiente ronda hasta que sólo
#   quede uno.
# - Debes mostrar por consola todo lo que sucede en el torneo,
#   así como el ganador.

import random

class Fighter:
    def __init__(self, name: str, speed: int, attack: int, defense: int):
        self.name = name.capitalize()
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.health = 0

def random_attributes() -> int:
    return random.randint(0, 100)

def is_power_of_two(num):
    return num >= 2 and (num & (num - 1)) == 0

def set_num_participants() -> list:
    participants = []
    while True:
        num = int(input("Indique un número\n"))
        if is_power_of_two(num):
            break
        else:
            print("Comprueba que el numero sea potencia de 2.")
    
    while len(participants) < num:
        num_fighter = 1
        name = input(f"nombre del luchador {num_fighter}: ")
        speed = random_attributes()
        attack = random_attributes()
        defense = random_attributes()
        
        fighter = Fighter(name, speed, attack, defense)
        
        participants.append(fighter)
        num_fighter += 1
    
    return participants

def select_fighters(array) -> object:
    fighter_1, fighter_2 = random.sample(array, 2)
    array.remove(fighter_1)
    array.remove(fighter_2)
    return fighter_1, fighter_2



def check_evasion() -> bool:
    return random.random() < 0.2

def damage(fighter_defense: object, fighter_attack: object) -> list:
    print(f"Ataca {fighter_attack.name} su poder de ataque es {fighter_attack.attack}.")
    if fighter_defense.defense > fighter_attack.attack:
        damage_attack = fighter_attack.attack * 0.1
    else:
        damage_attack = fighter_attack.attack - fighter_defense.defense
    return damage_attack

def Kombat(fighter_1: object, fighter_2: object, array: list):
    if fighter_2.speed > fighter_1.speed:
        fighter_1, fighter_2 = fighter_2, fighter_1
    
    fighter_1.health = 100
    fighter_2.health = 100
    round = 0
    
    while True:
        round += 1
        input("Pulsar enter.")
        print(f"Round - {round}\n"
            f"{fighter_1.name} {fighter_1.health} VS {fighter_2.name} {fighter_2.health}\n")
        
        if check_evasion():
            print(f"{fighter_2.name} esquiva el ataque.\n")
            
        else:
            fighter_1_damage = int(damage(fighter_2, fighter_1))
            print(f"{fighter_2.name} recibe {fighter_1_damage} puntos de daño.\n")
            fighter_2.health -= fighter_1_damage
            if fighter_2.health < 0:
                fighter_2.health = 0
                
        if fighter_2.health == 0:
            break
        
        if  check_evasion():
            print(f"{fighter_1.name} esquiva el ataque.\n")
            
        else:
            fighter_2_damage = int(damage(fighter_1, fighter_2))
            print(f"{fighter_1.name} recibe {fighter_2_damage} puntos de daño.\n")
            fighter_1.health -= fighter_2_damage
            if fighter_1.health < 0:
                fighter_1.health = 0
                
        if fighter_1.health == 0:
            break
        
    if fighter_1.health == 0:
            print(f"El ganador es {fighter_2.name} en la ronda {round}")
            array.append(fighter_2)
    else:
        print(f"El ganador es {fighter_1.name} en la ronda {round}")
        array.append(fighter_1)
    
    
    return array

def main():
    fighters = set_num_participants()
    new_phase = []
    print("¡Va a comenzar el torneo mundial de artes marciales!\n"
        f"Con un total de {len(fighters)} participantes\n")
    print("Los combates seran entre dos luchadores, quien gane pasara a la siguiente fase.\n"
        "Empecemos con los combates.\n")
    phase = 1
    kombat_num = 1
    while True:
        print(f"Combate {kombat_num}")
        fighter_1, fighter_2 = select_fighters(fighters)
        Kombat(fighter_1, fighter_2,new_phase)
        kombat_num += 1
        if len(fighters) == 0:
            if len(new_phase) > 1:
                fighters = new_phase.copy()
                new_phase.clear()
                phase += 1
            else:
                print("¡¡¡¡¡Torneo terminado!!!!!\n"
                    f"EL ganador es {new_phase[0].name}")
                break

if __name__=="__main__":
    main()