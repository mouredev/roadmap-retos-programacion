import reflex as rx

from app.models.event import Event

from app.components.action import left_action, right_action


def event(event: Event) -> rx.Component:
    return rx.hstack(
        left_action(event.left),
        rx.center(
            rx.text(event.time_str),
            width="10em",
        ),
        right_action(event.right),
        width="100%",
        align="center",
    )
