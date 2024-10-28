import reflex as rx
from enum import Enum


class View(Enum):
    LOADING = "loading"
    FORM = "form"
    TOURNAMENT = "tournament"


class State(rx.State):
    current_view: View = View.LOADING

    def on_mount(self) -> None:
        self.current_view = View.FORM
