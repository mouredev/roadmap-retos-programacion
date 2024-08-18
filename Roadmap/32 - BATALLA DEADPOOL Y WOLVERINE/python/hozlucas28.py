# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring


from abc import ABCMeta, abstractmethod
from random import randint
from typing import Self, TypedDict

import asyncio

# ---------------------------------------------------------------------------- #
#                      SUPERHEROREGENERATINGERROR (ERROR)                      #
# ---------------------------------------------------------------------------- #


class SuperheroRegeneratingException(Exception):
    def __init__(self, *, superhero: "AbcSuperhero") -> None:
        super().__init__(f"{superhero.name} is regenerating")


# ---------------------------------------------------------------------------- #
#                               SUPERHERO (CLASS)                              #
# ---------------------------------------------------------------------------- #

type AttackDamage = tuple[int, int]


class AbcSuperhero(metaclass=ABCMeta):
    @property
    @abstractmethod
    def life_points(self) -> int:
        pass

    @property
    @abstractmethod
    def regenerating(self) -> bool:
        pass

    @property
    @abstractmethod
    def attack_damage(self) -> AttackDamage:
        pass

    @property
    @abstractmethod
    def evade_percentage(self) -> int:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def set_regenerating(self, regenerating: bool) -> Self:
        pass

    @abstractmethod
    def evade_attack(self) -> bool:
        pass

    @abstractmethod
    def produce_damage(self) -> int:
        pass

    @abstractmethod
    def receive_damage(self, damage: int) -> Self:
        pass


class Superhero(AbcSuperhero):
    __life_points: int
    __regenerating: bool
    __attack_damage: AttackDamage
    __evade_percentage: int
    __name: str

    def __init__(
        self,
        *,
        life_points: int,
        attack_damage: AttackDamage,
        evade_percentage: int,
        name: str,
    ) -> None:
        self.__life_points = life_points
        self.__regenerating = False
        self.__attack_damage = attack_damage
        self.__evade_percentage = evade_percentage
        self.__name = name

    @property
    def life_points(self) -> int:
        return self.__life_points

    @property
    def regenerating(self) -> bool:
        return self.__regenerating

    @property
    def attack_damage(self) -> AttackDamage:
        return self.__attack_damage

    @property
    def evade_percentage(self) -> int:
        return self.__evade_percentage

    @property
    def name(self) -> str:
        return self.__name

    def set_regenerating(self, regenerating: bool) -> Self:
        self.__regenerating = regenerating
        return self

    def evade_attack(self) -> bool:
        rnd_int: int = randint(a=0, b=100)
        return rnd_int <= self.__evade_percentage

    def produce_damage(self) -> int:
        if self.__regenerating:
            raise SuperheroRegeneratingException(superhero=self)

        [min_attack_damage, max_attack_damage] = self.attack_damage
        rnd_damage: int = randint(a=min_attack_damage, b=max_attack_damage)
        return rnd_damage

    def receive_damage(self, damage: int) -> Self:
        self.__life_points -= damage
        return self


# ---------------------------------------------------------------------------- #
#                               WOLVERINE (CLASS)                              #
# ---------------------------------------------------------------------------- #


class Wolverine(Superhero):
    def __init__(self, *, life_points: int) -> None:
        super().__init__(
            life_points=life_points,
            attack_damage=(10, 120),
            evade_percentage=20,
            name="Wolverine",
        )


# ---------------------------------------------------------------------------- #
#                               DEADPOOL (CLASS)                               #
# ---------------------------------------------------------------------------- #


class Deadpool(Superhero):
    def __init__(self, *, life_points: int) -> None:
        super().__init__(
            life_points=life_points,
            attack_damage=(10, 100),
            evade_percentage=25,
            name="Deadpool",
        )


# ---------------------------------------------------------------------------- #
#                           SUPERHEROESFIGHT (CLASS)                           #
# ---------------------------------------------------------------------------- #


class Turn(TypedDict):
    attacker: AbcSuperhero
    number: int
    victim: AbcSuperhero


