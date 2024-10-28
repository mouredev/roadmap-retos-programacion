import reflex as rx

from app.states.fighters_inputs import FightersInputState
from app.states.tournament import TournamentState


class FormState(FightersInputState):
    async def start_button_on_click(self) -> None:
        # fighters_input_state = await self.get_state(FightersInputState)
        fighters = self.fighters.__copy__()[: self.num_fighters]
        for fighter in fighters:
            if fighter.name == "":
                return rx.window_alert("Todos los luchadores deben tener nombre")
            if list(
                filter(
                    lambda x: x < 1 or x > 100,
                    [fighter.speed, fighter.attack, fighter.defense],
                )
            ):
                return rx.window_alert(
                    "Las estadísticas de los luchadores deben estar entre 1 y 100"
                )
        tournament_state = await self.get_state(TournamentState)
        await tournament_state.start_tournament(fighters=fighters)
        self.reset()
