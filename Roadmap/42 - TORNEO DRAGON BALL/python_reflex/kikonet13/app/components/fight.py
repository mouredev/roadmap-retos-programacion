import reflex as rx

from app.models.fight import Fight

from app.components.fighter import (
    fighter_left,
    fighter_right,
    fighter_tbd_card,
)
from app.components.fighter_in_fight import fighter_health, fighter_condition
from app.components.event import event

from app.states.fight import FightState


def fight_component(fight: Fight, index: int) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.hstack(
                    rx.cond(
                        fight.left,
                        fighter_left(
                            fight.left.fighter,
                            # Se compara el contenido porque no hay id
                            fight.left.fighter.to_string() == fight.winner.to_string(),
                        ),
                        fighter_tbd_card(),
                    ),
                    width="100%",
                    justify="end",
                ),
                rx.center(
                    rx.cond(
                        fight.left,
                        fighter_condition(fight.left.condition),
                    ),
                    width="4em",
                ),
                rx.center(
                    rx.cond(
                        fight.simulated,
                        rx.tooltip(
                            rx.button(
                                rx.cond(
                                    fight.showed,
                                    rx.icon("eye-off"),
                                    rx.icon("eye"),
                                ),
                                variant="ghost",
                                size="2",
                                on_click=FightState.toggle_show(index),
                            ),
                            content=rx.cond(
                                fight.showed,
                                "Ocultar eventos",
                                "Mostrar eventos",
                            ),
                        ),
                        rx.tooltip(
                            rx.button(
                                rx.icon("swords"),
                                variant="ghost",
                                size="2",
                                on_click=FightState.simulate_fight(index),
                                disabled=~fight.left | ~fight.right,
                            ),
                            content="Simular combate",
                        ),
                    ),
                    width="10em",
                    height="4em",
                ),
                rx.center(
                    rx.cond(
                        fight.right,
                        fighter_condition(fight.right.condition),
                    ),
                    width="4em",
                ),
                rx.hstack(
                    rx.cond(
                        fight.right,
                        fighter_right(
                            fight.right.fighter,
                            # Se compara el contenido porque no hay id
                            fight.right.fighter.to_string() == fight.winner.to_string(),
                        ),
                        fighter_tbd_card(),
                    ),
                    width="100%",
                    justify="start",
                ),
                width="100%",
                justify="center",
                align="center",
                spacing="2",
            ),
            rx.cond(
                fight.simulated & fight.showed,
                rx.fragment(
                    rx.divider(),
                    rx.hstack(
                        fighter_health(fight.left.health, is_left=True),
                        rx.center(rx.icon("clock"), width="10em"),
                        fighter_health(fight.right.health, is_left=False),
                        align="center",
                        justify="center",
                        width="100%",
                    ),
                    rx.scroll_area(
                        rx.vstack(
                            rx.foreach(fight.events.reverse(), event),
                            width="100%",
                        ),
                        max_height="20em",
                    ),
                ),
            ),
        ),
        width="100%",
    )
