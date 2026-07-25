# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from abc import ABCMeta, abstractmethod
from typing import Self
from os import system

# ---------------------------------------------------------------------------- #
#                                    CLASSES                                   #
# ---------------------------------------------------------------------------- #


class AbcChristmasTree(metaclass=ABCMeta):
    @property
    @abstractmethod
    def height(self) -> int:
        pass

    @property
    @abstractmethod
    def tree(self) -> str:
        pass

    @abstractmethod
    def add_balls(self, *, ball: str) -> Self:
        pass

    @abstractmethod
    def add_lights(self, *, light: str) -> Self:
        pass

    @abstractmethod
    def add_star(self, *, star: str) -> Self:
        pass

    @abstractmethod
    def remove_balls(self, *, ball: str) -> Self:
        pass

    @abstractmethod
    def remove_lights(self, *, light: str) -> Self:
        pass

    @abstractmethod
    def remove_star(self, *, star: str) -> Self:
        pass

    @abstractmethod
    def turn_off_lights(self, *, light_off: str) -> Self:
        pass

    @abstractmethod
    def turn_on_lights(self, *, light_on: str) -> Self:
        pass


class ChristmasTree(AbcChristmasTree):
    __height: int
    __tree: list[str]
    __lights_indexes: list[list[int]]

    def __init__(self, *, height: int) -> None:
        tree: list[str] = []

        for i in range(height):
            branch_blank_spaces: str = " " * (height - i - 1) if height >= 2 else " "
            tree.append(branch_blank_spaces + "*" * (i * 2 + 1))

        trunk_blank_spaces: str = " " * (height - 2) if height >= 2 else ""
        tree.append(trunk_blank_spaces + "|||")
        tree.append(trunk_blank_spaces + "|||")

        self.__height = height
        self.__lights_indexes = []
        self.__tree = tree

    @property
    def height(self) -> int:
        return self.__height

    @property
    def tree(self) -> str:
        return "\n".join(self.__tree)

    def add_balls(self, *, ball: str) -> Self:
        for i in range(1, len(self.__tree) - 2):
            branch: str = self.__tree[i]
            counter: int = 0

            new_branch: str = ""

            for char in branch:
                new_branch += ball if not (counter % 2) and char == "*" else char
                counter += 1

            self.__tree[i] = new_branch

        return self

    def add_lights(self, *, light: str) -> Self:
        for i in range(1, len(self.__tree) - 1):
            branch: str = self.__tree[i]
            counter: int = 0

            new_branch: str = ""

            for j, char in enumerate(iterable=branch):
                if counter % 2 and char == "*":
                    new_branch += light
                    self.__lights_indexes.append([i, j])
                else:
                    new_branch += char

                counter += 1

            self.__tree[i] = new_branch

        return self

    def add_star(self, *, star: str) -> Self:
        self.__tree[0] = self.__tree[0].replace("*", star, 1)
        return self

    def remove_balls(self, *, ball: str) -> Self:
        for i in range(1, len(self.__tree) - 2):
            self.__tree[i] = self.__tree[i].replace(ball, "*")

        return self

    def remove_lights(self, *, light: str) -> Self:
        while len(self.__lights_indexes) != 0:
            [branch, index] = self.__lights_indexes[0]

            new_branch: str = ""

            for j in range(len(self.__tree[branch])):
                if j == index:
                    new_branch += "*"
                    self.__lights_indexes.pop(0)
                    continue

                new_branch += self.__tree[branch][j]

            self.__tree[branch] = new_branch

        return self

    def remove_star(self, *, star: str) -> Self:
        self.__tree[0] = self.__tree[0].replace(star, "*", 1)
        return self

    def turn_off_lights(self, *, light_off: str) -> Self:
        for [branch, index] in self.__lights_indexes:
            new_branch: str = ""

            for j in range(len(self.__tree[branch])):
                new_branch += light_off if j == index else self.__tree[branch][j]

            self.__tree[branch] = new_branch

        return self

    def turn_on_lights(self, *, light_on: str) -> Self:
        for [branch, index] in self.__lights_indexes:
            new_branch: str = ""

            for j in range(len(self.__tree[branch])):
                new_branch += light_on if j == index else self.__tree[branch][j]

            self.__tree[branch] = new_branch

        return self


# ---------------------------------------------------------------------------- #
#                                     MAIN                                     #
# ---------------------------------------------------------------------------- #


user_input: str = (input("> Enter the height of the christmas tree: ")).strip()

christmas_tree: AbcChristmasTree = ChristmasTree(height=int(user_input))

system(command="clear")
print(christmas_tree.tree)

print(
    "\n> Available operations...\n\n",
    "  1 - Add star.\n",
    "  2 - Remove star.\n",
    "  3 - Add balls.\n",
    "  4 - Remove balls.\n",
    "  5 - Add lights.\n",
    "  6 - Remove lights.\n",
    "  7 - Turn on lights.\n",
    "  8 - Turn off lights.\n",
    "  0 - Exit.",
)

user_input = (input("\n> Enter an operation: ")).strip()

while user_input != "0":
    match user_input:
        case "1":
            christmas_tree.add_star(star="@")

            system(command="clear")
            print(christmas_tree.tree)

        case "2":
            christmas_tree.remove_star(star="@")

            system(command="clear")
            print(christmas_tree.tree)

        case "3":
            christmas_tree.add_balls(ball="o")

            system(command="clear")
            print(christmas_tree.tree)

        case "4":
            christmas_tree.remove_balls(ball="o")

            system(command="clear")
            print(christmas_tree.tree)

        case "5":
            christmas_tree.add_lights(light="+")

            system(command="clear")
            print(christmas_tree.tree)

        case "6":
            christmas_tree.remove_lights(light="*")

            system(command="clear")
            print(christmas_tree.tree)

        case "7":
            christmas_tree.turn_on_lights(light_on="+")

            system(command="clear")
            print(christmas_tree.tree)

        case "8":
            christmas_tree.turn_off_lights(light_off="*")

            system(command="clear")
            print(christmas_tree.tree)

        case _:
            print("\n> Invalid operation! Try again...")

    print(
        "\n> Available operations...\n\n",
        "  1 - Add star.\n",
        "  2 - Remove star.\n",
        "  3 - Add balls.\n",
        "  4 - Remove balls.\n",
        "  5 - Add lights.\n",
        "  6 - Remove lights.\n",
        "  7 - Turn on lights.\n",
        "  8 - Turn off lights.\n",
        "  0 - Exit.",
    )

    user_input = (input("\n> Enter an operation: ")).strip()
