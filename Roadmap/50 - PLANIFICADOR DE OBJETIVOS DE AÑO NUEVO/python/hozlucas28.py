# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,consider-using-dict-items,line-too-long

from datetime import datetime
from pathlib import Path
from typing import TypedDict, Union, TypeVar, Iterable, Callable
from uuid import UUID, uuid4

# ---------------------------------------------------------------------------- #
#                                     TYPES                                    #
# ---------------------------------------------------------------------------- #

YearPlan = TypedDict(
    "YearPlan",
    {
        "january": list[list[Union["Goal", int]]],
        "february": list[list[Union["Goal", int]]],
        "march": list[list[Union["Goal", int]]],
        "april": list[list[Union["Goal", int]]],
        "may": list[list[Union["Goal", int]]],
        "june": list[list[Union["Goal", int]]],
        "july": list[list[Union["Goal", int]]],
        "august": list[list[Union["Goal", int]]],
        "september": list[list[Union["Goal", int]]],
        "october": list[list[Union["Goal", int]]],
        "november": list[list[Union["Goal", int]]],
        "december": list[list[Union["Goal", int]]],
    },
)

# ---------------------------------------------------------------------------- #
#                                  EXCEPTIONS                                  #
# ---------------------------------------------------------------------------- #


class MonthsOutOfRangeException(Exception):
    def __init__(self) -> None:
        super().__init__("Months out of range")


# ---------------------------------------------------------------------------- #
#                                    CLASSES                                   #
# ---------------------------------------------------------------------------- #


# ----------------------------------- Goal ----------------------------------- #


class Goal:
    __amount: int
    __description: str
    __uid: UUID
    __months_limit: int
    __units: str

    def __init__(
        self, *, _amount: int, _description: str, _months_limit: int, _units: str
    ) -> None:
        self.__amount = _amount
        self.__description = _description
        self.__uid = uuid4()
        self.__units = _units

        if _months_limit < 1 or _months_limit > Goal.max_months_limit():
            raise MonthsOutOfRangeException()

        self.__months_limit = _months_limit

    @staticmethod
    def max_months_limit() -> int:
        return 12

    @property
    def amount(self) -> int:
        return self.__amount

    @property
    def description(self) -> str:
        return self.__description

    @property
    def uid(self) -> UUID:
        return self.__uid

    @property
    def months_limit(self) -> int:
        return self.__months_limit

    @property
    def units(self) -> str:
        return self.__units

    def to_year_plan(self) -> YearPlan:
        year_plan: YearPlan = {
            "january": [],
            "february": [],
            "march": [],
            "april": [],
            "may": [],
            "june": [],
            "july": [],
            "august": [],
            "september": [],
            "october": [],
            "november": [],
            "december": [],
        }

        counter: int = self.__amount
        while counter:
            month_counter: int = self.__months_limit
            for _key in year_plan:
                if not counter or not month_counter:
                    break

                try:
                    year_plan[_key][0][1] += 1
                except IndexError:
                    year_plan[_key].append([self, 1])

                month_counter -= 1
                counter -= 1

        return year_plan


# --------------------------------- YearGoals -------------------------------- #


class YearGoals:
    __goals: list[Goal]
    __plan: YearPlan

    def __init__(self) -> None:
        self.__goals = []

        self.__plan = {
            "january": [],
            "february": [],
            "march": [],
            "april": [],
            "may": [],
            "june": [],
            "july": [],
            "august": [],
            "september": [],
            "october": [],
            "november": [],
            "december": [],
        }

    @staticmethod
    def max_goals() -> int:
        return 10

    @property
    def goals(self) -> list[Goal]:
        return self.__goals

    @property
    def plan(self) -> YearPlan:
        return self.__plan

    def __append_goal_to_plan(self, *, _goal: Goal) -> None:
        goal_year_plan: YearPlan = _goal.to_year_plan()

        aux: YearPlan = self.plan

        for _key in goal_year_plan:
            if goal_year_plan[_key]:
                aux[_key].append(*goal_year_plan[_key])
                continue
            break

        self.__plan = aux

    def __remove_goal_from_plan(self, *, uid: UUID) -> None:
        def __fn(element: list[Union[Goal, int]]) -> bool:
            return element[0].uid == uid  # type: ignore

        aux: YearPlan = self.plan

        for _key in self.__plan:
            goal_i: int = index_fn(iterable=aux[_key], fn=__fn)
            if goal_i == -1:
                break

            aux[_key] = [*aux[_key][:goal_i], aux[_key][goal_i + 1 :]]

    def add_goal(self, *, new_goal: Goal) -> bool:
        if len(self.__goals) == YearGoals.max_goals():
            return False

        new_goal_uid: UUID = new_goal.uid

        goal_i: int = index_fn(
            iterable=self.__goals, fn=lambda value: value.uid == new_goal_uid
        )
        if goal_i != -1:
            return False

        self.__goals.append(new_goal)
        self.__append_goal_to_plan(_goal=new_goal)

        return True

    def remove_goal(self, *, uid: UUID) -> bool:
        goal_i: int = index_fn(iterable=self.__goals, fn=lambda goal: goal.uid == uid)
        if goal_i == -1:
            return False

        self.__goals = [*self.__goals[:goal_i], *self.__goals[goal_i + 1 :]]
        self.__remove_goal_from_plan(uid=uid)

        return True

    def save_plan(
        self,
        *,
        _path: str,
        row: Callable[[Goal, int, int], str],
        month_title: Callable[[str], str] = lambda month: month.capitalize(),
    ) -> None:
        data: list[str] = []

        for _key in self.__plan:
            goals_month: list[list[Union[Goal, int]]] = self.__plan[_key]

            rows: list[str] = [month_title(_key)]
            for _i, [_goal, _amount] in enumerate(iterable=goals_month):
                rows.append(row(_goal, _amount, _i))  # type: ignore

            data.append("\n".join(rows))
            data.append("\n\n")

        with open(file=_path, mode="wt", encoding="utf-8") as file:
            file.writelines(data)
            file.close()


