import reflex as rx

from enum import Enum
from random import random

DODGE_CHANCE = 0.2


class ActionType(Enum):
    ATTACK = "attack"
    DEFENSE = "defense"
    DODGE = "dodge"
    NONE = "none"


class Action(rx.Base):
    pace: float = 0
    speed: int = 0
    action_type: ActionType = ActionType.NONE
    value: int = 0
    damage: int = 0

    @classmethod
    def attack(cls, speed: int, attack: int):
        pace = float(f"{100 / speed:.2f}")
        return cls(
            pace=pace,
            speed=speed,
            action_type=ActionType.ATTACK,
            value=attack,
        )

    @classmethod
    def defense(cls, defense: int):
        if random() < DODGE_CHANCE:
            action_type = ActionType.DODGE
            value = 0
        else:
            action_type = ActionType.DEFENSE
            value = defense
        return cls(
            action_type=action_type,
            value=value,
        )
