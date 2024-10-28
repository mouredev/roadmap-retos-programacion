import reflex as rx

from app.models.fight import Fight
from app.models.fighter import Fighter


class Phase(rx.Base):
    fighters: list[Fighter] = []
    fights: list[Fight]
    name: str = ""
    number: int
    num_fighters: int
    drawn: bool = False

    def __init__(self, number: int) -> None:
        super().__init__(
            number=number,
            num_fighters=2**number,
            fights=[Fight() for _ in range(2 ** (number - 1))],
        )
        self.name = self._set_name()

    def _set_name(self) -> str:
        if self.number == 1:
            return "Final"
        elif self.number == 2:
            return "Semifinales"
        else:
            return f"1/{2**(self.number-1)} de final"