# ---------------------------------------------------------------------------- #
#                                   UTILITIES                                  #
# ---------------------------------------------------------------------------- #

T = TypeVar("T")


def index_fn(*, iterable: Iterable[T], fn: Callable[[T], bool]) -> int:
    for _i, element in enumerate(iterable=iterable):
        if fn(element):
            return _i
    return -1


def goal_to_row(_goal: Goal, _amount: int, index: int) -> str:
    _desc: str = _goal.description
    _units: str = _goal.units
    _total_amount: int = _goal.amount
    return f"[ ] {index + 1}. {_desc} ({_amount} {_units}/mes). Total: {_total_amount}."


# ---------------------------------------------------------------------------- #
#                                     MAIN                                     #
# ---------------------------------------------------------------------------- #

year_goals: YearGoals = YearGoals()


print(
    "> Available operations:\n\n"
    + " 1 - Add goal.\n"
    + " 2 - Remove goal.\n"
    + " 3 - Show goals.\n"
    + " 4 - Show plan.\n"
    + " 5 - Save plan.\n"
    + " 0 - Exit."
)

user_input: str = input("\n> Select an operation: ").strip()

while user_input != "0":
    match (user_input):
        case "1":
            print("\n> Complete the following goal data...")
            units: str = input("\n> Units: ").strip()
            amount: int = int(input("\n> Amount (as a number): ").strip())
            description: str = input("\n> Description: ").strip()

            months_limit: int = int(input("\n> Months limit (as a number): ").strip())
            while months_limit < 1 or months_limit > Goal.max_months_limit():
                print(
                    "\n> Error! Months limit must be between 1 and 12 (both included). Try again..."
                )
                months_limit = int(input("\n> Months limit (as a number): ").strip())

            goal: Goal = Goal(
                _amount=amount,
                _description=description,
                _months_limit=months_limit,
                _units=units,
            )

            if year_goals.add_goal(new_goal=goal):
                print("\n> Goal added!")
            else:
                print("\n> An error occurred! The goal was not added.")

        case "2":
            goal_uid: UUID = UUID(input("\n> Goal id to remove: ").strip())

            if year_goals.remove_goal(uid=goal_uid):
                print(f'\n> Goal "{goal_uid}" removed!')
            else:
                print("\n> An error occurred! The goal was not removed.")

        case "3":
            goals_rows: list[str] = []
            for _goal in year_goals.goals:
                goals_rows.append(
                    f'\n• Goal "{_goal.uid}"...'
                    + f'\n\n  - ID: "{_goal.uid}".'
                    + f'\n  - Description: "{_goal.description}".'
                    + f"\n  - Months limit: {_goal.months_limit}."
                    + f"\n  - Amount: {_goal.amount}."
                    + f'\n  - Units: "{_goal.units}".'
                )

            if goals_rows:
                print("\n".join(goals_rows))

        case "4":
            plan: YearPlan = year_goals.plan

            plan_rows: list[str] = []
            for key in plan:
                goals: list[list[Union[Goal, int]]] = plan[key]

                plan_row: str = f"\n{key.capitalize()}:"
                for i, [goal, amount] in enumerate(iterable=goals):  # type: ignore
                    desc: str = goal.description
                    units: str = goal.units
                    total_amount: int = goal.amount
                    plan_row += f"\n[ ] {i + 1}. {desc} ({amount} {units}/mes). Total: {total_amount}."

                plan_rows.append(plan_row)

            if plan_rows:
                print("\n".join(plan_rows))

        case "5":
            current_date: datetime = datetime.now()
            path: str = f"{Path().absolute()}\\plan-{current_date.year}.txt"
            year_goals.save_plan(_path=path, row=goal_to_row)

            print(f'\n> Plan saved in "{path}" path.')

        case "_":
            print("\n> Invalid operation! Try again...")

    print(
        "\n> Available operations:\n\n"
        + " 1 - Add goal.\n"
        + " 2 - Remove goal.\n"
        + " 3 - Show goals.\n"
        + " 4 - Show plan.\n"
        + " 5 - Save plan.\n"
        + " 0 - Exit."
    )

    user_input = input("\n> Select an operation: ").strip()
