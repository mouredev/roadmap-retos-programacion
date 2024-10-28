import reflex as rx

from app.models.action import Action, ActionType

from app.utils.info_badges import INFO_BADGES


def left_action_badge(action_type: str, value: int = 0) -> rx.Component:
    return rx.badge(
        rx.cond(value, value, "-"),
        rx.icon(INFO_BADGES[action_type]["icon_tag"], size=16),
        color_scheme=INFO_BADGES[action_type]["color_scheme"],
        variant="outline",
        size="3",
        min_width="5em",
        justify_content="end",
        title=INFO_BADGES[action_type]["content"],
    )


def right_action_badge(action_type: str, value: int = 0) -> rx.Component:
    return rx.badge(
        rx.icon(INFO_BADGES[action_type]["icon_tag"], size=16),
        rx.cond(value, value, "-"),
        color_scheme=INFO_BADGES[action_type]["color_scheme"],
        variant="outline",
        size="3",
        min_width="5em",
        justify_content="start",
        title=INFO_BADGES[action_type]["content"],
    )


def left_action(action: Action) -> rx.Component:
    return rx.hstack(
        rx.match(
            action.action_type,
            (
                ActionType.DODGE.value,
                left_action_badge("dodge"),
            ),
            (
                ActionType.ATTACK.value,
                rx.fragment(
                    left_action_badge("speed", action.speed),
                    left_action_badge("attack", action.value),
                ),
            ),
            (
                ActionType.DEFENSE.value,
                rx.fragment(
                    left_action_badge("damage", action.damage),
                    left_action_badge("defense", action.value),
                ),
            ),
        ),
        spacing="2",
        width="100%",
        justify="end",
    )


def right_action(action: Action) -> rx.Component:
    return rx.hstack(
        rx.match(
            action.action_type,
            (
                ActionType.DODGE.value,
                right_action_badge("dodge"),
            ),
            (
                ActionType.ATTACK.value,
                rx.fragment(
                    right_action_badge("attack", action.value),
                    right_action_badge("speed", action.speed),
                ),
            ),
            (
                ActionType.DEFENSE.value,
                rx.fragment(
                    right_action_badge("defense", action.value),
                    right_action_badge("damage", action.damage),
                ),
            ),
        ),
        spacing="2",
        width="100%",
        justify="start",
    )
