import reflex as rx
import requests

from app.models.variation import Variation
from app.models.fighter import Fighter

from app.states.nationalities_modal import NationalitiesModalState

MAX_FIGHTERS_EXPONENT = 10
MAX_FIGHTERS = 2**MAX_FIGHTERS_EXPONENT


class FightersInputState(NationalitiesModalState):
    num_fighters: int = 8
    columns: list[dict[str, str]] = [
        {
            "title": "Nombre",
            "type": "str",
            "width": 200,
        },
        {
            "title": "Vel.",
            "type": "int",
            "width": 40,
        },
        {
            "title": "At.",
            "type": "int",
            "width": 40,
        },
        {
            "title": "Def.",
            "type": "int",
            "width": 40,
        },
        {
            "title": "🗠",
            "type": "int",
            "width": 40,
        },
    ]
    fighters: list[Fighter] = [Fighter() for _ in range(MAX_FIGHTERS)]

    @rx.var
    def data(self) -> list[list[str | int]]:
        return [
            [
                fighter.name,
                fighter.speed,
                fighter.attack,
                fighter.defense,
                fighter.average,
            ]
            for fighter in self.fighters[: self.num_fighters]
        ]

    def on_mount(self) -> None:
        # self.reset()
        pass

    def select_on_change(self, value: str) -> None:
        self.num_fighters = int(value)

    def random_data(self) -> None:
        self.fighters = []
        speed_variation = Variation()
        attack_variation = Variation()
        defense_variation = Variation()

        # nationalities_modal_state = await self.get_state(NationalitiesModalState)

        countries = ",".join([nat.tag for nat in self.nationalities if nat.active])

        response = requests.get(
            f"https://randomuser.me/api/?results={MAX_FIGHTERS}&inc=name&nat={countries}"
        )
        results = response.json()["results"]
        for result in results:
            self.fighters.append(
                Fighter(
                    name=result["name"]["first"] + " " + result["name"]["last"],
                    speed=speed_variation.get_random_number(),
                    attack=attack_variation.get_random_number(),
                    defense=defense_variation.get_random_number(),
                )
            )

    def data_editor_on_cell_edited(
        self, pos: tuple[int, int], value_dict: dict[str, str | int]
    ) -> None:
        column, row = pos
        if column == 4:
            return
        value = value_dict["data"]
        self.fighters[row].set_column(column, value)
