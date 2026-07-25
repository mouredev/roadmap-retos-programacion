"""
Programa que simula una pelea y determina un ganador
- Simula un combate por turnos

Personaje (2)
- Puntos de vida iniciales (1000 puntos)

- Daño de ataque variable
    - Deadpool: entre 10 y 100 puntos
    - Wolverine: entre 10 y 120 puntos
    - Si el daño que ejecuta el atacante es maximo, le vuelve a tocar en el turno siguiente atacar.
        - El oponente se tiene que regenerar, pero sin aumentar vida

- Regeneracion
- Evasión de ataques
    - Deadpool: 25% de posibilidades
    - Wolverine: 20% de posibilidades

- Un personaje pierde si sus puntos de vida llegan a cero o menos.

Acciones:
1. Simula una batalla
2. Muestra el numero del turno (pausa de 1 segundo entre turnos)
3. Muestra que pasa en cada turno
4. Muestra la vida en cada turno
5. Muestra el resultado final
"""

import random
from abc import ABC, abstractmethod
from time import sleep


class Hero(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def attack(self, turn_counter: int) -> int:
        pass

    @abstractmethod
    def evade(self) -> bool:
        pass


class Deadpool(Hero):
    def __init__(self):
        self.name = "Deadpool"
        self.health = 1000
        self.min_damage = 10
        self.max_damage = 100
        self.prob_evade = 25
        self.special_attack_turn = 3

    def attack(self, turn_counter: int) -> int:
        """
        Calcula el daño de un ataque generando un número aleatorio.
        - Si el turno es multiplo de 3, ejecuta un ataque especial con el máximo de daño.

        Returns:
            int: Puntos de daño infligidos (entre 10 y 100).
        """

        if turn_counter % self.special_attack_turn == 0:
            return self.max_damage
        else:
            return random.randint(self.min_damage, self.max_damage)

    def evade(self) -> bool:
        """
        Decide si el personaje evade el ataque del oponente en función de su porcentaje de evasión.

        Returns:
            bool: True si evade el ataque, False si no lo hace.
        """
        prob_evasion = random.randint(1, 100)

        if prob_evasion <= self.prob_evade:
            return True
        else:
            return False

    def __str__(self) -> str:
        """
        Retorna el estado del personaje

        Returns:
            str: Estado del personaje
        """
        return f"{self.name} tiene una vida de {self.health} puntos."


class Wolverine(Hero):
    def __init__(self):
        self.name = "Wolverine"
        self.health = 1000
        self.min_damage = 10
        self.max_damage = 120
        self.prob_evade = 20
        self.special_attack_turn = 4

    def attack(self, turn_counter: int) -> int:
        if turn_counter % self.special_attack_turn == 0:
            return self.max_damage
        else:
            return random.randint(self.min_damage, self.max_damage)

    def evade(self) -> bool:
        prob_evasion = random.randint(1, 100)

        if prob_evasion <= self.prob_evade:
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"{self.name} tiene una vida de {self.health} puntos."


class View:
    def display_msg(self, msg: str):
        print(msg)

    def display_err(self, err: str):
        print(f"\nERROR: {err}")


class Fight:
    def __init__(self, deadpool: Hero, wolverine: Hero, view: View):
        self.deadpool = deadpool
        self.wolverine = wolverine
        self.view = view
        self.turn_counter = 0

    def who_starts(self) -> Hero:
        """
        Sirve para elegir que personaje comienza atacando en la batalla.

        Returns:
            Hero,Hero: Retorna el primero el que empieza atacando y seguido el que empieza defendiendo.
        """
        result = random.randint(1, 2)
        if result == 1:
            first = self.deadpool
            second = self.wolverine
            return first, second

        else:
            first = self.wolverine
            second = self.deadpool
            return first, second

    def _execute_attack(self, first_opp: Hero, second_opp: Hero, first_opp_damage: int) -> bool:
        """
        Ejecuta un ataque de un heroe.

        Returns:
            bool: retorna True si el ataque fue máximo, False si no lo fue
        """
        self.view.display_msg(
            f"- {first_opp.name} lanzo un ataque de {first_opp_damage} puntos de daño"
        )

        if first_opp_damage == first_opp.max_damage:
            second_opp.health -= first_opp_damage

            self.view.display_msg(f"\t- {first_opp.name} uso su ataque con el máximo daño posible.")
            self.view.display_msg(
                f"\t- {second_opp.name} no puede atacar, se esta recuperando del daño sufrido."
            )
            self.view.display_msg(f"\t- {second_opp}\n")

            return True

        else:
            if second_opp.evade():
                self.view.display_msg(f"\t- {second_opp.name} esquivo el ataque.")
                self.view.display_msg(f"\t- {second_opp}\n")

            else:
                second_opp.health -= first_opp_damage

                self.view.display_msg(f"\t- {second_opp}\n")

            return False

    def turn(self, first_opponent: Hero, second_opponent: Hero) -> Hero:
        """
        Desarrolla un turno de la batalla.
        - Calcula los daños de los heroes
        - Ejecuta la funcion de ataque

        Returns:
            Hero: retorna el siguiente orden de los oponentes.
        """
        sleep(1)

        self.turn_counter += 1
        self.view.display_msg(f"\nComienza el turno: {self.turn_counter}.")

        # Calculo los daños de los ataques en funcion de los turnos
        first_opponent_damage = first_opponent.attack(self.turn_counter)
        second_opponent_damage = second_opponent.attack(self.turn_counter)

        # Ataca el primer oponente
        max_attack_result = self._execute_attack(
            first_opponent, second_opponent, first_opponent_damage
        )
        if max_attack_result:
            return first_opponent, second_opponent

        if second_opponent.health <= 0:
            return first_opponent, second_opponent

        # Ataca el segundo oponente
        max_attack_result = self._execute_attack(
            second_opponent, first_opponent, second_opponent_damage
        )
        if max_attack_result:
            return second_opponent, first_opponent

        return first_opponent, second_opponent


def main():
    deadpool = Deadpool()
    wolverine = Wolverine()
    view = View()
    fight = Fight(deadpool, wolverine, view)

    view.display_msg("\nBATALLA ENTRE DEADPOOL Y WOLVERINE")

    first_opponent, second_opponent = fight.who_starts()

    while first_opponent.health > 0 and second_opponent.health > 0:
        first_opponent, second_opponent = fight.turn(first_opponent, second_opponent)

    if first_opponent.health <= 0 and second_opponent.health > 0:
        view.display_msg(f"\n{second_opponent.name} ha ganado la batalla.")

    elif second_opponent.health <= 0 and first_opponent.health > 0:
        view.display_msg(f"\n{first_opponent.name} ha ganado la batalla.")


if __name__ == "__main__":
    main()
