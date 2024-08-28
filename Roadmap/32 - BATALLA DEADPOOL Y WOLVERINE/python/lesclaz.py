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

import dataclasses
from random import choice, randint
import time


# Representa un peleador.
@dataclasses.dataclass
class Fighter:

    name: str
    min_damage: int
    max_damage: int
    evasion_possibilities: int
    health_regeneration: int
    life_points: int
    turns: int = 0
    attacks: int = 0
    max_damage_inflicted: int = 0
    min_damage_inflicted: int = 0
    damage_inflicted: int = 0


# Representa un turno en la pelea.
@dataclasses.dataclass
class Turn:

    number: int
    attacker: Fighter
    damage: int

# Representa la pelea
class Fight:

    def __init__(self, fighter_one: Fighter, fighter_two: Fighter) -> None:
        self.fighter_one = fighter_one
        self.fighter_two = fighter_two
        self.current_turn = Turn(1, choice([fighter_one, fighter_two]), 0)
        self.previous_turn = Turn(
            0,
            fighter_one if self.current_turn.attacker == fighter_two else fighter_two,
            0
        )

    @property
    def fighter_attacker(self) -> Fighter:
        return self.fighter_one if self.current_turn.attacker == self.fighter_one else self.fighter_two

    def __attempt_health_regeneration(self) -> None:
        health_generated = randint(0, self.fighter_attacker.health_regeneration + 1)
        if health_generated > 0:
            self.fighter_attacker.life_points += health_generated
            print(f"Se regenera y recupera {health_generated} puntos de vida.")

    def __to_attack(self) -> int:
        damage_receiver = self.fighter_one if self.previous_turn.attacker == self.fighter_one else self.fighter_two
        self.current_turn.damage = randint(10, self.current_turn.attacker.max_damage + 1)
        if randint(1, self.previous_turn.attacker.evasion_possibilities) == 1:
            return 0
        else:
            damage_receiver.life_points -= self.current_turn.damage
            return self.current_turn.damage

    def __switch_turn(self):
        proximo = self.previous_turn.attacker
        self.previous_turn = self.current_turn
        self.current_turn = Turn(self.previous_turn.number + 1, proximo, 0)

    def comment_turn(self) -> None:
        if self.previous_turn.number == 0:
            print("Comienza la pelea!")

        self.fighter_attacker.turns += 1

        print(f"El atacante del turno {self.current_turn.number} es {self.fighter_attacker.name}.")

        if self.previous_turn.damage == self.previous_turn.attacker.max_damage:
            print(f"Pero no ataca por recibir el daño máximo en el turno anterior.\n\n")
            self.__switch_turn()
            return
        else:
            self.__attempt_health_regeneration()
            damage_inflicted = self.__to_attack()
            if damage_inflicted == 0:
                print(f"{self.current_turn.attacker.name} ataca pero {self.previous_turn.attacker.name} logra esquivarlo.\n\n")
            else:
                print(f"{self.current_turn.attacker.name} ataca y provoca un daño de {self.current_turn.damage}.")
                self.fighter_attacker.damage_inflicted += damage_inflicted
                if damage_inflicted > self.fighter_attacker.max_damage_inflicted:
                    self.fighter_attacker.max_damage_inflicted = damage_inflicted
                if damage_inflicted < self.fighter_attacker.min_damage_inflicted or self.fighter_attacker.min_damage_inflicted == 0:
                    self.fighter_attacker.min_damage_inflicted = damage_inflicted
                print(
                    f"Los puntos de vida actual de {self.previous_turn.attacker.name} son "
                    f"{self.previous_turn.attacker.life_points if self.previous_turn.attacker.life_points > 0 else 0}.\n\n"
                )

            self.fighter_attacker.attacks += 1
            if self.fighter_one.life_points > 0 and self.fighter_two.life_points > 0:
                self.__switch_turn()


if __name__ == '__main__':

    def print_fighter_statistics(fighter: Fighter) -> None:
        print(f"Estadisticas de {fighter.name}:")
        print(f"Total de daño infringido al rival :: {fighter.damage_inflicted} en {fighter.turns} turnos.")
        print(f"Ataque más poderoso :: {fighter.max_damage_inflicted} puntos.")
        print(f"Ataque más debil :: {fighter.min_damage_inflicted} puntos.")

    deadpool_life_points = int(input("Introduzca los puntos de vida inicial para Deadpool: "))
    wolverine_life_points = int(input("Introduzca los puntos de vida inicial para Wolverine: "))

    # Peleadores
    deadpool = Fighter("Deadpool", 10, 100, 5, 70, deadpool_life_points)
    wolverine = Fighter("Wolverine", 10, 120, 6, 70, wolverine_life_points)

    # La pelea
    fight = Fight(deadpool, wolverine)

    while fight.fighter_one.life_points > 0 and fight.fighter_two.life_points > 0:
        fight.comment_turn()
        time.sleep(1)

    print(
        f"{fight.current_turn.attacker.name} es el ganador de la pelea! "
        f"Con {fight.current_turn.attacker.life_points} puntos de vida restantes.\n\n"
    )
    print_fighter_statistics(fight.current_turn.attacker)
    print()
    print_fighter_statistics(fight.previous_turn.attacker)
