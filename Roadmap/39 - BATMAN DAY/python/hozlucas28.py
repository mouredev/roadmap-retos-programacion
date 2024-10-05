# pylint: disable=missing-module-docstring,missing-function-docstring

from datetime import datetime
from typing import Literal, Tuple, TypedDict, List


# ---------------------------------------------------------------------------- #
#                                FIRST CHALLENGE                               #
# ---------------------------------------------------------------------------- #


def get_batman_day_anniversary(*, anniversary: int) -> datetime:
    anniversary_date: datetime = datetime(year=1939, month=9, day=16)

    if anniversary > 0:
        anniversary_date = datetime(
            year=anniversary_date.year + anniversary,
            month=anniversary_date.month,
            day=1,
        )

        i: int = 1
        saturday_counter: int = 1 if anniversary_date.weekday() == 5 else 0

        while saturday_counter < 3:
            anniversary_date = datetime(
                year=anniversary_date.year, month=anniversary_date.month, day=i
            )

            if anniversary_date.weekday() == 5:
                saturday_counter += 1

            i += 1

    return anniversary_date


batman_day_85th_anniversary: datetime = get_batman_day_anniversary(anniversary=85)
batman_day_100th_anniversary: datetime = get_batman_day_anniversary(anniversary=100)

print("> First challenge...")

print(
    f"\n> The 85th anniversary of Batman day is on "
    f"{batman_day_85th_anniversary.month}/"
    f"{batman_day_85th_anniversary.day}/"
    f"{batman_day_85th_anniversary.year}."
)

print(
    f"\n> The 100th anniversary of Batman day is on "
    f"{batman_day_100th_anniversary.month}/"
    f"{batman_day_100th_anniversary.day}/"
    f"{batman_day_100th_anniversary.year}."
)


# ---------------------------------------------------------------------------- #
#                               SECOND CHALLENGE                               #
# ---------------------------------------------------------------------------- #


# ----------------------------------- Types ---------------------------------- #


type ThreatLevel = Literal[
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
]

type RowSensors = Tuple[
    ThreatLevel,
    ThreatLevel,
    ThreatLevel,
    ThreatLevel,
    ThreatLevel,
    ThreatLevel,
    ThreatLevel,
    ThreatLevel,
    ThreatLevel,
    ThreatLevel,
    ThreatLevel,
    ThreatLevel,
    ThreatLevel,
    ThreatLevel,
    ThreatLevel,
    ThreatLevel,
    ThreatLevel,
    ThreatLevel,
    ThreatLevel,
    ThreatLevel,
]

type Sensors = Tuple[
    RowSensors,
    RowSensors,
    RowSensors,
    RowSensors,
    RowSensors,
    RowSensors,
    RowSensors,
    RowSensors,
    RowSensors,
    RowSensors,
    RowSensors,
    RowSensors,
    RowSensors,
    RowSensors,
    RowSensors,
    RowSensors,
    RowSensors,
    RowSensors,
    RowSensors,
    RowSensors,
]

ThreatLevelPos = TypedDict("ThreatLevelPos", {"x": int, "y": int, "threat_level": int})


# ----------------------------------- Main ----------------------------------- #


def get_threat_levels(*, _sensors: Sensors) -> List[ThreatLevelPos]:
    _threat_levels: List[ThreatLevelPos] = []

    for i in range(1, len(_sensors) - 1):
        for j in range(1, len(_sensors[i]) - 1):
            _threat_level: int = 0

            _threat_level += _sensors[i - 1][j - 1]
            _threat_level += _sensors[i - 1][j]
            _threat_level += _sensors[i - 1][j + 1]

            _threat_level += _sensors[i][j - 1]
            _threat_level += _sensors[i][j]
            _threat_level += _sensors[i][j + 1]

            _threat_level += _sensors[i + 1][j - 1]
            _threat_level += _sensors[i + 1][j]
            _threat_level += _sensors[i + 1][j + 1]

            _threat_levels.append({"x": j, "threat_level": _threat_level, "y": i})

    return _threat_levels


batman_cave_pos: Tuple[int, int] = (0, 0)

sensors: Sensors = (
    (1, 0, 1, 1, 2, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1),
    (2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0),
    (1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1),
    (0, 9, 8, 0, 2, 0, 9, 2, 8, 1, 0, 1, 3, 7, 8, 1, 0, 2, 7, 6),
    (1, 0, 1, 1, 2, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1),
    (3, 1, 8, 7, 9, 6, 1, 7, 9, 0, 1, 0, 1, 9, 2, 1, 3, 0, 8, 0),
    (1, 6, 9, 1, 2, 8, 0, 2, 1, 3, 2, 8, 7, 2, 8, 0, 1, 7, 9, 0),
    (1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 1, 0),
    (0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0),
    (2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2),
    (7, 8, 6, 1, 0, 9, 2, 8, 1, 3, 7, 1, 0, 2, 0, 9, 1, 6, 7, 8),
    (0, 1, 7, 9, 2, 8, 1, 6, 7, 8, 1, 2, 0, 3, 1, 8, 2, 7, 0, 1),
    (3, 0, 9, 1, 8, 6, 1, 0, 7, 9, 2, 0, 1, 2, 8, 0, 1, 9, 6, 1),
    (1, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0),
    (0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0),
    (2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2),
    (9, 6, 1, 0, 9, 8, 7, 2, 8, 0, 1, 0, 3, 6, 2, 7, 9, 2, 8, 1),
    (0, 7, 8, 9, 6, 2, 1, 9, 6, 7, 8, 0, 9, 7, 6, 8, 1, 0, 2, 8),
    (2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2),
    (3, 2, 1, 9, 6, 7, 0, 3, 1, 8, 2, 7, 9, 2, 0, 9, 7, 6, 8, 0),
)

threat_levels: List[ThreatLevelPos] = get_threat_levels(_sensors=sensors)

threat_levels_greater_than_twenty = list(
    filter(lambda threat_level: threat_level["threat_level"] >= 20, threat_levels)
)

print("\n> Second challenge...")

print("\n> Threat levels greater than 20 (security protocol activated)...")

for threat_level in threat_levels_greater_than_twenty:
    print(f"\n> Coordinates (x, y): ({threat_level['x']}, {threat_level['y']}).")
    print(f"> Threat level: {threat_level['threat_level']}.")

print("\n> Position with the maximum threat level...")

max_threat_level: ThreatLevelPos = max(
    iter(threat_levels_greater_than_twenty),
    key=lambda threat_level: threat_level["threat_level"],
)

distance_to_batman_cave: int = abs(max_threat_level["x"] - batman_cave_pos[0]) + abs(
    max_threat_level["y"] - batman_cave_pos[1]
)

print(f"\n> Coordinates (x, y): ({max_threat_level['x']}, {max_threat_level['y']}).")
print(f"> Threat level: {max_threat_level['threat_level']}.")
print(f"> Distance to batman cave: {distance_to_batman_cave} cells.")
