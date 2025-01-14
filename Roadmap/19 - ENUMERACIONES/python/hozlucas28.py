# pylint: disable=missing-function-docstring,pointless-string-statement,missing-module-docstring,missing-class-docstring,broad-exception-raised,broad-exception-caught

from enum import Enum
from typing import Self

"""
    Enums...
"""

print("Enums...")

WeekDays = Enum(
    "WeekDays",
    [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ],
)

print(f"\nName of the first week day: {WeekDays.Monday.name}")
print(f"Name of the second week day: {WeekDays.Tuesday.name}")
print(f"Name of the third week day: {WeekDays.Wednesday.name}")
print(f"Name of the fourth week day: {WeekDays.Thursday.name}")
print(f"Name of the fifth week day: {WeekDays.Friday.name}")
print(f"Name of the sixth week day: {WeekDays.Saturday.name}")
print(f"Name of the seventh week day: {WeekDays.Sunday.name}")

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

"""
    Additional challenge...
"""

print("Additional challenge...")

States = Enum(
    "State",
    [
        "Earring",
        "Sent",
        "Delivered",
        "Cancelled",
    ],
)


class Order:
    __uid: int
    __state: States

    def __init__(self, *, uid: int, state: States) -> None:
        self.__uid = uid
        self.__state = state

    def get_uid(self) -> int:
        return self.__uid

    def get_state(self) -> States:
        return self.__state

    def cancel(self) -> None | Exception:
        if self.__state == States.Earring:
            self.__state = States.Cancelled
            return

        raise Exception(f"The order with id {self.__uid} can't be cancelled")

    def deliver(self) -> None | Exception:
        if self.__state == States.Sent:
            self.__state = States.Delivered
            return

        raise Exception(f"The order with id {self.__uid} can't be delivered")

    def print_state(self) -> Self:
        print(f"The order with id {self.__uid} is {self.__state.name.lower()}")
        return self

    def send(self) -> None | Exception:
        if self.__state == States.Earring:
            self.__state = States.Sent
            return

        raise Exception(f"The order with id {self.__uid} can't be sent")


first_order: Order = Order(uid=1, state=States.Earring)
second_order: Order = Order(uid=2, state=States.Sent)
third_order: Order = Order(uid=3, state=States.Delivered)
fourth_order: Order = Order(uid=4, state=States.Cancelled)

print()
first_order.print_state()
second_order.print_state()
third_order.print_state()
fourth_order.print_state()

first_order.send()
first_order.deliver()

print()
first_order.print_state()

print()
try:
    second_order.send()
except Exception as error:
    print(error)

try:
    third_order.deliver()
except Exception as error:
    print(error)

try:
    fourth_order.send()
except Exception as error:
    print(error)
