import reflex as rx

from app.models.fighter_in_fight import Condition, FighterInFight

# INFO_CONDITIONS = {
#     str(Condition.BEST.value): {
#         "icon_tag": "move-up",
#         "color": "cyan",
#     },
#     str(Condition.GOOD.value): {
#         "icon_tag": "move-up-right",
#         "color": "grass",
#     },
#     str(Condition.NORMAL.value): {
#         "icon_tag": "move-right",
#         "color": "amber",
#     },
#     str(Condition.BAD.value): {
#         "icon_tag": "move-down-right",
#         "color": "orange",
#     },
#     str(Condition.WORST.value): {
#         "icon_tag": "move-down",
#         "color": "tomato",
#     },
# }


def fighter_condition_detail(icon_tag: str, color: str) -> rx.Component:
    return rx.tooltip(
        rx.icon(
            icon_tag,
            color=rx.color(color, 8),
            # size=48,
            stroke_width=4,
        ),
        content="Condición",
    )


def fighter_condition(condition: Condition) -> rx.Component:
    return rx.match(
        condition,
        (
            Condition.BEST,
            fighter_condition_detail("move-up", "cyan"),
        ),
        (
            Condition.GOOD,
            fighter_condition_detail("move-up-right", "grass"),
        ),
        (
            Condition.NORMAL,
            fighter_condition_detail("move-right", "amber"),
        ),
        (
            Condition.BAD,
            fighter_condition_detail("move-down-right", "orange"),
        ),
        (
            Condition.WORST,
            fighter_condition_detail("move-down", "tomato"),
        ),
    )


def fighter_health(health: int, is_left: bool = True) -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.hstack(
                rx.cond(
                    is_left,
                    rx.fragment(
                        rx.text(health),
                        rx.icon("heart"),
                    ),
                    rx.fragment(
                        rx.icon("heart"),
                        rx.text(health),
                    ),
                ),
            ),
            rx.progress(
                value=health,
                max=100,
                color_scheme="orange",
                width="6em",
            ),
            justify="center",
            align="center",
        ),
        width="100%",
        justify=rx.cond(is_left, "end", "start"),
        align="center",
    )
