import reflex as rx


from app.states.fighters_inputs import FightersInputState, MAX_FIGHTERS_EXPONENT


def num_fighters_select() -> rx.Component:
    num_fighters_list = [str(2**i) for i in range(1, MAX_FIGHTERS_EXPONENT + 1)]
    return (
        rx.select(
            num_fighters_list,
            name="num_fighters",
            value=FightersInputState.num_fighters.to_string(),
            on_change=FightersInputState.select_on_change,
        ),
    )


def random_data_button() -> rx.Component:
    return rx.button(
        "Datos aleatorios",
        on_click=FightersInputState.random_data,
        variant="outline",
    )


def fighters_data_editor() -> rx.Component:
    return rx.data_editor(
        columns=FightersInputState.columns,
        data=FightersInputState.data,
        on_cell_edited=FightersInputState.data_editor_on_cell_edited,
        on_mount=FightersInputState.on_mount,
    )
