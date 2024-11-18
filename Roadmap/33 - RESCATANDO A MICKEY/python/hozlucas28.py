# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,too-few-public-methods,expression-not-assigned

from abc import ABCMeta, abstractmethod
from typing import TypedDict, Literal, Self, cast

# ---------------------------------------------------------------------------- #
#                                     TYPES                                    #
# ---------------------------------------------------------------------------- #


Cell = Literal["⬜️", "⬛️", "🐭", "🚪"]

Dashboard = list[list[Cell]]

Position = TypedDict("Position", {"x": int, "y": int})


# ---------------------------------------------------------------------------- #
#                                  EXCEPTIONS                                  #
# ---------------------------------------------------------------------------- #


class ExitNotFoundException(Exception):
    def __init__(self) -> None:
        super().__init__("exit not found")


class GameOverException(Exception):
    def __init__(self) -> None:
        super().__init__("game over")


class InvalidPlayerPositionException(Exception):
    def __init__(self, *, invalidPos: "Position") -> None:
        super().__init__(
            f"position ({invalidPos['x']}, {invalidPos['y']}) is invalid for a player"
        )


class PlayerNotFoundException(Exception):
    def __init__(self) -> None:
        super().__init__("player not found")


# ---------------------------------------------------------------------------- #
#                                    CLASSES                                   #
# ---------------------------------------------------------------------------- #


# ----------------------------------- Maze ----------------------------------- #

InitialPositions = TypedDict("InitialPositions", {"exit": Position, "player": Position})


class AbcMaze(metaclass=ABCMeta):
    @property
    @abstractmethod
    def dashboard(self) -> Dashboard:
        pass

    @property
    @abstractmethod
    def exit_pos(self) -> Position:
        pass

    @property
    @abstractmethod
    def player_pos(self) -> Position:
        pass

    @player_pos.setter
    def player_pos(self, pos: Position) -> None:
        pass


class Maze(AbcMaze):
    __dashboard: Dashboard
    __exit_pos: Position
    __player_pos: Position
    __original_cell_at_player_pos: Cell

    def __init__(self, *, dashboard: Dashboard) -> None:
        initial_positions: InitialPositions = self.__get_initial_positions(
            dashboard=dashboard
        )
        self.__dashboard = dashboard
        self.__exit_pos = initial_positions["exit"]
        self.__player_pos = initial_positions["player"]
        self.__original_cell_at_player_pos = "⬜️"

    def __get_initial_positions(self, *, dashboard: Dashboard) -> InitialPositions:
        exit_pos: Position = {"x": -1, "y": -1}
        player_pos: Position = {"x": -1, "y": -1}

        for y, row in enumerate(iterable=dashboard):
            for x, col in enumerate(iterable=row):
                if col == "🐭":
                    player_pos["x"] = x
                    player_pos["y"] = y
                elif col == "🚪":
                    exit_pos["x"] = x
                    exit_pos["y"] = y

        if exit_pos["x"] < 0:
            raise ExitNotFoundException()

        if player_pos["x"] < 0:
            raise PlayerNotFoundException()

        return {"exit": exit_pos, "player": player_pos}

    @property
    def dashboard(self) -> Dashboard:
        return self.__dashboard

    @property
    def exit_pos(self) -> Position:
        return self.__exit_pos

    @property
    def player_pos(self) -> Position:
        return self.__player_pos

    @player_pos.setter
    def player_pos(self, pos: Position) -> None:
        if not self.__is_valid_pos_for_player(pos=pos):
            raise InvalidPlayerPositionException(invalidPos=pos)

        x, y = pos["x"], pos["y"]
        px, py = self.__player_pos["x"], self.__player_pos["y"]
        pre_original_cell_at_player_pos = self.__original_cell_at_player_pos

        self.__original_cell_at_player_pos = self.__dashboard[y][x]
        self.__dashboard[y][x] = "🐭"
        self.__dashboard[py][px] = pre_original_cell_at_player_pos
        self.__player_pos = pos

    def __is_valid_pos(self, *, pos: Position) -> bool:
        x, y = pos["x"], pos["y"]
        dashboard = self.__dashboard

        dashboard_max_y: int = len(dashboard) - 1
        out_of_y_range: bool = y < 0 or y > dashboard_max_y
        if out_of_y_range:
            return False

        dashboard_max_x: int = len(dashboard[0]) - 1
        out_of_x_range: bool = x < 0 or x > dashboard_max_x
        if out_of_x_range:
            return False

        return True

    def __is_valid_pos_for_player(self, *, pos: Position) -> bool:
        if not self.__is_valid_pos(pos=pos):
            return False

        x, y = pos["x"], pos["y"]
        cell_at_pos: Cell = self.__dashboard[y][x]

        obstacle_at_pos: bool = cell_at_pos == "⬛️"
        return not obstacle_at_pos


