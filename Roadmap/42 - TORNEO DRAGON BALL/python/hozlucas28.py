# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,broad-exception-raised,too-many-arguments

from abc import ABCMeta, abstractmethod
from typing import TypedDict
from random import choice, random


# ---------------------------------------------------------------------------- #
#                                    CLASSES                                   #
# ---------------------------------------------------------------------------- #


# ---------------------------------- Fighter --------------------------------- #


class AbcFighter(metaclass=ABCMeta):
    @property
    @abstractmethod
    def life(self) -> float:
        pass

    @property
    @abstractmethod
    def attack(self) -> float:
        pass

    @property
    @abstractmethod
    def defense(self) -> float:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def speed(self) -> float:
        pass

    @life.setter
    def life(self, new_life: float) -> None:
        pass

    @abstractmethod
    def copy(self) -> "AbcFighter":
        pass


class Fighter(AbcFighter):
    __life: float
    __attack: float
    __defense: float
    __name: str
    __speed: float

    def __init__(
        self,
        *,
        life: float = 100,
        attack: float,
        defense: float,
        name: str,
        speed: float,
    ) -> None:
        self.__life = life
        self.__attack = attack
        self.__defense = defense
        self.__name = name
        self.__speed = speed

    @property
    def life(self) -> float:
        return self.__life

    @property
    def attack(self) -> float:
        return self.__attack

    @property
    def defense(self) -> float:
        return self.__defense

    @property
    def name(self) -> str:
        return self.__name

    @property
    def speed(self) -> float:
        return self.__speed

    @life.setter
    def life(self, new_life: float) -> None:
        self.__life = max(new_life, 0)

    def copy(self) -> AbcFighter:
        return Fighter(
            life=self.__life,
            attack=self.__attack,
            defense=self.__defense,
            name=self.__name,
            speed=self.__speed,
        )


# -------------------------------- Tournament -------------------------------- #


ShiftInformation = TypedDict(
    "ShiftInformation",
    {
        "attack_damage": float,
        "attacker": AbcFighter,
        "shift": float,
        "victim": AbcFighter,
    },
)

Round = TypedDict(
    "Round",
    {
        "info_per_shifts": list[ShiftInformation],
        "looser": AbcFighter,
        "shifts": float,
        "winner": AbcFighter,
    },
)


class AbcTournament(metaclass=ABCMeta):
    @property
    @abstractmethod
    def phase(self) -> int:
        pass

    @property
    @abstractmethod
    def team_a(self) -> list[AbcFighter]:
        pass

    @property
    @abstractmethod
    def team_b(self) -> list[AbcFighter]:
        pass

    @property
    @abstractmethod
    def winner(self) -> AbcFighter | None:
        pass

    @abstractmethod
    def execute_next_round(self) -> Round:
        pass


