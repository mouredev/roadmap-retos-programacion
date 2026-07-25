# pylint: disable=missing-module-docstring,missing-function-docstring

from datetime import date, datetime, timedelta
from asyncio import sleep, run
from os import system
from threading import Thread
from typing import TypedDict
import math

TimeRemaining = TypedDict(
    "TimeRemaining",
    {
        "days": int,
        "hours": int,
        "minutes": int,
        "seconds": int,
    },
)


def get_time_remaining(*, _from: date, _to: date) -> TimeRemaining:
    time_remaining: TimeRemaining = {"days": 0, "hours": 0, "minutes": 0, "seconds": 0}

    diff_dates: timedelta = _to - _from
    total_seconds: int = diff_dates.seconds

    time_remaining["days"] = diff_dates.days

    time_remaining["hours"] = math.floor(total_seconds / 3600)
    total_seconds -= time_remaining["hours"] * 3600

    time_remaining["minutes"] = math.floor(total_seconds / 60)
    total_seconds -= time_remaining["minutes"] * 60

    time_remaining["seconds"] = total_seconds

    return time_remaining


async def main() -> None:
    start_date: date = datetime.now()
    end_date: date = datetime(year=2024, month=11, day=28, hour=0, minute=59, second=0)

    remaining_time: TimeRemaining = get_time_remaining(_from=start_date, _to=end_date)

    system(command="clear")

    print(
        f"> Time remaining for {end_date}: "
        f"[ {remaining_time['days']:{0}6} days | "
        f"{remaining_time['hours']:{0}2} hours | "
        f"{remaining_time['minutes']:{0}2} minutes | "
        f"{remaining_time['seconds']:{0}2} seconds ]."
    )

    while (
        remaining_time["days"]
        or remaining_time["hours"]
        or remaining_time["minutes"]
        or remaining_time["seconds"]
    ):
        start_date: date = datetime.now()

        await sleep(delay=1)
        remaining_time = get_time_remaining(_from=start_date, _to=end_date)

        system(command="clear")

        print(
            f"> Time remaining for {end_date}: "
            f"[ {remaining_time['days']:{0}6} days | "
            f"{remaining_time['hours']:{0}2} hours | "
            f"{remaining_time['minutes']:{0}2} minutes | "
            f"{remaining_time['seconds']:{0}2} seconds ]."
        )

    print("\n> The day has come!")


Thread(
    target=run,
    kwargs={
        "main": main(),
    },
).start()
