import reflex as rx

from app.models.tournament import Tournament
from app.models.fighter import Fighter

from app.state import State, View


class TournamentState(rx.State):
    tournament: Tournament | None = None
    winner: Fighter | None = None

    current_phase_pos: int | None

    @rx.var
    def is_first_phase(self) -> bool:
        if self.tournament:
            return self.current_phase_pos == 0
        return False

    @rx.var
    def is_last_phase(self) -> bool:
        if self.tournament:
            return self.current_phase_pos == len(self.tournament.phases) - 1
        return False

    def create_default_tournament(self) -> None:
        self.tournament = Tournament(fighters=[])

    async def start_tournament(self, fighters: list[Fighter] = []) -> None:
        self.tournament = Tournament(fighters=fighters)
        self.current_phase_pos = 0
        state = await self.get_state(State)
        state.current_view = View.TOURNAMENT

    async def reset_button_on_click(self) -> None:
        self.reset()
        state = await self.get_state(State)
        state.reset()
        state.on_mount()

    def previous_button_on_click(self) -> None:
        self.current_phase_pos -= 1

    def next_button_on_click(self) -> None:
        self.current_phase_pos += 1

    def on_mount(self) -> None:
        if not self.tournament:
            self.tournament = Tournament(fighters=[])
