import reflex as rx

from app.models.fighter_in_fight import FighterInFight
from app.models.fighter import Fighter
from app.models.action import Action
from app.models.event import Event


class Fight(rx.Base):
    left: FighterInFight | None = None
    right: FighterInFight | None = None
    winner: Fighter | None = None
    events: list[Event] = []
    simulated: bool = False
    showed: bool = False
