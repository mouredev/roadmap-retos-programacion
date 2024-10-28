import reflex as rx

from app.components.nationalities_modal import nationalities_modal
from app.components.fighters_inputs import (
    num_fighters_select,
    random_data_button,
    fighters_data_editor,
)

from app.states.form import FormState


def form() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text("Número de luchadores", white_space="nowrap"),
            num_fighters_select(),
            spacing="2",
            align="center",
            justify="center",
            width="100%",
        ),
        fighters_data_editor(),
        rx.hstack(
            rx.hstack(
                random_data_button(),
                nationalities_modal(),
            ),
            rx.button(
                "Iniciar torneo",
                on_click=FormState.start_button_on_click,
            ),
            spacing="2",
            align="center",
            justify="between",
            width="100%",
        ),
        spacing="4",
        id="form",
    )
