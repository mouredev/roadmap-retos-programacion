"""
Ayudar a escapar a Mickey.
- Laberinto formado por un CUADRADO de 6x6 CELDAS
    - Valores de las celdas:
        - Celda vacia
        - Celda con obstaculo
        - Mickey
        - Salida

- Acciones:
    1. Crear la matriz que represente el laberinto
    2. Interactuar con el usuario por consola para preguntarle desplazamientos
        - arriba, izquierda, derecha y abajo
    3. Mostrar actualización del laberinto tras cada desplazamiento
    4. Validar los movimientos teniendo en cuenta los limites del laberinto y los obstaculos
        - Avisar al usuario
    5. Finalizar el programa cuando Mickey llega a la salida
"""

from dataclasses import dataclass, field
from enum import StrEnum
from random import randint


@dataclass
class Maze:
    """
    Representa la estructura de datos del laberinto.

    Attributes:
        rows (int): Número de filas del laberinto. Por defecto 6.
        cols (int): Número de columnas. Se iguala a rows en __post_init__ si no se especifica.
        pos_min (int): Índice mínimo válido (0).
        pos_max (int): Índice máximo válido (calculado dinámicamente).
        maze (list): La matriz que representa el tablero de juego.
    """

    rows: int = 6
    cols: int = rows
    pos_min: int = 0
    pos_max: int = 0
    maze: list = field(default_factory=list)

    def __post_init__(self):
        """Calcula los límites dinámicos después de la inicialización."""
        self.pos_max = self.rows - 1

    def get_limits(self) -> int:
        """
        Devuelve los límites inferior y superior del laberinto.

        Returns:
            tuple[int, int]: Una tupla con (pos_min, pos_max).
        """
        return self.pos_min, self.pos_max


class MoveOption(StrEnum):
    UP = "1"
    DOWN = "2"
    RIGHT = "3"
    LEFT = "4"
    EXIT = "5"


class View:
    """Maneja toda la interacción con el usuario (entradas y salidas por consola)."""

    def display_msg(self, msg: str):
        """
        Muestra un mensaje estándar en la consola.

        Args:
            msg (str): El mensaje a mostrar.
        """
        print(msg)

    def display_err(self, err):
        """
        Muestra un mensaje de error formateado.

        Args:
            err (str): El texto del error.
        """
        print(f"\nERROR: {err}")

    def get_user_input(self, prompt: str) -> str:
        """
        Solicita información al usuario.

        Args:
            prompt (str): El texto que se mostrará para pedir el dato.

        Returns:
            str: Lo que el usuario escribe en la consola.
        """
        return input(prompt)


