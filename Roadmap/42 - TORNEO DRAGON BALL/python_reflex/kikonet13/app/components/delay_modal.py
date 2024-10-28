import reflex as rx

from app.states.phase import PhaseState

IN_MIN = 1
IN_MAX = 100
OUT_MIN = 0.5
OUT_MAX = 3


def delay_modal() -> rx.Component:
    return rx.tooltip(
        # No funciona el tooltip con el popover
        rx.box(
            rx.popover.root(
                rx.popover.trigger(
                    rx.button(
                        rx.icon(
                            tag="clock",
                        ),
                        variant="outline",
                    ),
                ),
                rx.popover.content(
                    rx.vstack(
                        rx.hstack(
                            rx.icon(
                                "snail",
                                stroke_width=OUT_MAX
                                + ((PhaseState.speed - IN_MIN) / (IN_MAX - IN_MIN))
                                * (OUT_MIN - OUT_MAX),
                            ),
                            rx.icon(
                                "rabbit",
                                stroke_width=OUT_MIN
                                + ((PhaseState.speed - IN_MIN) / (IN_MAX - IN_MIN))
                                * (OUT_MAX - OUT_MIN),
                            ),
                            justify="between",
                            width="100%",
                        ),
                        rx.slider(
                            default_value=PhaseState.speed,
                            min=1,
                            max=100,
                            on_change=PhaseState.set_delay.throttle(100),
                            on_value_commit=PhaseState.set_delay,
                        ),
                        width="10em",
                    ),
                ),
            ),
        ),
        content="Velocidad de simulación",
    )
