"""
 * EJERCICIO:
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista.
 * 2. Cada personaje puede impartir un daño aleatorio:
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario:
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 * Acciones:
 * 1. Simula una batalla.
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 * 3. Muestra qué pasa en cada turno.
 * 4. Muestra la vida en cada turno.
 * 5. Muestra el resultado final.
"""

from random import randint, random
from time import sleep
from typing import Self


class Damage:
    def __init__(self, min_: int = 10, max_: int = 100):
        self._min = min_
        self._max = max_

    def calculate(self):
        return randint(self.min, self.max)

    @property
    def min(self):
        return self._min

    @property
    def max(self):
        return self._max


class Fighter:
    def __init__(
        self,
        name: str,
        damage: Damage,
        evade: float,
        life: int,
        rests: bool = False,
    ):
        self._name = name
        self._damage = damage
        self._evade = evade
        self._life = life
        self._rests = rests

    def attack(self) -> int:
        # Check if current fighter has to rest
        if self._rests:
            print(f"{self.name} se está recuperando...")
            self._rests = False
            return 0

        # Calculate the damage value
        damage = self._damage.calculate()
        # Check if fighter will need to rest in his next turn
        self._rests = damage == self._damage.max
        if self._rests:
            print(
                f"Golpe crítico! {self.name} deberá descansar en el siguiente turno..."
            )

        return damage

    def evade(self, damage: int):
        if random() < self._evade:
            print(f"{self.name} ha esquivado el ataque!")
        else:
            print(f"{self.name} ha recibido {damage} puntos de daño!")
            self._update_life(damage)

    def _update_life(self, damage: int):
        self._life -= damage
        if self._life < 0:
            self._life = 0

    @property
    def name(self):
        return self._name

    @property
    def life(self):
        return self._life


D = "Deadpool"
W = "Wolverine"


def ask_life(fighter: str) -> int | None:
    while True:
        try:
            print("\nPuedes pulsar Q para salir.")
            message = f"Introduce la vida de {fighter}:\n > "

            num = input(message)
            if num.lower() == "q":
                return

            assert (
                num.replace(".", "", 1).isnumeric() and int(num) >= 1
            ), f"Debes introducir un número positivo."

        except AssertionError as error:
            print(error)

        else:
            return int(num)


def create_fighters() -> tuple[Fighter, Fighter] | None:
    # Definir Deadpool
    life = ask_life(fighter=D)
    if life is None:
        return

    deadpool = Fighter(
        name=D, damage=Damage(min_=10, max_=100), evade=0.25, life=life
    )

    # Definir Wolverine
    life = ask_life(fighter=W)
    if life is None:
        return

    wolverine = Fighter(
        name=W, damage=Damage(min_=10, max_=120), evade=0.2, life=life
    )

    return deadpool, wolverine


def is_winner(fighters: tuple[Fighter]):
    return any([fighter.life <= 0 for fighter in fighters])


def show_life(fighters: list[Fighter]):
    for fighter in fighters:
        print(f" - Vida de {fighter.name}:", fighter.life)


def simulate():
    # Create fighters and their data
    fighters: tuple[Fighter] = create_fighters()
    if fighters is None:
        return

    print("\nVidas iniciales:")
    show_life(fighters)

    print("\n¡COMIENZA EL COMBATE!")

    # Select who starts the fight
    current_fighter = fighters[0] if random() < 0.5 else fighters[1]

    turn_counter = 1
    while not is_winner(fighters):
        print(f"\nTURNO {turn_counter}: {current_fighter.name} ataca!")

        other_fighter = fighters[
            (fighters.index(current_fighter) + 1) % len(fighters)
        ]

        damage = current_fighter.attack()
        if damage:
            other_fighter.evade(damage)

        show_life(fighters)

        if is_winner(fighters):
            print(f"\n{current_fighter.name.upper()} HA GANADO EL COMBATE!")
            return

        current_fighter = other_fighter
        turn_counter += 1

        sleep(1)


if __name__ == "__main__":
    simulate()
