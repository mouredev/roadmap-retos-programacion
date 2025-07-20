"""
 * EJERCICIO:
 * ¡El último videojuego de Dragon Ball ya está aquí!
 * Se llama Dragon Ball: Sparking! ZERO.
 *
 * Simula un Torneo de Artes Marciales, al más puro estilo
 * de la saga, donde participarán diferentes luchadores, y el
 * sistema decidirá quién es el ganador.
 *
 * Luchadores:
 * - Nombre.
 * - Tres atributos: velocidad, ataque y defensa
 *   (con valores entre 0 a 100 que tú decidirás).
 * - Comienza cada batalla con 100 de salud.
 * Batalla:
 * - En cada batalla se enfrentan 2 luchadores.
 * - El luchador con más velocidad comienza atacando.
 * - El daño se calcula restando el daño de ataque del
 *   atacante menos la defensa del oponente.
 * - El oponente siempre tiene un 20% de posibilidad de
 *   esquivar el ataque.
 * - Si la defensa es mayor que el ataque, recibe un 10%
 *   del daño de ataque.
 * - Después de cada turno y ataque, el oponente pierde salud.
 * - La batalla finaliza cuando un luchador pierde toda su salud.
 * Torneo:
 * - Un torneo sólo es válido con un número de luchadores
 *   potencia de 2.
 * - El torneo debe crear parejas al azar en cada ronda.
 * - Los luchadores se enfrentan en rondas eliminatorias.
 * - El ganador avanza a la siguiente ronda hasta que sólo
 *   quede uno.
 * - Debes mostrar por consola todo lo que sucede en el torneo,
 *   así como el ganador.
"""

import random
import json
import itertools

# He decidido que las estadisticas de cada guerrero se generen aleatoriamente.
class Warrior:
    def __init__(self, name) -> None:
        self.name = name
        self.speed = random.randint(0, 100)
        self.attack = random.randint(0, 100)
        self.defense = random.randint(0, 100)
        self.health = 100

    def get_name(self):
        return self.name

    def get_speed(self):
        return self.speed
    
    def get_attack(self):
        return self.attack
    
    def get_minimun_attack(self):
        return self.attack * 0.1
    
    def get_defense(self):
        return self.defense
    
    def get_health(self):
        return self.health
    
    def set_health(self, new_health):
        self.health = new_health
    
    def reduce_health(self, hit: int):
        self.health = max(0, self.health - hit)

    def evade_attack(self) -> bool:
        evade = random.randint(1,10)
        if evade == 2 or evade == 9:
            return True
        return False
    
    def is_alive(self) -> bool:
        return self.health > 0
    
    def to_dict(self):
        return {
            "name": self.name,
            "speed": self.speed,
            "attack": self. attack,
            "defense": self.defense,
            "heath": self.health
        }
    

class BattleManager:
    def __init__(self, warriors: dict) -> None:
        self.warriors = warriors

    def run_fight(self, battle, round):
        warrior_1 = self.warriors[battle[0]]
        warrior_2 = self.warriors[battle[1]]
        print(f"RONDA - {round}")
        print(f"Batalla: {warrior_1.get_name()} vs {warrior_2.get_name()}")
        print(f"{json.dumps(warrior_1.to_dict(),indent=2)} Vs {json.dumps(warrior_2.to_dict(),indent=2)}")
        if warrior_1.get_speed() >= warrior_2.get_speed():
            print(f"\t{warrior_1.get_name()} es más rápido y empieza la batalla")
            turn = [warrior_1, warrior_2]
        else:
            print(f"\t{warrior_2.get_name()} es más rápido y empieza la batalla")
            turn = [warrior_2, warrior_1]
        turn_cycle = itertools.cycle(turn)
        while warrior_1.is_alive() and warrior_2.is_alive():
            active_warrior = next(turn_cycle)
            active_warrior_name = active_warrior.get_name()
            print(f"\t{active_warrior_name} ataca")
            pasive_warrior = next(turn_cycle)
            pasive_warrior_name = pasive_warrior.get_name()
            print(f"\t{pasive_warrior_name} intenta evadir el ataque.")
            if not pasive_warrior.evade_attack():
                print(f"\t{pasive_warrior_name} no consigue evadir el ataque.")
                if pasive_warrior.get_defense() >= active_warrior.get_attack():
                    attack = active_warrior.get_minimun_attack()
                    pasive_warrior.reduce_health(attack)
                    print(f"\tLa defensa de {pasive_warrior_name} es muy fuerte, sólo recibe {attack} puntos de daño.")
                else:
                    attack = active_warrior.get_attack() - pasive_warrior.get_defense()
                    pasive_warrior.reduce_health(attack)
                    print(f"\t{active_warrior_name} realiza un buen ataque y le golpea con {attack} puntos de ataque")
            else:
                print(f"\t{pasive_warrior_name} consigue evadir el ataque. No recibe daño")
            next(turn_cycle)# paso de turno para que en la siguiente ronda se cambien los turnos.
            print(f"\t-{warrior_1.get_name()} - {warrior_1.get_health()} PV")
            print(f"\t-{warrior_2.get_name()} - {warrior_2.get_health()} PV")
            print("")
        if warrior_1.get_health() > 0:
            winner = warrior_1.get_name()
            warrior_1.set_health(100)
            looser = warrior_2.get_name()
        else:
            winner = warrior_2.get_name()
            warrior_2.set_health(100)
            looser = warrior_1.get_name()
        print(f"{winner} gana la batalla y sigue adelante")
        print(f"{looser} queda eliminado")
        return winner, looser

    

