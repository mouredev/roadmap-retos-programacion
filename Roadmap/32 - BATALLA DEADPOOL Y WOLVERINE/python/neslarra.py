"""
 EJERCICIO:
 ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 Crea un programa que simule la pelea y determine un ganador.
 El programa simula un combate por turnos, donde cada protagonista posee unos
 puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 de regeneración y evasión de ataques.
 Requisitos:
 1. El usuario debe determinar la vida inicial de cada protagonista.
 2. Cada personaje puede impartir un daño aleatorio:
    - Deadpool: Entre 10 y 100.
    - Wolverine: Entre 10 y 120.
 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 4. Cada personaje puede evitar el ataque contrario:
    - Deadpool: 25% de posibilidades.
    - Wolverine: 20% de posibilidades.
 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 Acciones:
 1. Simula una batalla.
 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 3. Muestra qué pasa en cada turno.
 4. Muestra la vida en cada turno.
 5. Muestra el resultado final.
"""
from abc import ABC, abstractmethod
from random import choice
from time import sleep


class AbstractHero(ABC):

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defense(self, hit_power: float):
        pass

    @abstractmethod
    def get_lives_level(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_max_hit_power(self):
        pass


class AbstractFight(ABC):

    @abstractmethod
    def turn(self):
        pass

    @abstractmethod
    def get_turn(self):
        pass

    @abstractmethod
    def combat(self):
        pass


class Hero(AbstractHero):

    def __init__(self, name: str, lives: int, attack_power: dict, defense_pct: float):

        self.name = name
        self.lives = lives
        self.attack_power = attack_power
        self.defense_pct = defense_pct

    def attack(self):
        hit = choice([x for x in self.attack_power.keys()])
        return hit, self.attack_power[hit]

    def defense(self, hit_power: float):
        damage = hit_power * (1 - self.defense_pct / 100)
        self.lives -= damage / 10                           # la potencia del golpe es mucho mayor que las vidas => lo bajo para que dure la pelea

    def get_lives_level(self):
        return self.lives.__round__(2)

    def get_name(self):
        return self.name

    def get_max_hit_power(self):
        return max([x for x in self.attack_power.values()])


class Fight(AbstractFight):

    def __init__(self, hero1: AbstractHero, hero2: AbstractHero):

        self.hero1 = hero1
        self.hero2 = hero2
        self.turn_number = 0
        self.lost_turn = False

    def turn(self):
        self.turn_number += 1

    def get_turn(self):
        return self.turn_number

    def combat(self):
        self.turn()
        if self.get_turn() % 2 == 0:
            if self.lost_turn:
                print(f"\t{self.hero1.get_name()} lost its turn.")
                self.lost_turn = False
            else:
                punch, power = self.hero1.attack()
                self.hero2.defense(power)
                print(f"\t{self.hero1.get_name()} hits with {punch}")
                if power == self.hero1.get_max_hit_power():
                    self.lost_turn = True
        else:
            if self.lost_turn:
                print(f"\t{self.hero2.get_name()} lost its turn.")
                self.lost_turn = False
            else:
                punch, power = self.hero2.attack()
                self.hero1.defense(power)
                print(f"\t{self.hero2.get_name()} hits with {punch}")
                if power == self.hero2.get_max_hit_power():
                    self.lost_turn = True
        print(f"\t{self.hero1.get_name()}'s lives {self.hero1.get_lives_level()}  /  {self.hero2.get_name()}'s lives {self.hero2.get_lives_level()}")


deadpool = Hero("Deadpool", 20, {"left_punch": 10, "right_punch": 20, "left_kick": 30, "right_kick": 40, "up_flying_kick": 50,
                                 "down_flying_kick": 60, "single_pistol": 70, "double_pistol": 80, "single_sword": 100, "double_sword": 100},
                25)
wolverine = Hero("Wolverine", 20, {"left_punch": 10, "right_punch": 20, "left_kick": 30, "right_kick": 40, "up_flying_kick": 50,
                                   "down_flying_kick": 60, "left_knives_up": 90, "right_knives_up": 90, "left_knives_down": 120, "right_knives_down": 120},
                 20)

fight = Fight(deadpool, wolverine)

while deadpool.get_lives_level() > 0 and wolverine.get_lives_level() > 0:
    print(f"Turn# {fight.get_turn() + 1}")
    fight.combat()
    sleep(1)
    if deadpool.get_lives_level() <= 0:
        print(f"{wolverine.get_name()} WON!!!")
    if wolverine.get_lives_level() <= 0:
        print(f"{deadpool.get_name()} WON!!!")

r"""
La salida es algo como ésto:

Turn# 1
    Wolverine hits with left_knives_down
    Deadpool's lives 11.0  /  Wolverine's lives 20
Turn# 2
    Deadpool lost its turn.
    Deadpool's lives 11.0  /  Wolverine's lives 20
Turn# 3
    Wolverine hits with right_knives_up
    Deadpool's lives 4.25  /  Wolverine's lives 20
Turn# 4
    Deadpool hits with right_kick
    Deadpool's lives 4.25  /  Wolverine's lives 16.8
Turn# 5
    Wolverine hits with down_flying_kick
    Deadpool's lives -0.25  /  Wolverine's lives 16.8
Wolverine WON!!!
"""
