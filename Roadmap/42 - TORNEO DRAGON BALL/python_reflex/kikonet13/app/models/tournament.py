import reflex as rx
from math import log2

from app.models.phase import Phase
from app.models.fighter import Fighter


class Tournament(rx.Base):
    phases: list[Phase]

    def __init__(self, fighters: list[Fighter]) -> None:
        num_fighters = len(fighters)

        if num_fighters:
            exp = log2(num_fighters)
            if exp % 1 != 0:
                raise ValueError("El número de luchadores debe ser una potencia de 2")

            phases = [Phase(number=i) for i in range(int(exp), 0, -1)]
            phases[0].fighters = fighters
        else:
            phases = []

        super().__init__(phases=phases)