class Tournament:
    def __init__(self, participants_names: list):
        self.participants_names = participants_names
        self.warriors = {name : Warrior(name) for name in self.participants_names}
        self.battles = []
        self.battle_manager = BattleManager(self.warriors)
        self.round = 0

    def set_new_round(self):
        self.battles.clear()
        self.round += 1 
        while self.participants_names:
            p1 = self.participants_names.pop(random.randint(0, len(self.participants_names) - 1))
            p2 = self.participants_names.pop(random.randint(0, len(self.participants_names) - 1))
            self.battles.append((p1, p2))

    def fight_round(self):
        for battle in self.battles:
            winner , looser = self.battle_manager.run_fight(battle, self.round)
            self.participants_names.append(winner)



def main():

    participants = [
        "Goku", "Vegeta", "Gohan", "Piccolo", "Krillin", "Trunks", "Bulma", "Freezer",
        "Cell", "Majin Buu", "Yamcha", "Tien", "Chiaotzu", "Master Roshi", "Chi-Chi",
        "Android 18", "Android 17", "Android 16", "Bardock", "Raditz", "Nappa", "Videl",
        "Hercule", "Pan", "Goten", "King Kai", "Supreme Kai", "Kibito", "Dende", "Korin",
        "Yajirobe", "Shenron", "Whis", "Beerus", "Jiren", "Hit", "Zamasu", "Goku Black",
        "Fused Zamasu", "Future Trunks", "Broly (DBZ)", "Broly (DB Super)", "Paragus",
        "Kale", "Caulifla", "Cabba", "Toppo", "Dyspo", "Granolah", "Moro", "Gas", "Merus",
        "Zeno", "Grand Priest", "King Cold", "Cooler", "Garlic Jr.", "Bojack", "Janemba",
        "Tapion", "Dabura", "Pikkon", "Arale", "Uub", "Launch", "Pilaf", "Mai", "Shu",
        "Dr. Gero", "Dr. Briefs", "Android 19", "Android 13", "Android 14", "Android 15",
        "Android 21", "Turles", "Lord Slug", "Zarbon", "Dodoria", "Recoome", "Burter",
        "Jeice", "Guldo", "Captain Ginyu", "Babidi", "Sorbet", "Tagoma", "Jaco", "Monaka",
        "Vados", "Champa", "Basil", "Lavender", "Bergamo", "Ribrianne", "Kakunsa", "Rozie",
        "Cumber", "Fu", "Hearts", "Omega Shenron", "Syn Shenron", "Nova Shenron",
        "Eis Shenron", "Haze Shenron", "Oceanus Shenron", "Rage Shenron", "Naturon Shenron",
        "Baby", "General Rilldo", "Dr. Myuu", "Super 17", "Vegeta Jr.", "Goku Jr.",
        "Majuub", "Puar", "Oolong", "Gregory", "Bubbles", "Fortuneteller Baba", "Annin",
        "Princess Snake", "Gine", "Cell Jr.", "Zarama", "Moro's Goons", "Granolahs mother",
        "OG73-I"
    ]

    print(f"Cuantos guerreros quieres que participen en el torneo?")
    print(f"1: 2 Participantes")
    print(f"2: 4 Participantes")
    print(f"3: 8 Participantes")
    print(f"4: 16 Participantes")
    print(f"5: 32 Participantes")
    print(f"6: 64 Participantes")
    print(f"7: 128 Participantes")
    number_of_participants = int(input(" Introduce la opción: "))
    participants = participants[0 : 2 ** number_of_participants]

    my_tournamet = Tournament(participants)
    while len(my_tournamet.participants_names) > 1:
        my_tournamet.set_new_round()
        my_tournamet.fight_round()
    print(f"El ganador del torneo ha sido {my_tournamet.participants_names[0]}")
    print(f"Estadisticas del campeon: {my_tournamet.warriors[my_tournamet.participants_names[0]].to_dict()}")

main()