class ExecutedTurn(Turn):
    damage_produced_by_attacker: int
    damage_received_by_victim: int
    victim_avoid_attack: bool


class AbcSuperheroesFight(metaclass=ABCMeta):
    @property
    @abstractmethod
    def turn(self) -> Turn:
        pass

    @property
    @abstractmethod
    def winner(self) -> None | AbcSuperhero:
        pass

    @abstractmethod
    def execute_turn(self) -> ExecutedTurn:
        pass


class SuperheroesFight(AbcSuperheroesFight):
    __turn: Turn
    __winner: None | AbcSuperhero

    def __init__(
        self, *, superhero_one: AbcSuperhero, superhero_two: AbcSuperhero
    ) -> None:
        self.__turn = {
            "attacker": superhero_one,
            "number": 1,
            "victim": superhero_two,
        }

        self.__winner = None

    @property
    def turn(self) -> Turn:
        return self.__turn

    @property
    def winner(self) -> None | AbcSuperhero:
        return self.__winner

    def execute_turn(self) -> ExecutedTurn:
        turn: Turn = self.turn
        attacker: AbcSuperhero = turn["attacker"]
        number: int = turn["number"]
        victim: AbcSuperhero = turn["victim"]

        victim.set_regenerating(regenerating=False)

        self.__turn = {
            "attacker": victim,
            "number": number + 1,
            "victim": attacker,
        }

        try:
            damage_produced_by_attacker: int = attacker.produce_damage()
            attacker_attack_damage: AttackDamage = attacker.attack_damage

            victim_avoid_attack: bool = victim.evade_attack()

            if victim_avoid_attack:
                return {
                    "attacker": attacker,
                    "damage_produced_by_attacker": damage_produced_by_attacker,
                    "damage_received_by_victim": 0,
                    "number": number,
                    "victim": victim,
                    "victim_avoid_attack": victim_avoid_attack,
                }

            victim.receive_damage(damage_produced_by_attacker)
            victim.set_regenerating(
                regenerating=damage_produced_by_attacker == attacker_attack_damage[1]
            )

            if victim.life_points <= 0:
                self.__winner = attacker

            return {
                "attacker": attacker,
                "damage_produced_by_attacker": damage_produced_by_attacker,
                "damage_received_by_victim": damage_produced_by_attacker,
                "number": number,
                "victim": victim,
                "victim_avoid_attack": victim_avoid_attack,
            }

        except SuperheroRegeneratingException as error:
            raise error


# ---------------------------------------------------------------------------- #
#                                     MAIN                                     #
# ---------------------------------------------------------------------------- #


async def main() -> None:
    deadpool: Deadpool = Deadpool(life_points=500)
    wolverine: Wolverine = Wolverine(life_points=500)

    superheroes_fight: SuperheroesFight = SuperheroesFight(
        superhero_one=deadpool, superhero_two=wolverine
    )

    while superheroes_fight.winner is None:
        await asyncio.sleep(delay=1)
        current_turn: Turn = superheroes_fight.turn

        try:
            executed_turn: ExecutedTurn = superheroes_fight.execute_turn()

            if executed_turn["victim_avoid_attack"]:
                print(
                    f"\n> Turn N°{executed_turn['number']}: {executed_turn['victim'].name}",
                    f" avoided {executed_turn['attacker'].name} attack.",
                )
                continue

            print(
                f"\n> Turn N°{executed_turn['number']}: {executed_turn['attacker'].name} attacked"
                + f" {executed_turn['victim'].name} with"
                + f" {executed_turn['damage_produced_by_attacker']} points of damage.",
                f"[ Life points of Deadpool: {deadpool.life_points} ]",
                f"[ Life points of Wolverine: {wolverine.life_points} ]",
                sep="\n",
            )
        except SuperheroRegeneratingException:
            print(
                f"\n> Turn N°{current_turn['number']}: {current_turn['attacker'].name} is"
                + " regenerating"
            )

    print(f"\nThe winner is {superheroes_fight.winner.name}!")


asyncio.run(main=main())
