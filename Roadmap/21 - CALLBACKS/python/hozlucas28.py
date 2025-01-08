# pylint: disable=pointless-string-statement,missing-function-docstring,missing-module-docstring,unused-argument

from random import randrange
from threading import Thread
from time import sleep
from typing import Callable, TypeVar

"""
    Callbacks...
"""

print("Callbacks...")

T = TypeVar("T")


def map_list(*, __array: list[T], __callback: Callable[[T, int], T]) -> None:
    for __index, __value in enumerate(iterable=__array):
        __array[__index] = __callback(__value, __index)


numbers: list[int] = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(f"\nNumbers array before 'map_list' function call: {numbers!r}")

map_list(__array=numbers, __callback=lambda value, index: value + 1)
print(f"Numbers array after 'map_list' function call: {numbers!r}")

countries: list[str] = ["Argentina", "United States", "Spain", "Germany"]
print(f"\nCountries array before 'map_list' function call: {countries!r}")

map_list(__array=countries, __callback=lambda value, index: f"Are you from {value}?")
print(f"Countries array after 'map_list' function call: {countries!r}")

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

"""
    Additional challenge...
"""

print("Additional challenge...\n")


def prepare_dish(
    *,
    dish_name: str,
    on_confirm: Callable[[str], None],
    on_ready: Callable[[str], None],
    on_deliver: Callable[[str], None],
) -> None:
    on_confirm(dish_name)

    random_timeout: int = randrange(start=1, stop=10 + 1, step=1)

    sleep(random_timeout)
    on_ready(dish_name)

    on_deliver(dish_name)


Thread(
    target=prepare_dish,
    kwargs={
        "dish_name": "Spaghetti",
        "on_confirm": lambda dish_name: print(f"{dish_name} in preparation."),
        "on_ready": lambda dish_name: print(f"{dish_name} is ready to deliver."),
        "on_deliver": lambda dish_name: print(f"{dish_name} delivered."),
    },
).start()

Thread(
    target=prepare_dish,
    kwargs={
        "dish_name": "Soup",
        "on_confirm": lambda dish_name: print(f"{dish_name} in preparation."),
        "on_ready": lambda dish_name: print(f"{dish_name} is ready to deliver."),
        "on_deliver": lambda dish_name: print(f"{dish_name} delivered."),
    },
).start()