class Tournament(AbcTournament):
    __pair_of_fighters: list[AbcFighter]
    __phase: int
    __round: int
    __team_a: list[AbcFighter]
    __team_b: list[AbcFighter]
    __winner: AbcFighter | None

    def __init__(self, *, _team_a: list[AbcFighter], _team_b: list[AbcFighter]) -> None:
        if len(_team_a) != len(_team_b):
            raise Exception("The number of fighters in both teams must be equal")

        if len(_team_a) % 2 or len(_team_b) % 2:
            raise Exception("The number of fighters in both teams must be even")

        self.__pair_of_fighters = []
        self.__phase = 0
        self.__round = 0
        self.__team_a = _team_a
        self.__team_b = _team_b
        self.__winner = None

        self.__set_rnd_pair_of_fighters()

    @property
    def phase(self) -> int:
        return self.__phase

    @property
    def team_a(self) -> list[AbcFighter]:
        return self.__team_a

    @property
    def team_b(self) -> list[AbcFighter]:
        return self.__team_b

    @property
    def winner(self) -> AbcFighter | None:
        return self.__winner

    def __set_rnd_pair_of_fighters(self) -> None:

        team_a_cpy: list[AbcFighter] = self.__team_a.copy()
        team_b_cpy: list[AbcFighter] = self.__team_b.copy()

        for _ in range(len(self.__team_a)):
            rnd_fighter_a: AbcFighter = choice(seq=team_a_cpy)
            rnd_fighter_b: AbcFighter = choice(seq=team_b_cpy)

            team_a_cpy.remove(rnd_fighter_a)
            team_b_cpy.remove(rnd_fighter_b)

            self.__pair_of_fighters.append(rnd_fighter_a)
            self.__pair_of_fighters.append(rnd_fighter_b)

    def execute_next_round(self) -> Round:
        if self.__winner is not None:
            raise Exception("The tournament already has a winner")
        if len(self.__pair_of_fighters) < 2:
            raise Exception("Not enough fighters to execute the next round")

        self.__round += 1
        offset: int = self.__round - 1

        fighter_01: AbcFighter = self.__pair_of_fighters[offset]
        fighter_02: AbcFighter = self.__pair_of_fighters[offset + 1]

        if fighter_01.speed < fighter_02.speed:
            fighter_01, fighter_02 = fighter_02, fighter_01

        shifts = 0
        info_per_shifts: list[ShiftInformation] = []

        while fighter_01.life and fighter_02.life:
            attack_damage = 0

            if random() > 0.2:
                attack: float = fighter_01.attack
                defense: float = fighter_02.defense

                attack_damage: float = abs(attack - defense)
                if defense > attack:
                    attack_damage = attack_damage * 0.1

                fighter_02.life = fighter_02.life - attack_damage

            shifts += 1

            info_per_shifts.append(
                {
                    "attack_damage": attack_damage,
                    "attacker": fighter_01.copy(),
                    "victim": fighter_02.copy(),
                    "shift": shifts,
                }
            )

            fighter_01, fighter_02 = fighter_02, fighter_01

        fighter_01 = self.__pair_of_fighters[offset]
        fighter_02 = self.__pair_of_fighters[offset + 1]

        looser_index: int = (offset + 1) if fighter_01.life else offset
        looser: AbcFighter = self.__pair_of_fighters.pop(looser_index)

        if len(self.__pair_of_fighters) < 2:
            self.__winner = self.__pair_of_fighters[0]

        if self.__round == len(self.__pair_of_fighters):
            self.__round = 0
            self.__phase += 1

        return {
            "winner": fighter_01.copy() if fighter_01.life else fighter_02.copy(),
            "looser": looser,
            "shifts": shifts,
            "info_per_shifts": info_per_shifts,
        }


# ---------------------------------------------------------------------------- #
#                                     MAIN                                     #
# ---------------------------------------------------------------------------- #


team_a: list[AbcFighter] = [
    Fighter(attack=90, defense=80, name="Goku", speed=95),
    Fighter(attack=85, defense=75, name="Vegeta", speed=90),
    Fighter(attack=70, defense=65, name="Piccolo", speed=80),
    Fighter(attack=60, defense=55, name="Krillin", speed=70),
]

team_b: list[AbcFighter] = [
    Fighter(attack=88, defense=78, name="Frieza", speed=92),
    Fighter(attack=82, defense=72, name="Cell", speed=88),
    Fighter(attack=75, defense=65, name="Majin Buu", speed=85),
    Fighter(attack=65, defense=60, name="Broly", speed=75),
]

tournament: AbcTournament = Tournament(_team_a=team_a, _team_b=team_b)

rounds: int = 0

while tournament.winner is None:
    _round: Round = tournament.execute_next_round()

    rounds += 1

    print(
        f"> Round {rounds} "
        f"({_round['winner'].name} vs "
        f"{_round['looser'].name})...\n"
    )

    for shift in _round["info_per_shifts"]:
        if shift["attack_damage"] > 0:
            print(
                f"> Shift {shift['shift']}: "
                f"{shift['attacker'].name} attacks "
                f"{shift['victim'].name} with an attack damage of ",
                shift["attack_damage"],
            )
        else:
            print(
                f"> Shift {shift['shift']}: "
                f"{shift['attacker'].name} attacks "
                f"{shift['victim'].name}, but {shift['victim'].name} "
                "evades the attack."
            )

    print(
        f"\n> {_round['winner'].name} wins the fight against "
        f"{_round['looser'].name} in {_round['shifts']} shifts!\n"
    )


print(f"> The winner of the tournament is {tournament.winner.name}!")
