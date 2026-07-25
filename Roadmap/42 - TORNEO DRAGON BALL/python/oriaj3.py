"""
 * EJERCICIO:
 * ¡El último videojuego de Dragon Ball ya está aquí!
 * Se llama Dragon Ball: Sparking! ZERO.
 *
 * Simula un Torneo de Artes Marciales, al más puro estilo
 * de la saga, donde participarán diferentes luchadores, y el
 * sistema decidirá quién es el ganador.
 *
 */
"""
from colorama import Fore, Style
import random

# Funciones para imprimir texto con colores
def title(text: str):
    print(f"{Fore.CYAN}{text}{Style.RESET_ALL}")

def result(text: str):
    print(f"{Fore.LIGHTYELLOW_EX}{text}{Style.RESET_ALL}")

def info(text: str):
    print(f"{Fore.WHITE}{text}{Style.RESET_ALL}")

# Clase para definir a los luchadores
# La suma de velocidad, ataque y defensa debe ser 100
class fighter: 

    def __init__(self, name: str, speed: int, attack: int, defense: int):
        if speed < 0 or attack < 0 or defense < 0:
            raise ValueError("Los valores de velocidad, ataque y defensa deben ser positivos")
        if speed + attack + defense != 100:
            raise ValueError("La suma de velocidad, ataque y defensa debe ser 100")
        self.name = name
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.health = 100
# Clase para definir una batalla entre dos luchadores
# Después de las batallas, el luchador ganador recupera 50 de vida
class battle:
    def __init__(self, fighter1: fighter, fighter2: fighter):
        title(f"\n --* Batalla entre {fighter1.name} y {fighter2.name} *--") 
        self.turn = 0
        if fighter1.speed > fighter2.speed:
            self.attacker = fighter1
            self.defender = fighter2
            info(f"{fighter1.name} ataca primero")
        elif fighter1.speed < fighter2.speed:
            self.attacker = fighter2
            self.defender = fighter1
            info(f"{fighter2.name} ataca primero")	
        else:
            random_money = random.randint(1, 2)
            if random_money == 1:
                self.attacker = fighter1
                self.defender = fighter2
                info("A misma velocidad, luchador 1 ataca primero")
            else:
                self.attacker = fighter2
                self.defender = fighter1
                info("A misma velocidad, luchador 2 ataca primero")
    
    def attack(self):
        title(f"\n [Turno {self.turn}]: {self.attacker.name} ataca a {self.defender.name}")
        if self.defender.defense > self.attacker.attack:
            damage = 0.1 * self.attacker.attack
        else:
            damage = self.attacker.attack - self.defender.defense
        squish = random.randint(1, 5)
        if squish == 1:
            damage = 0
            info("El ataque ha fallado")
        else: 
            info(f"{self.attacker.name} ha atacado a {self.defender.name} y le ha hecho {damage} de daño")
        self.defender.health -= damage
        
        info(f"{self.defender.name} tiene {self.defender.health} de vida.") 

    def change_turn(self):
        self.attacker, self.defender = self.defender, self.attacker

    def start(self):
        while self.attacker.health > 0 and self.defender.health > 0:
            self.attack()
            self.change_turn()
            self.turn += 1
        if self.attacker.health > 0:
            result(f"¹... {self.attacker.name} ha ganado")
            #Cuando gana el luchador, se le suma 50 de vida
            self.attacker.health += 50    
        else:
            result(f"¹... {self.defender.name} ha ganado")
            #Cuando gana el luchador, se le suma 50 de vida
            self.defender.health += 50

# Clase para definir un torneo
class tournament:
    def __init__ (self, fighters: list):
        if len(fighters) % 2 != 0:
            raise ValueError("El número de luchadores debe ser par")
        self.fighters = fighters
        self.round = 0
        self.winners = []
        self.loosers = []

    def start(self):
        while len(self.fighters) >= 2:
            self.round += 1
            title(f"\n [*] Ronda {self.round}[*]")
            random.shuffle(self.fighters) # Barajamos los luchadores
            for i in range(0, len(self.fighters), 2):
                batalla = battle(self.fighters[i], self.fighters[i+1])
                batalla.start()
                if self.fighters[i].health > 0:
                    self.winners.append(self.fighters[i])
                    self.loosers.append(self.fighters[i+1])
                else:
                    self.winners.append(self.fighters[i+1])
                    self.loosers.append(self.fighters[i])
            self.fighters = self.winners
            self.winners = []
        result(f"\n 🏁🏁🏁 El torneo ha terminado [*]")
        result(f"🏆🏆🏆 El ganador del torneo es {self.fighters[0].name}")

"""
    * TORNEO DRAGON BALL *
"""

luchador1 = fighter(name="Goku", speed=33, attack=34, defense=33)
luchador2 = fighter(name="Vegeta", speed=34, attack=30, defense=36)
luchador3 = fighter(name="Piccolo", speed=30, attack=35, defense=35)
luchador4 = fighter(name="Krillin", speed=0, attack=50, defense=50)
luchador5 = fighter(name="Yamcha", speed=50, attack=25, defense=25)
luchador6 = fighter(name="Tenshinhan", speed=20, attack=40, defense=40)
luchador7 = fighter(name="Chaoz", speed=24, attack=38, defense=38)
luchador8 = fighter(name="Yajirobe", speed=15, attack=37, defense=48)

torneo = tournament([luchador1, luchador2, luchador3, luchador4, luchador5, luchador6, luchador7, luchador8])
torneo.start()

