import reflex as rx

from app.models.fighter import Fighter
from app.models.fighter_in_fight import FighterInFight

from app.utils.info_badges import INFO_BADGES


def fighter_tbd_card() -> rx.Component:
    return rx.text.strong(
        "TBD",
        size="4",
        padding="2",
    )


def fighter_name(name: str, is_bold: bool = False) -> rx.Component:
    return (
        rx.cond(
            is_bold,
            rx.text.strong(
                name,
                style={"line-height": "1"},
            ),
            rx.text(
                name,
                style={"line-height": "1"},
                color_scheme="gray",
            ),
        ),
    )


def attribute_badge(attribute: str, value: int) -> rx.Component:
    return rx.tooltip(
        rx.badge(
            value,
            color_scheme=INFO_BADGES[attribute]["color_scheme"],
        ),
        content=INFO_BADGES[attribute]["content"],
    )


def fighter_attributes(speed: int, attack: int, defense: int) -> rx.Component:
    return rx.hstack(
        attribute_badge("speed", speed),
        attribute_badge("attack", attack),
        attribute_badge("defense", defense),
        spacing="1",
    )


def fighter_left(fighter: Fighter, is_bold: bool = False) -> rx.Component:
    return rx.hstack(
        rx.vstack(
            fighter_name(fighter.name, is_bold),
            fighter_attributes(fighter.speed, fighter.attack, fighter.defense),
            justify="between",
            align="end",
        ),
        rx.tooltip(
            # No funciona el tooltip con el avatar
            rx.box(
                rx.avatar(
                    fallback=fighter.average.to_string(),
                    size="4",
                ),
            ),
            content="Media",
        ),
        align="center",
        justify="start",
    )


def fighter_right(fighter: Fighter, is_bold: bool = False) -> rx.Component:
    return rx.hstack(
        rx.tooltip(
            # No funciona el tooltip con el avatar
            rx.box(
                rx.avatar(
                    fallback=fighter.average.to_string(),
                    size="4",
                ),
            ),
            content="Media",
        ),
        rx.vstack(
            fighter_name(fighter.name, is_bold),
            fighter_attributes(fighter.speed, fighter.attack, fighter.defense),
            justify="between",
            align="start",
        ),
        align="center",
        justify="start",
    )


def fighter_card(fighter: Fighter) -> rx.Component:
    return rx.card(
        fighter_left(fighter),
    )
