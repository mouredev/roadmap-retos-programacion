from abc import ABC, abstractmethod
from typing import Tuple


class MazeInterface(ABC):
    @abstractmethod
    def get_cell(self, position: Tuple[int, int]) -> str:
        pass

    @abstractmethod
    def update_maze(self, character_position: Tuple[int, int], last_position: Tuple[int, int]):
        pass

    @abstractmethod
    def print_maze(self):
        pass


class Character:
    finish: bool
    up: str
    right: str
    left: str
    down: str
    last_position: Tuple[int, int]
    position: Tuple[int, int]
    maze: MazeInterface

    def __init__(self, maze: MazeInterface):
        self.finish = False
        self.up = '⬜'
        self.right = '⬛'
        self.left = '⬛'
        self.down = ''
        self.last_position = (0, 0)
        self.position = (5, 2)
        self.maze = maze
        self.update_character_elements()

    def move_up(self):
        match self.up:
            case '⬜':
                print("Avanza hacia arriba")
                self.last_position = self.position
                self.position = (self.position[0] - 1, self.position[1])
                self.update_character_elements()
            case '⬛':
                print("Hay un obstáculo")
            case '':
                print("Estás en el límite del mapa")
            case '🚪':
                print("Llegaste a la salida")
                self.finish = True

    def move_right(self):
        match self.right:
            case '⬜':
                print("Avanza hacia la derecha")
                self.last_position = self.position
                self.position = (self.position[0], self.position[1] + 1)
                self.update_character_elements()
            case '⬛':
                print("Hay un obstáculo")
            case '':
                print("Estás en el límite del mapa")
            case '🚪':
                print("Llegaste a la salida")
                self.finish = True

    def move_left(self):
        match self.left:
            case '⬜':
                print("Avanza hacia la izquierda")
                self.last_position = self.position
                self.position = (self.position[0], self.position[1] - 1)
                self.update_character_elements()
            case '⬛':
                print("Hay un obstáculo")
            case '':
                print("Estás en el límite del mapa")
            case '🚪':
                print("Llegaste a la salida")
                self.finish = True

    def move_down(self):
        match self.down:
            case '⬜':
                print("Avanza hacia abajo")
                self.last_position = self.position
                self.position = (self.position[0] + 1, self.position[1])
                self.update_character_elements()
            case '⬛':
                print("Hay un obstáculo")
            case '':
                print("Estás en el límite del mapa")
            case '🚪':
                print("Llegaste a la salida")
                self.finish = True

    def update_character_elements(self):
        # Positions around the character
        up = (self.position[0] - 1, self.position[1])
        down = (self.position[0] + 1, self.position[1])
        right = (self.position[0], self.position[1] + 1)
        left = (self.position[0], self.position[1] - 1)

        self.up = self.maze.get_cell(up)
        self.down = self.maze.get_cell(down)
        self.right = self.maze.get_cell(right)
        self.left = self.maze.get_cell(left)


class Maze(MazeInterface):
    maze = [['🚪', '⬜', '⬛', '⬛', '⬛', '⬛'],
            ['⬛', '⬜', '⬛', '⬛', '⬛', '⬛'],
            ['⬛', '⬜', '⬜', '⬜', '⬛', '⬛'],
            ['⬛', '⬛', '⬛', '⬜', '⬛', '⬛'],
            ['⬛', '⬛', '⬜', '⬜', '⬛', '⬛'],
            ['⬛', '⬛', '🐭', '⬛', '⬛', '⬛']]

    def get_cell(self, position: Tuple[int, int]) -> str:
        if 0 <= position[0] < len(self.maze) and 0 <= position[1] < len(self.maze[0]):
            return self.maze[position[0]][position[1]]
        return ''

    def update_maze(self, character_position: Tuple[int, int], last_position: Tuple[int, int]):
        self.maze[character_position[0]][character_position[1]] = '🐭'
        self.maze[last_position[0]][last_position[1]] = '⬜'

    def print_maze(self):
        for row in self.maze:
            actual_row = ""
            for element in row:
                actual_row += element
            print(actual_row)


def main():
    maze = Maze()
    character = Character(maze)

    while not character.finish:
        maze.print_maze()
        print("\nMovimiento de Mickey:"
              "\n- Arriba"
              "\n- Abajo"
              "\n- Derecha"
              "\n- Izquierda")
        option = input("> ").lower()
        print("")

        match option:
            case "arriba":
                character.move_up()
            case "abajo":
                character.move_down()
            case "derecha":
                character.move_right()
            case "izquierda":
                character.move_left()
            case _:
                print("⚠️Opción incorrecta")

        maze.update_maze(character.position, character.last_position)


if __name__ == '__main__':
    main()
