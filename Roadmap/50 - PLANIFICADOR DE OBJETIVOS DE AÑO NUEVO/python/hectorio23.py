# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

from datetime import datetime
from pathlib import Path
from typing import TypedDict, Union, TypeVar, Iterable, Callable
from uuid import UUID, uuid4

##################################
########## Data Types ############            
##################################

class YearPlan(TypedDict):
    """Represents a detailed plan for goals across the months of a year."""
    january: list[list[Union["Goal", int]]]
    february: list[list[Union["Goal", int]]]
    march: list[list[Union["Goal", int]]]
    april: list[list[Union["Goal", int]]]
    may: list[list[Union["Goal", int]]]
    june: list[list[Union["Goal", int]]]
    july: list[list[Union["Goal", int]]]
    august: list[list[Union["Goal", int]]]
    september: list[list[Union["Goal", int]]]
    october: list[list[Union["Goal", int]]]
    november: list[list[Union["Goal", int]]]
    december: list[list[Union["Goal", int]]]

###################################
######## Custom Exceptions ########       
###################################

class MonthsOutOfRangeException(Exception):
    """Exception raised when the month limit for a goal is out of valid range."""
    def __init__(self) -> None:
        super().__init__("Months out of range. Valid range is 1 to 12.")

###################################
########### Core Classes ##########           
###################################

class Goal:
    """Represents an individual goal with its details and constraints."""

    def __init__(self, *, amount: int, description: str, months_limit: int, units: str) -> None:
        self.amount = amount
        self.description = description
        self.uid = uuid4()
        self.units = units

        if months_limit < 1 or months_limit > self.max_months_limit():
            raise MonthsOutOfRangeException()

        self.months_limit = months_limit

    @staticmethod
    def max_months_limit() -> int:
        """Returns the maximum allowed months for a goal."""
        return 12

    def to_monthly_plan(self) -> YearPlan:
        """Generates a yearly plan for the goal based on its amount and months limit."""
        year_plan: YearPlan = {month: [] for month in YearPlan.__annotations__.keys()}
        remaining_amount = self.amount

        for month in year_plan:
            if remaining_amount <= 0:
                break

            month_amount = min(remaining_amount, self.months_limit)
            year_plan[month].append([self, month_amount])
            remaining_amount -= month_amount

        return year_plan


class YearGoals:
    """Manages a collection of goals and their aggregated yearly plan."""

    def __init__(self) -> None:
        self.goals = []
        self.plan = {month: [] for month in YearPlan.__annotations__.keys()}

    @staticmethod
    def max_goals() -> int:
        """Returns the maximum number of goals allowed."""
        return 10

    def add_goal(self, goal: Goal) -> None:
        """Adds a new goal to the collection and updates the yearly plan."""
        if len(self.goals) >= self.max_goals():
            raise ValueError("Maximum number of goals reached.")

        self.goals.append(goal)
        self._update_plan_with_goal(goal)

    def _update_plan_with_goal(self, goal: Goal) -> None:
        """Incorporates a new goal into the existing yearly plan."""
        goal_plan = goal.to_monthly_plan()

        for month, tasks in goal_plan.items():
            self.plan[month].extend(tasks)

    def save_plan(self, file_path: str) -> None:
        """Saves the yearly plan to a text file."""
        with open(file_path, "w", encoding="utf-8") as file:
            for month, tasks in self.plan.items():
                file.write(f"{month.capitalize()}:\n")
                for idx, (goal, amount) in enumerate(tasks):
                    file.write(f"[ ] {idx + 1}. {goal.description} ({amount} {goal.units}/month). Total: {goal.amount}.\n")
                file.write("\n")

####################################
######## Utility Functions #########        
####################################

def get_user_input(prompt: str, validate: Callable[[str], bool] = lambda x: True) -> str:
    """Prompts the user for input and validates the response."""
    while True:
        response = input(prompt).strip()
        if validate(response):
            return response
        print("Invalid input. Please try again.")

####################################
########## Main Program Loop #######        
####################################

def main() -> None:
    """Main entry point for the Goal Management application."""
    year_goals = YearGoals()

    menu = (
        "\nGoal Management System\n"
        "------------------------\n"
        "1. Add a new goal\n"
        "2. Remove an existing goal\n"
        "3. Display all goals\n"
        "4. Show detailed plan\n"
        "5. Save plan to file\n"
        "0. Exit\n"
    )

    while True:
        print(menu)
        choice = get_user_input("Select an option: ", lambda x: x.isdigit() and 0 <= int(x) <= 5)

        if choice == "0":
            print("Goodbye!")
            break

        if choice == "1":
            description = get_user_input("Enter goal description: ")
            units = get_user_input("Enter units (e.g., books, hours): ")
            amount = int(get_user_input("Enter amount: ", lambda x: x.isdigit()))
            months_limit = int(get_user_input("Enter months limit (1-12): ", lambda x: x.isdigit() and 1 <= int(x) <= 12))

            try:
                goal = Goal(amount=amount, description=description, months_limit=months_limit, units=units)
                year_goals.add_goal(goal)
                print("Goal added successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            goal_uid = get_user_input("Enter the ID of the goal to remove: ")
            year_goals.goals = [g for g in year_goals.goals if str(g.uid) != goal_uid]
            print("Goal removed, if it existed.")

        elif choice == "3":
            if not year_goals.goals:
                print("No goals available.")
            else:
                for goal in year_goals.goals:
                    print(f"- {goal.description} ({goal.amount} {goal.units} over {goal.months_limit} months)")

        elif choice == "4":
            for month, tasks in year_goals.plan.items():
                print(f"{month.capitalize()}:\n")
                for idx, (goal, amount) in enumerate(tasks):
                    print(f"  [ ] {idx + 1}. {goal.description} ({amount} {goal.units}/month). Total: {goal.amount}.")
                print()

        elif choice == "5":
            file_path = f"plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            year_goals.save_plan(file_path)
            print(f"Plan saved to {file_path}")

if __name__ == "__main__":
    main()
