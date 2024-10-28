import reflex as rx


def question_modal(
    trigger: rx.Component,
    title: str,
    description: str,
    on_click: rx.EventHandler,
) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            trigger,
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(
                title,
            ),
            rx.alert_dialog.description(
                description,
                size="2",
            ),
            rx.hstack(
                rx.alert_dialog.cancel(
                    rx.button(
                        "No",
                        variant="soft",
                    ),
                ),
                rx.alert_dialog.action(
                    rx.button(
                        "Sí",
                        on_click=on_click,
                    ),
                ),
                align="center",
                justify="end",
            ),
        ),
    )
