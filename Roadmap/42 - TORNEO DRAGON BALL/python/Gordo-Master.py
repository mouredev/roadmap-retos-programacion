# 42 - Torneo de Dragon Ball
import random

def is_pow(a: int, b: int):
    if a < 1 or b < 1:
        return False
    if b == 1:
        return a == 1
    
    while a % b == 0:
        a = a // b
    return a == 1

def append_two(elements: list):
    groups = []
    for i in range(0,len(elements),2):
        group = elements[i:i+2]
        groups.append(group)
    return groups


class Figther:

    def __init__(self, name: str, attack: int, defense: int, speed: int):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.health = 100
        self.dodge_chance = 20

class Duel:

    def show_hp(self, figther1: Figther):
        print(f"{figther1.name} tiene {figther1.health} HP")

    def round_duel(self, attacker: Figther, defender: Figther): # Aca esta la logica de como se comporta en cada round las interacciones
        damage = attacker.attack - defender.defense
        if damage <= 0: 
                damage = int(0.1 * attacker.attack)
        if random.random() > (defender.dodge_chance / 100):  # Si esquiva
            defender.health -= damage
            print(f"{attacker.name} ha hecho {damage} daño a {defender.name}")
        else:
            print(f"{defender.name} ha esquivado el ataque!")
        self.show_hp(defender)

    def duel(self, figther1 : Figther, figther2 : Figther): # Este seria el conjunto de rounds hasta que se determine un ganador
        figther1.health = 100
        figther2.health = 100
        print(f"Combate: {figther1.name}({figther1.health}) VS {figther2.name}({figther2.health})")
        count = 0
        while True:
            if figther1.speed > figther2.speed:
                attacker = figther1
                defender = figther2
            elif figther2.speed > figther1.speed:
                attacker = figther2
                defender = figther1
            else:
                aux_list = [figther1, figther2]
                random.shuffle(aux_list)
                attacker, defender = aux_list
            count += 1
            print(f"\nRonda {count}")
            self.round_duel(attacker, defender)
            if defender.health <= 0:
                print(f"{defender.name} ya no puede continuar!")
                print(f"El ganador es {attacker.name}!!")
                return attacker
            count += 1
            print(f"\nRonda {count}")
            self.round_duel(defender,attacker)
            if attacker.health <= 0:
                print(f"{attacker.name} ya no puede continuar!")
                print(f"El ganador es {defender.name}!!")
                return defender


class Tournament:


    def matches(self, *figthers): # Logica del sorteo de los participantes
        if len(figthers) == 1 :
            print(f"Enhorabuena, tenemos un ganador: {figthers[0].name}!!!")
            return
        
        winner_list = []
        if not is_pow(len(figthers),2) :
            print("Cantidad de participante incorrecto. \nSe deben registra cantidades potencia de 2. \nEj: 2, 4, 8, 16, etc")
            return
        else:
            figthers_list = list(figthers)
            random.shuffle(figthers_list)
            figthers_list = append_two(figthers_list)
            for two_f in figthers_list:
                winner = Duel().duel(two_f[0], two_f[1])
                winner_list.append(winner)
                input("Para mostrar el siguiente duelo, presione enter")
            self.matches(*winner_list)


android17 = Figther("Andoide 17", 87, 80, 80)
trunks = Figther("Trunks", attack=85, defense=75, speed=80)
yamcha = Figther("Yamcha", 50, 50, 50)
goku = Figther("Goku", attack=95, defense=85, speed=90)
vegeta = Figther("Vegeta", attack=90, defense=80, speed=85)
gohan = Figther("Gohan", attack=88, defense=82, speed=87)
piccolo = Figther("Piccolo", attack=80, defense=88, speed=70)
frieza = Figther("Frieza", attack=92, defense=78, speed=86)
cell = Figther("Cell", attack=89, defense=83, speed=82)
majin_buu = Figther("Majin Buu", attack=87, defense=90, speed=65)

torneo_artes_marciales = Tournament()

torneo_artes_marciales.matches(goku, vegeta, gohan, piccolo, yamcha, frieza, cell, majin_buu)