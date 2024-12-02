# pylint: disable=missing-module-docstring,missing-class-docstring,broad-exception-caught,missing-function-docstring,line-too-long

from abc import ABCMeta, abstractmethod
from os import system
from typing import TypedDict

# ---------------------------------------------------------------------------- #
#                                     TYPES                                    #
# ---------------------------------------------------------------------------- #

CalendarCell = TypedDict("CalendarCell", {"discovered": bool, "id": int})

# ---------------------------------------------------------------------------- #
#                                    ERRORS                                    #
# ---------------------------------------------------------------------------- #


class CalendarCellDiscoveredError(Exception):
    def __init__(self, *, cell: CalendarCell) -> None:
        super().__init__(f"{cell["id"]} calendar cell is already discovered")


class CalendarDayNotFoundError(Exception):
    def __init__(self, *, day: int) -> None:
        super().__init__(f"{day} calendar day not found")


class CalendarDayOuOfRangeError(Exception):
    def __init__(self, *, _day: int, _from: int, _to: int) -> None:
        super().__init__(
            f"{_day} calendar day is out of range, it must be between {_from} and {_to} (both included)"
        )


# ---------------------------------------------------------------------------- #
#                                    CLASSES                                   #
# ---------------------------------------------------------------------------- #

# --------------------------------- Calendar --------------------------------- #


class AbcCalendar(metaclass=ABCMeta):
    @property
    @abstractmethod
    def _array(self) -> list[list[CalendarCell]]:
        pass

    @property
    @abstractmethod
    def from_(self) -> int:
        pass

    @property
    @abstractmethod
    def to_(self) -> int:
        pass

    @abstractmethod
    def discover_day(self, *, day: int) -> None:
        pass

    @abstractmethod
    def to_print(self) -> str:
        pass


class Calendar(AbcCalendar):
    __array: list[list[CalendarCell]]
    __from: int
    __to: int

    def __init__(self, *, _from: int, _to: int) -> None:
        counter: int = _from

        self.__from = _from
        self.__to = _to

        self.__array: list[list[CalendarCell]] = []
        for i in range(0, Calendar.rows()):
            self.__array.append([])

            for _ in range(0, Calendar.cols()):
                self.__array[i].append({"discovered": False, "id": counter})
                counter += 1

    @staticmethod
    def rows() -> int:
        return 4

    @staticmethod
    def cols() -> int:
        return 6

    @property
    def _array(self) -> list[list[CalendarCell]]:
        return self.__array

    @property
    def from_(self) -> int:
        return self.__from

    @property
    def to_(self) -> int:
        return self.__to

    def discover_day(self, *, day: int) -> None:
        flag: bool = False
        counter: int = self.__from

        if day < self.__from or day > self.__to:
            raise CalendarDayOuOfRangeError(_day=day, _from=self.__from, _to=self.__to)

        for i, _ in enumerate(iterable=self.__array):
            if counter > self.__to:
                break

            for j, _ in enumerate(iterable=self.__array[i]):
                if counter > self.__to:
                    break

                if self.__array[i][j]["id"] == day:
                    if self.__array[i][j]["discovered"]:
                        raise CalendarCellDiscoveredError(cell=self.__array[i][j])

                    self.__array[i][j]["discovered"] = True
                    flag = True
                    break

                counter += 1

            if flag:
                break

        if not flag:
            raise CalendarDayNotFoundError(day=day)

    def to_print(self) -> str:
        calendar_printable: list[str] = []

        counter: int = self.__from

        for i, row in enumerate(iterable=self.__array):
            if counter > self.__to:
                break

            row: list[CalendarCell] = self.__array[i]

            row_printable: str = "" if i == 0 else "\n"
            row_printable += (f"{'*'*4} " * len(row)).rstrip() + "\n"

            for _, col in enumerate(iterable=row):
                if counter > self.__to:
                    break

                row_printable += f"*{''.ljust(2,'*') if col['discovered'] else str(object=col['id']).rjust(2, '0')}* "
                counter += 1

            row_printable = f"{row_printable.rstrip()}\n"
            row_printable += (f"{'*'*4} " * len(row)).rstrip()

            calendar_printable.append(row_printable)

        calendar_printable_str: str = ""
        for i, tempo in enumerate(iterable=calendar_printable):
            calendar_printable_str += tempo if (i == 0) else f"\n{tempo}"

        return calendar_printable_str


# ---------------------------------------------------------------------------- #
#                                     MAIN                                     #
# ---------------------------------------------------------------------------- #


calendar: AbcCalendar = Calendar(_from=1, _to=24)

print(calendar.to_print())

print(
    "\n> Available operations...\n\n",
    "  1 - Discover day.\n",
    "  0 - Exit.",
)

input01: str = input("\n> Enter an operation: ").strip()

while input01 != "0":
    match (input01):
        case "1":
            input02: str = input("\n> Enter the day to discover: ").strip()

            try:
                calendar.discover_day(day=int(input02))
                system(command="clear")
                print(f"> Day {input02} discovered!")

            except CalendarDayOuOfRangeError as error:
                system(command="clear")
                print(
                    f"\n> The day {input02} must be between {calendar.from_} and {calendar.to_} (both included)!"
                )

            except CalendarCellDiscoveredError as error:
                system(command="clear")
                print(f"\n> The day {input02} is already discovered!")

            except CalendarDayNotFoundError as error:
                system(command="clear")
                print(f"\n> {input02} day not found in the calendar!")

            except Exception as error:
                system(command="clear")
                print("\n> An error occurred on discover the day!")

        case _:
            system(command="clear")
            print("\n> Invalid operation! Try again...")

    print(f"\n{calendar.to_print()}")

    print(
        "\n> Available operations...\n\n",
        "  1 - Discover day.\n",
        "  0 - Exit.",
    )

    input01 = input("\n> Enter an operation: ").strip()
