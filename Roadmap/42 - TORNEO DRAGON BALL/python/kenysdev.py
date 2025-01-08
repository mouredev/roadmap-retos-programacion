# _____________________________________
# https://github.com/kenysdev
# 2024 - Python
# _____________________________________
# 42 TORNEO DRAGON BALL
# ------------------------------------

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
import math

class Fighter:
    def __init__(self, name: str, speed: int, attack: int, defense: int):
        self._name: str = name
        self._speed: int = speed
        self._attack: int = attack
        self._defense: int = defense
        self._health: float = 100

    def execute_attack(self, opponent):
        print(f"'{self._name}' ataca a '{opponent._name}'")
        
        damage: float = 0
        if opponent._defense >= self._attack:
            damage = self._attack * 0.1 # 10%
        else: 
            damage = self._attack - opponent._defense

        if not opponent.activate_defense():
            opponent._health -= damage
            print(f"'{opponent._name}' ha recibido '{damage}' de daño")
            print(f"Salud restante '{opponent._health}'\n")
        else:    
            print(f"'{opponent._name}' ha esquivado el ataque.\n")
    
    def activate_defense(self) -> bool:
        return random.random() <= 0.2  # 20%

# __________________________________________________________
class Battle:
    def __init__(self, fighter1, fighter2):
        self._fighter1 = fighter1
        self._fighter2 = fighter2
        print(f"__'{self._fighter1._name} VS '{self._fighter2._name}'__\n")

    def __combat(self, fighter_a, fighter_b) -> Fighter:
        while True:
            fighter_a.execute_attack(fighter_b)
            if fighter_b._health <= 0:
                print(f"--> '{fighter_a._name}' gana la batalla.__\n")
                return fighter_a

            fighter_b.execute_attack(fighter_a)
            if fighter_a._health <= 0:
                print(f"--> '{fighter_b._name}' gana la batalla.\n")
                return fighter_b

    def start(self) -> Fighter:
        if self._fighter1._speed > self._fighter2._speed:
            return self.__combat(self._fighter1, self._fighter2)
        else:
            return self.__combat(self._fighter2, self._fighter1)
            
# __________________________________________________________
class Tournament:
    def __init__(self, fighter, battle, fighters: dict):
        self._fighter = fighter
        self._battle = battle
        self._fighters: dict = fighters

    def __is_power_of_2(self) -> bool:
        n: int = len(self._fighters)
        if n <= 1:
            return False
        return math.log2(n).is_integer()

    def __get_random_pairs(self) -> tuple:
        fighters_random = random.sample(list(self._fighters.keys()), 2)
        fighter1_data = {**self._fighters[fighters_random[0]], 'name': fighters_random[0]}
        fighter2_data = {**self._fighters[fighters_random[1]], 'name': fighters_random[1]}

        fighter1 = self._fighter(**fighter1_data)
        fighter2 = self._fighter(**fighter2_data)

        del self._fighters[fighters_random[0]]
        del self._fighters[fighters_random[1]]

        return fighter1, fighter2

    def start_rounds(self, round_num = 1):
        if not self.__is_power_of_2():
            print("El número de luchadores debe ser una potencia de 2.")
            return

        print(f"\n__Ronda #{round_num}__")
        next_round: dict = {}
        while True:
            fighter1, fighter2 = self.__get_random_pairs()
            battle = self._battle(fighter1, fighter2)
            winner = battle.start()

            next_round[winner._name] = {
                "speed": winner._speed, 
                "attack": winner._attack, 
                "defense": winner._defense
            }

            if len(self._fighters) == 0 and len(next_round) > 1:
                self._fighters = next_round
                self.start_rounds(round_num + 1)
                break
            
            if len(self._fighters) == 0 and len(next_round) == 1:
                print(f"\n--> El vencedor del torneo es '{winner._name}'.")
                break        

# __________________________________________________________
FIGHTERS: dict = {
    "Goku": {"speed": 100, "attack": 95, "defense": 85},
    "Vegeta": {"speed": 95, "attack": 90, "defense": 90},
    "Gohan": {"speed": 85, "attack": 95, "defense": 85},
    "Freezer": {"speed": 90, "attack": 90, "defense": 90},
    "Piccolo": {"speed": 90, "attack": 85, "defense": 90},
    "Krillin": {"speed": 85, "attack": 75, "defense": 75},
    "Cell": {"speed": 90, "attack": 95, "defense": 85},
    "Majin Buu": {"speed": 80, "attack": 85, "defense": 95},
}

if __name__ == "__main__":
    print("Simulación del Torneo de Artes Marciales")
    tournament = Tournament(Fighter, Battle, FIGHTERS)
    tournament.start_rounds()

# end
