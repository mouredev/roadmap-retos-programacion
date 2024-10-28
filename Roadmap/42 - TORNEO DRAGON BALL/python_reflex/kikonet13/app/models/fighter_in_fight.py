import reflex as rx
from enum import Enum
from random import choice, randint

from app.models.fighter import Fighter
from app.models.action import Action


MIN = 1
MAX = 100
MIN_MODIFIER = 0.8
MAX_MODIFIER = 1.2


class Condition(Enum):
    BEST = 1.2
    GOOD = 1.1
    NORMAL = 1.0
    BAD = 0.9
    WORST = 0.8


class FighterInFight(rx.Base):
    fighter: Fighter
    condition: Condition
    health: int = 100

    _min_attack: int
    _max_attack: int
    _min_defense: int
    _max_defense: int
    _min_speed: int
    _max_speed: int

    def __init__(self, fighter: Fighter):
        super().__init__(
            fighter=fighter,
            condition=choice(
                list(Condition),
            ),
        )
        self._min_attack: int = int(
            max(self.fighter.attack * self.condition * MIN_MODIFIER, MIN)
        )
        self._max_attack: int = int(
            min(self.fighter.attack * self.condition * MAX_MODIFIER, MAX)
        )
        self._min_defense: int = int(
            max(self.fighter.defense * self.condition * MIN_MODIFIER, MIN)
        )
        self._max_defense: int = int(
            min(self.fighter.defense * self.condition * MAX_MODIFIER, MAX)
        )
        self._min_speed: int = int(
            max(self.fighter.speed * self.condition * MIN_MODIFIER, MIN)
        )
        self._max_speed: int = int(
            min(self.fighter.speed * self.condition * MAX_MODIFIER, MAX)
        )

    def _get_attack(self) -> int:
        return randint(self._min_attack, self._max_attack)

    def _get_defense(self) -> int:
        return randint(self._min_defense, self._max_defense)

    def _get_speed(self) -> int:
        return randint(self._min_speed, self._max_speed)

    def next_attack(self) -> Action:
        return Action.attack(self._get_speed(), self._get_attack())

    def next_defense(self) -> Action:
        return Action.defense(self._get_defense())