class Game:
    """Controla la lógica principal del juego, el estado y las reglas."""

    def __init__(self, maze: Maze, view: View):
        """
        Inicializa el juego.

        Args:
            maze (Maze): Objeto con la configuración del tablero.
            view (View): Objeto para manejar la interfaz de usuario.
        """

        self.maze = maze
        self.maze_pos_min, self.maze_pos_max = self.maze.get_limits()
        self.view = view

        self.mickey = "🐭"
        self.empty = "⬜️"
        self.obstacle = "⬛️"
        self.exit = "🚪"

        self.obstacle_counter = 9
        self.move_counter = 0
        self.mickey_pos = None
        self.exit_pos = None

    def generate_maze(self):
        """
        Genera el laberinto inicial colocando a Mickey, la salida y los obstáculos.

        Asegura que la salida no se superpone con Mickey y que los obstáculos
        no se superponen con nada existente.
        """

        self.view.display_msg("\nComienza el juego:")
        self.view.display_msg("- Generando un nuevo mapa aleatorio ...\n")

        self.maze.maze = [["⬜️"] * self.maze.cols for _ in range(self.maze.rows)]

        mickey_row = randint(self.maze_pos_min, self.maze_pos_max)
        mickey_col = randint(self.maze_pos_min, self.maze_pos_max)
        self.maze.maze[mickey_row][mickey_col] = self.mickey
        self.mickey_pos = [mickey_row, mickey_col]

        while True:
            exit_row = randint(self.maze_pos_min, self.maze_pos_max)
            exit_col = randint(self.maze_pos_min, self.maze_pos_max)
            if self.maze.maze[exit_row][exit_col] == self.mickey:
                continue
            else:
                self.maze.maze[exit_row][exit_col] = self.exit
                self.exit_pos = [exit_row, exit_col]
                break

        counter = 0
        while counter < self.obstacle_counter:
            row = randint(self.maze_pos_min, self.maze_pos_max)
            col = randint(self.maze_pos_min, self.maze_pos_max)

            if (
                self.maze.maze[row][col] == self.obstacle
                or self.maze.maze[row][col] == self.exit
                or self.maze.maze[row][col] == self.mickey
            ):
                continue
            else:
                self.maze.maze[row][col] = self.obstacle
                counter += 1

        self._print_maze()

    def get_next_move(self) -> MoveOption:
        """
        Solicita al usuario el siguiente movimiento y lo valida.

        Maneja errores de entrada si el usuario introduce una opción que no existe.

        Returns:
            MoveOption: La opción seleccionada por el usuario (UP, DOWN, etc.).
        """

        while True:
            try:
                move = MoveOption(
                    self.view.get_user_input(
                        "\nSelecciona el siguiente movimiento de Mickey:\n"
                        "1. Arriba\n"
                        "2. Abajo\n"
                        "3. Derecha\n"
                        "4. Izquierda\n"
                        "5. Finalizar el juego.\n"
                        "\n-> Escribe tu opcion: "
                    )
                )

                match move:
                    case MoveOption.UP:
                        return MoveOption.UP
                    case MoveOption.DOWN:
                        return MoveOption.DOWN
                    case MoveOption.RIGHT:
                        return MoveOption.RIGHT
                    case MoveOption.LEFT:
                        return MoveOption.LEFT
                    case MoveOption.EXIT:
                        return MoveOption.EXIT

            except ValueError:
                self.view.display_err("\nMovimiento no válido")

    def update_maze(self, next_move: MoveOption):
        """
        Coordina la ejecución del movimiento seleccionado.

        Args:
            next_move (MoveOption): La dirección hacia la que mover a Mickey.
        """

        match next_move:
            case MoveOption.UP:
                self._make_move(move_row=-1)
                self._print_maze()
                return

            case MoveOption.DOWN:
                self._make_move(move_row=1)
                self._print_maze()
                return

            case MoveOption.RIGHT:
                self._make_move(move_col=1)
                self._print_maze()
                return

            case MoveOption.LEFT:
                self._make_move(move_col=-1)
                self._print_maze()
                return

    def finish_game(self) -> bool:
        """
        Comprueba si Mickey ha llegado a la salida.

        Returns:
            bool: True si la posición de Mickey coincide con la salida, False en caso contrario.
        """

        if self.exit_pos[0] == self.mickey_pos[0] and self.exit_pos[1] == self.mickey_pos[1]:
            self.view.display_msg("\nENHORABUENA, MICKEY ENCONTRO LA SALIDA.")
            self.view.display_msg(f"- Tardaste {self.move_counter} movimientos en resolverlo.\n")
            return True
        else:
            return False

    def _make_move(self, move_row=0, move_col=0):
        """
        Realiza el cálculo interno del movimiento y actualiza la matriz.

        Verifica si el movimiento es válido (dentro de límites y sin obstáculos).
        Si es válido, actualiza la posición de Mickey y la matriz visual.

        Args:
            move_row (int): Desplazamiento en filas (-1, 0, 1).
            move_col (int): Desplazamiento en columnas (-1, 0, 1).
        """

        if (
            (self.mickey_pos[0] == self.maze_pos_min and move_row == -1)
            or (self.mickey_pos[0] == self.maze_pos_max and move_row == 1)
            or (self.mickey_pos[1] == self.maze_pos_min and move_col == -1)
            or (self.mickey_pos[1] == self.maze_pos_max and move_col == 1)
        ):
            self.view.display_err("Movimiento fuera de limites.\n")
            return

        elif (
            self.maze.maze[self.mickey_pos[0] + move_row][self.mickey_pos[1] + move_col]
            == self.obstacle
        ):
            self.view.display_err("Hay un obstaculo.\n")
            return

        else:
            self.maze.maze[self.mickey_pos[0]][self.mickey_pos[1]] = self.empty
            self.maze.maze[self.mickey_pos[0] + move_row][self.mickey_pos[1] + move_col] = (
                self.mickey
            )
            self.mickey_pos[0] = self.mickey_pos[0] + move_row
            self.mickey_pos[1] = self.mickey_pos[1] + move_col

            self.move_counter += 1
            return

    def _print_maze(self):
        """Imprime el estado actual del laberinto en la consola."""

        for i in range(len(self.maze.maze)):
            print(self.maze.maze[i])


def main():
    view = View()
    maze = Maze()
    game = Game(maze, view)

    view.display_msg("\nBIENVENIDO A EL JUEGO DEL LABERINTO.")

    game.generate_maze()
    print(f"\nMickey POS: {game.mickey_pos}")
    print(f"EXIT POS: {game.exit_pos}")

    finish = False
    while not finish:
        next_move = game.get_next_move()
        view.display_msg(f"\nElegiste: {next_move.name}\n")

        if next_move == MoveOption.EXIT:
            view.display_msg("\nSaliendo del juego ...\n")
            break

        game.update_maze(next_move)
        finish = game.finish_game()


if __name__ == "__main__":
    main()
