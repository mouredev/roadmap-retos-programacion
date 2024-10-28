import reflex as rx

from app.views.form import form
from app.views.tournament import tournament

from app.state import State, View
from app.states.tournament import TournamentState

# He sobreescrito el método rx.Base.dict() para que incluya las @property
# Hay un error con los estados anidados que se soluciona con esto: https://github.com/reflex-dev/reflex/commit/4cec2d152c6d8f5fbdf26a0fd10cd1220b96d7c9


class IndexState(rx.State):
    async def reset_all(self) -> None:
        substates = self.get_parent_state().get_substates()
        for substate in substates:
            state = await self.get_state(substate)
            state.reset()
        state = await self.get_state(State)
        state.on_mount()

    async def on_load(self) -> None:
        # self.reset_all()
        pass


@rx.page(
    route="/",
    on_load=IndexState.on_load,
    title="Torneo Dragon Ball",
)
def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            # rx.icon_button("refresh-ccw", on_click=IndexState.reset_all),
            rx.vstack(
                rx.link(
                    rx.code(
                        "Retos de programación by mouredev",
                        size="4",
                        variant="outline",
                    ),
                    href="https://retosdeprogramacion.com/",
                    is_external=True,
                ),
                rx.hstack(
                    rx.heading(
                        rx.code("42", size="8"),
                        " Torneo Dragon Ball",
                        size="8",
                        trim="both",
                    ),
                    # rx.link(
                    #     rx.image(
                    #         src="/github.svg",
                    #         width="2.5em",
                    #         height="2.5em",
                    #     ),
                    #     href="https://github.com/KikoNet13/reto_42_torneo_dragon_ball",
                    #     is_external=True,
                    # ),
                    rx.link(
                        rx.button(
                            rx.icon(
                                "github",
                                size=28,
                            ),
                            variant="soft",
                            size="3",
                        ),
                        href="https://github.com/KikoNet13/reto_42_torneo_dragon_ball",
                        is_external=True,
                    ),
                    align="center",
                    justify="center",
                ),
                align="center",
                justify="center",
                margin_y="2em",
            ),
            rx.match(
                State.current_view,
                (
                    View.LOADING,
                    rx.skeleton(
                        rx.box(
                            width="100%",
                            height="100%",
                            align="center",
                            justify="center",
                        ),
                        loading=True,
                    ),
                ),
                (
                    View.FORM,
                    form(),
                ),
                (
                    View.TOURNAMENT,
                    rx.skeleton(
                        tournament(),
                        loading=~TournamentState.tournament,
                    ),
                ),
            ),
            width="100%",
            height="100%",
            align="center",
        ),
        width="100%",
        min_height="100vh",
        align="center",
        justify="center",
        on_mount=State.on_mount,
    )


app = rx.App(
    style={
        ".rt-ScrollAreaViewport > *": {
            "min-width": "100% !important",
        },
        "background": "radial-gradient(circle, #222222, #000000)",
    },
    theme=rx.theme(
        appearance="dark",
        panel_background="solid",
    ),
)
