import reflex as rx


from app.components.phase import phase
from app.components.question_modal import question_modal
from app.components.delay_modal import delay_modal

from app.states.tournament import TournamentState
from app.states.phase import PhaseState
from app.states.fight import FightState


def tournament() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(
                rx.tooltip(
                    # El tooltip no funciona como trigger
                    rx.box(
                        question_modal(
                            trigger=rx.button(
                                rx.icon("trash-2"),
                                color_scheme="tomato",
                            ),
                            title="Reiniciar torneo",
                            description="¿Estás seguro de que quieres reiniciar el torneo?",
                            on_click=TournamentState.reset_button_on_click,
                        ),
                    ),
                    content="Reiniciar torneo",
                ),
                rx.button(
                    "Sortear",
                    on_click=PhaseState.draw,
                    disabled=~PhaseState.is_drawable,
                ),
                rx.tooltip(
                    rx.button(
                        rx.icon("swords"),
                        on_click=FightState.simulate_all,
                        disabled=~PhaseState.is_ready_to_simulate,
                    ),
                    content="Simular todos los combates",
                ),
                delay_modal(),
                align="center",
                justify="start",
                width="100%",
            ),
            rx.hstack(
                rx.heading(
                    PhaseState.phase.name,
                    size="6",
                ),
                justify="center",
                width="100%",
            ),
            rx.hstack(
                rx.tooltip(
                    rx.button(
                        rx.icon("arrow-left"),
                        disabled=TournamentState.is_first_phase,
                        on_click=TournamentState.previous_button_on_click,
                    ),
                    content="Anterior fase",
                ),
                rx.tooltip(
                    rx.button(
                        rx.icon("arrow-right"),
                        disabled=TournamentState.is_last_phase,
                        on_click=TournamentState.next_button_on_click,
                    ),
                    content="Siguiente fase",
                ),
                align="center",
                justify="end",
                width="100%",
            ),
            spacing="2",
            width="100%",
        ),
        phase(),
        rx.cond(
            TournamentState.is_last_phase & TournamentState.winner,
            rx.vstack(
                rx.icon(
                    "medal",
                    size=256,
                    stroke_width=1,
                ),
                rx.heading(
                    TournamentState.winner.name,
                ),
                spacing="2",
                align="center",
                width="100%",
            ),
        ),
        width="100%",
        spacing="4",
        id="form",
        on_mount=TournamentState.on_mount,
    )
