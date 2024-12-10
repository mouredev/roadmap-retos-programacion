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


class Damage:
    def __init__(self, min_: int = 10, max_: int = 100):
        self._min = min_
        self._max = max_

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
        self.rests = rests

    # def __eq__(self, other: object) -> bool:
    #     if isinstance(other, Fighter):
    #         return self.name == other.name

    #     return False

    @property
    def name(self):
        return self._name

    @property
    def damage(self):
        return self._damage

    @property
    def evade(self):
        return self._evade

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, life: int):
        self._life = life


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


def get_damage(damage: Damage):
    return randint(damage.min, damage.max)


def winner(fighter: Fighter):
    return fighter.life <= 0


def show_life(fighters: list[Fighter]):
    for fighter in fighters:
        print(f" - Vida de {fighter.name}:", fighter.life)


def fight(current_fighter: Fighter, other_fighter: Fighter) -> bool:
    # Check if current fighter has to rest
    if current_fighter.rests:
        print(f"{current_fighter.name} se está recuperando...")
        current_fighter.rests = False
        return False

    # Calculate the damage value
    damage = get_damage(current_fighter.damage)
    # Check if fighter will need to rest in his next turn
    current_fighter.rests = damage == current_fighter.damage.max
    if current_fighter.rests:
        print(
            f"Golpe crítico! {current_fighter.name} deberá descansar en el siguiente turno..."
        )

    if random() < other_fighter.evade:
        print(f"{other_fighter.name} ha esquivado el ataque!")
    else:
        print(f"{other_fighter.name} ha recibido {damage} puntos de daño!")
        other_fighter.life -= damage
        if other_fighter.life < 0:
            other_fighter.life = 0

    return winner(other_fighter)


def simulate():
    # Create fighters and their data
    fighters: tuple[Fighter] = create_fighters()
    if fighters is None:
        return

    print("\nVidas iniciales:")
    show_life(fighters)

    print("\n¡COMIENZA EL COMBATE!")

    # Select who starts the fight
    turn = fighters[0] if random() < 0.5 else fighters[1]

    turn_counter = 1
    is_winner = False
    while not is_winner:
        print(f"\nTURNO {turn_counter}: {turn.name} ataca!")

        other_fighter = fighters[(fighters.index(turn) + 1) % len(fighters)]

        is_winner = fight(
            current_fighter=turn,
            other_fighter=other_fighter,
        )

        show_life(fighters)

        if is_winner:
            print(f"\n{turn.name.upper()} HA GANADO EL COMBATE!")
            return

        turn = other_fighter
        turn_counter += 1

        sleep(1)


if __name__ == "__main__":
    simulate()
