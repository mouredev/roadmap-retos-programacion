import reflex as rx

from app.states.nationalities_modal import NationalitiesModalState


def nationality_checkbox(nat: dict, pos: int) -> rx.Component:
    return rx.hstack(
        rx.checkbox(
            checked=nat["active"].bool(),
            on_change=NationalitiesModalState.check_box_on_change(pos),
        ),
        rx.tooltip(
            rx.image(
                src=nat["image_url"],
                alt=nat["tag"].to_string(),
                width="2em",
            ),
            content=nat["tag"].to_string(),
        ),
        height="2em",
        align="center",
    )


def popover_content() -> rx.Component:
    return rx.grid(
        rx.foreach(
            NationalitiesModalState.nationalities,
            lambda nat, pos: nationality_checkbox(nat, pos),
        ),
        columns="3",
        spacing="4",
        width="15em",
    )


def nationalities_modal() -> rx.Component:
    return rx.tooltip(
        # No funciona el tooltip con el popover
        rx.box(
            rx.popover.root(
                rx.popover.trigger(
                    rx.button(
                        rx.icon(
                            tag="globe",
                        ),
                        variant="outline",
                    ),
                ),
                rx.popover.content(
                    popover_content(),
                ),
            ),
        ),
        content="Nacionalidades",
    )
