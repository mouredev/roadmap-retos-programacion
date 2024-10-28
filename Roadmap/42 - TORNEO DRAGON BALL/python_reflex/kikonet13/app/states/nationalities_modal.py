import reflex as rx

from app.models.nationality import Nationality, create_nationalities


class NationalitiesModalState(rx.State):
    nationalities: list[Nationality] = create_nationalities()

    def check_box_on_change(self, pos: int, value: bool) -> None:
        self.nationalities[pos].active = value
