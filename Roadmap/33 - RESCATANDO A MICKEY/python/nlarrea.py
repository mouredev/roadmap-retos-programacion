"""
 * EJERCICIO:
 * ¡Disney ha presentado un montón de novedades en su D23! 
 * Pero... ¿Dónde está Mickey?
 * Mickey Mouse ha quedado atrapado en un laberinto mágico 
 * creado por Maléfica.
 * Desarrolla un programa para ayudarlo a escapar.
 * Requisitos:
 * 1. El laberinto está formado por un cuadrado de 6x6 celdas.
 * 2. Los valores de las celdas serán:
 *    - "⬜️" Vacío
 *    - ⬛️ Obstáculo
 *    - 🐭 Mickey
 *    - 🚪 Salida
 * Acciones:
 * 1. Crea una matriz que represente el laberinto (no hace falta
 * que se genere de manera automática).
 * 2. Interactúa con el usuario por consola para preguntarle hacia
 * donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
 * 3. Muestra la actualización del laberinto tras cada desplazamiento.
 * 4. Valida todos los movimientos, teniendo en cuenta los límites
 * del laberinto y los obstáculos. Notifica al usuario.
 * 5. Finaliza el programa cuando Mickey llegue a la salida.
"""

from enum import Enum
from typing import Literal


EMPTY = "⬜️"
PLAYER = "🐭"
EXIT = "🚪"
OBSTACLE = "⬛️"

MAZE = [
    [PLAYER, OBSTACLE, OBSTACLE, OBSTACLE, OBSTACLE, OBSTACLE],
    [EMPTY, OBSTACLE, OBSTACLE, OBSTACLE, EMPTY, OBSTACLE],
    [EMPTY, OBSTACLE, OBSTACLE, OBSTACLE, EMPTY, OBSTACLE],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [OBSTACLE, EMPTY, OBSTACLE, EMPTY, OBSTACLE, OBSTACLE],
    [OBSTACLE, EMPTY, OBSTACLE, EMPTY, EMPTY, EXIT],
]


class Action(Enum):
    UP = "w"
    DOWN = "s"
    RIGHT = "d"
    LEFT = "a"
    EXIT = "q"


class Position:
    def __init__(self, row: int, col: int, max_row: int, max_col: int):
        self.row = row
        self.col = col
        self._max_row = max_row
        self._max_col = max_col

    def __eq__(self, value: object):
        if isinstance(value, Position):
            return value.row == self.row and value.col == self.col

        return False

    def __hash__(self) -> int:
        return hash(self.row, self.col)

    def move(self, direction: str):
        if direction == Action.UP.value:
            self._up()
        elif direction == Action.DOWN.value:
            self._down()
        elif direction == Action.RIGHT.value:
            self._right()
        elif direction == Action.LEFT.value:
            self._left()
        else:
            print(f"La dirección '{direction}' no es posible.")

    def _up(self) -> tuple[int, int]:
        if self.row > 0:
            self.row -= 1
        return (self.row, self.col)

    def _down(self) -> tuple[int, int]:
        if self.row < self._max_row:
            self.row += 1
        return (self.row, self.col)

    def _left(self) -> tuple[int, int]:
        if self.col > 0:
            self.col -= 1
        return (self.row, self.col)

    def _right(self) -> tuple[int, int]:
        if self.col < self._max_col:
            self.col += 1
        return (self.row, self.col)


def select_movement() -> str:
    keys = [action.value for action in Action]
    while True:
        print("Movimientos posibles:")
        for action in Action:
            print(f" [{action.value.upper()}]: {action.name.capitalize()}")

        try:
            selection = input("Selecciona qué hacer:\n > ")
            assert (
                selection.isalpha() and selection.lower() in keys
            ), f"\nDebes introducir una de las siguientes letras: {', '.join(keys)}"

        except AssertionError as error:
            print(error)

        else:
            return selection.lower()


def print_maze(maze: list[list[str]]):
    print()
    for row in maze:
        print("".join(row))
    print()


def update_maze(
    maze: list[list[str]], new_position: Position
) -> list[list[str]]:
    # Get current player's position
    old_player_pos = get_position(maze, PLAYER)

    # Update player position to be empty from now on
    maze[old_player_pos.row][old_player_pos.col] = EMPTY
    # Update maze to show player in new position
    maze[new_position.row][new_position.col] = PLAYER

    return maze


def get_position(maze: list[list[str]], item: Literal["🐭", "🚪"]) -> Position:
    for nrow, row in enumerate(maze):
        for ncol, col in enumerate(row):
            if col == item:
                return Position(
                    row=nrow, col=ncol, max_row=len(maze), max_col=len(row)
                )


def actions(maze: list[list[str]], position: Position) -> list[str]:
    actions_ = []

    # Up
    if position.row > 0 and maze[position.row - 1][position.col] in [
        EMPTY,
        EXIT,
    ]:
        actions_.append(Action.UP.value)

    # Down
    if position.row < len(maze) - 1 and maze[position.row + 1][
        position.col
    ] in [EMPTY, EXIT]:
        actions_.append(Action.DOWN.value)

    # Left
    if position.col > 0 and maze[position.row][position.col - 1] in [
        EMPTY,
        EXIT,
    ]:
        actions_.append(Action.LEFT.value)

    # Right
    if position.col < len(maze) - 1 and maze[position.row][
        position.col + 1
    ] in [EMPTY, EXIT]:
        actions_.append(Action.RIGHT.value)

    return actions_


def run(maze: list[list[str]]):
    EXIT_POS = get_position(maze, EXIT)
    player_pos = get_position(maze, PLAYER)

    while True:
        print_maze(maze)

        selected = select_movement()
        available_actions = actions(maze, player_pos)

        if selected == Action.EXIT.value:
            print("\nSaliendo del juego.")
            break

        elif selected not in available_actions:
            print("\nLa opción que has escogido no es posible.")
            continue

        player_pos.move(selected)
        maze = update_maze(maze, player_pos)

        if player_pos == EXIT_POS:
            print_maze(maze)
            print("\n\n¡HAS ENCONTRADO LA SALIDA!")
            break


if __name__ == "__main__":
    run(MAZE)