# ----------------------------------- Game ----------------------------------- #

type Move = Literal["down", "left", "right", "up"]


class AbcGame(metaclass=ABCMeta):
    @property
    @abstractmethod
    def game_over(self) -> bool:
        pass

    @property
    @abstractmethod
    def maze(self) -> AbcMaze:
        pass

    @abstractmethod
    def move_player(self, *, _move: Move) -> Self:
        pass


class Game(AbcGame):
    __game_over: bool
    __maze: AbcMaze

    def __init__(self, *, _maze: AbcMaze) -> None:
        self.__maze = _maze
        self.__game_over = self.__is_game_over()

    @property
    def game_over(self) -> bool:
        return self.__game_over

    @property
    def maze(self) -> AbcMaze:
        return self.__maze

    def move_player(self, *, _move: Move) -> Self:
        if self.__game_over:
            raise GameOverException()

        _maze: AbcMaze = self.__maze

        curren_player_pos = _maze.player_pos
        x, y = curren_player_pos["x"], curren_player_pos["y"]

        match _move:
            case "down":
                _maze.player_pos = {"x": x, "y": y + 1}
            case "left":
                _maze.player_pos = {"x": x - 1, "y": y}
            case "right":
                _maze.player_pos = {"x": x + 1, "y": y}
            case "up":
                _maze.player_pos = {"x": x, "y": y - 1}

        self.__game_over = self.__is_game_over()
        return self

    def __is_game_over(self) -> bool:
        _maze: AbcMaze = self.__maze
        player_pos = _maze.player_pos
        exit_pos = _maze.exit_pos

        px, py = player_pos["x"], player_pos["y"]
        ex, ey = exit_pos["x"], exit_pos["y"]

        player_at_exit_pos: bool = px == ex and py == ey

        return player_at_exit_pos


# ---------------------------------------------------------------------------- #
#                                     UTILS                                    #
# ---------------------------------------------------------------------------- #


def print_dashboard(*, _dashboard: Dashboard) -> None:
    print("[")

    for row in _dashboard:
        print(f" {row}")

    print("]")


# ---------------------------------------------------------------------------- #
#                                     MAIN                                     #
# ---------------------------------------------------------------------------- #


maze: Maze = Maze(
    dashboard=[
        ["🚪", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
        ["⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️"],
        ["⬜️", "⬛️", "⬜️", "⬛️", "⬜️", "⬜️"],
        ["⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "🐭"],
        ["⬛️", "⬛️", "⬜️", "⬛️", "⬜️", "⬛️"],
        ["⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️"],
    ]
)

game: Game = Game(_maze=maze)
print_dashboard(_dashboard=game.maze.dashboard)

while not game.game_over:
    move: str = input("\n> Enter a move ('up', 'right', 'left', or 'down'): ")

    try:
        print()

        match cast(Move, move.strip().lower()):
            case "down":
                game.move_player(_move="down")
                print_dashboard(_dashboard=game.maze.dashboard)

            case "left":
                game.move_player(_move="left")
                print_dashboard(_dashboard=game.maze.dashboard)

            case "right":
                game.move_player(_move="right")
                print_dashboard(_dashboard=game.maze.dashboard)

            case "up":
                game.move_player(_move="up")
                print_dashboard(_dashboard=game.maze.dashboard)

            case _:
                print("> Invalid move! Try again...")

    except InvalidPlayerPositionException:
        print("> Player can not move down!")

print("\n> Game over!")
