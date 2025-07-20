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

# La clase Warrior se encarga de gestionar los datos de cada guerrero.
# He decidido que las estadisticas de cada guerrero se generen aleatoriamente.
class Warrior:
    def __init__(self, name) -> None:
        self.name = name
        self.speed = random.randint(0, 100)
        self.attack = random.randint(0, 100)
        self.defense = random.randint(0, 100)
        self.health = 100.0

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
    
    def reduce_health(self, hit: float):
        self.health = max(0, self.health - hit)

    def evade_attack(self) -> bool:
        evade = random.randint(1,10)
        if evade == 2 or evade == 9:
            return True
        return False
    
    def is_alive(self) -> bool:
        return self.health > 0
    
    def print_statictics(self):
        print(f"Nombre: {self.name}")
        print(f"\tSpeed: {self.speed}")
        print(f"\tAttack: {self.attack}")
        print(f"\tDefense: {self.defense}")


# La clase Combat strategy sirve como clase padre para las diferentes estrategias de combate.
# en principio utilizo las reglas que se indicaba en el enunciado, pero si quisiera añadir
# nuevas reglas de lucha (pe. el mas veloz ataca con un ratio) con crear una nueva estrategia seria suficiente.
# De esta forma cuple el principio Solid Abierto a extensión, cerrado a modificación.    
class CombatStrategy:
    def decide_turn_order(self, warrior1, warrior2):
        raise NotImplementedError
    
    def perform_attack(self, attacker, defender):
        raise NotImplementedError
    
class DefaultCombatStrategy(CombatStrategy):
    def decide_turn_order(self, warrior1, warrior2):
        if warrior1.get_speed() >= warrior2.get_speed():
            return [warrior1, warrior2]
        else:
            return [warrior2, warrior1]
        
    def perform_attack(self, attacker: Warrior, defender: Warrior):
        print(f"\t{attacker.get_name()} ataca")            
        print(f"\t{defender.get_name()} intenta evadir el ataque.")
        if not defender.evade_attack():
            print(f"\t{defender.get_name()} no consigue evadir el ataque.")
            if defender.get_defense() >= attacker.get_attack():
                damage = attacker.get_minimun_attack()
                print(f"\tLa defensa de {defender.get_name()} es muy fuerte, recibe daño mínimo.")
            else:
                damage = attacker.get_attack() - defender.get_defense()
                print(f"\t{attacker.get_name()} tiene un gran ataque y golpea de lleno.")
            defender.reduce_health(damage)
            return f"\t{attacker.get_name()} ataca y causa {damage} puntos de daño a {defender.get_name()}."
        else:
            return f"\t{defender.get_name()} evade el ataque de {attacker.get_name()}."

    
# Esta clase se encarga de gestionar y ejecutar la batalla entre dos contrincantes.
# gestionando los turnos y utilizando la estrategia de combate indicada,
# devolviendo al final el ganadopr y el perdedor  
class BattleManager:
    def __init__(self, warriors: dict, strategy: CombatStrategy) -> None:
        self.warriors = warriors
        self.strategy = strategy

    def run_fight(self, battle, round):
        warrior_1: Warrior = self.warriors[battle[0]]
        warrior_2: Warrior = self.warriors[battle[1]]

        print(f"{'RONDA':<10} - {round}")
        print(f"{'Batalla:':<10} {warrior_1.get_name():<15} vs {warrior_2.get_name():<15}")
        print(f"{'Velocidad':<10} {warrior_1.get_speed():<15} vs {warrior_2.get_speed():<15}")
        print(f"{'Ataque':<10} {warrior_1.get_attack():<15} vs {warrior_2.get_attack():<15}")
        print(f"{'Defensa':<10} {warrior_1.get_defense():<15} vs {warrior_2.get_defense():<15}")

        turn_order = self.strategy.decide_turn_order(warrior_1, warrior_2)
        turn_cycle = itertools.cycle(turn_order)

        while warrior_1.is_alive() and warrior_2.is_alive():
            attacker = next(turn_cycle)
            defender = next(turn_cycle)
            result = self.strategy.perform_attack(attacker, defender)
            print(result)
            print(f"\t-{warrior_1.get_name()} - {warrior_1.get_health()} PV")
            print(f"\t-{warrior_2.get_name()} - {warrior_2.get_health()} PV")
            next(turn_cycle)# paso de turno para que en la siguiente ronda se cambien los turnos.
            print("")

        if warrior_1.get_health() > 0:
            winner , looser = warrior_1.get_name(), warrior_2.get_name()
            warrior_1.set_health(100)
        else:
            winner, looser = warrior_2.get_name(), warrior_1.get_name()
            warrior_2.set_health(100)

        print(f"{winner} gana la batalla y sigue adelante")
        print(f"{looser} queda eliminado")
        return winner, looser

    
# La clase Tournamet se encarga de gestionar el torneo, sorteando los emparejamiento de cada ronda 
# y lanzando los combates.
class Tournament:
    def __init__(self, participants_names: list, strategy : CombatStrategy):
        self.participants_names = participants_names
        self.warriors = {name : Warrior(name) for name in self.participants_names}
        strategy = DefaultCombatStrategy()
        self.battle_manager = BattleManager(self.warriors, strategy)
        self.battles = []
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

    strategy = DefaultCombatStrategy()
    my_tournamet = Tournament(participants, strategy)
    while len(my_tournamet.participants_names) > 1:
        my_tournamet.set_new_round()
        my_tournamet.fight_round()
    print(f"El ganador del torneo ha sido {my_tournamet.participants_names[0]}")
    print(f"Estadisticas del campeon:")
    my_tournamet.warriors[my_tournamet.participants_names[0]].print_statictics()

main()