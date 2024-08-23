# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# ---------------------------------------
# 32 * RESCATANDO A MICKEY
# ---------------------------------------
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
 *    - ⬜️ Vacío
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
 * del laberinto y los obtáculos. Notifica al usuario.
 * 5. Finaliza el programa cuando Mickey llegue a la salida.
"""

from typing import List, Dict, Tuple
import random

# ________________________
class Data:
    def __init__(self, config: Dict[str, str]) -> None:
        self._config = config
        self._maze: List[List[int]] = []
        self._position: Tuple[int, int] = (0, 0)
        self._exit: Tuple[int, int] = (0, 0)

    def print_maze(self) -> None:
        print("--------------------------------------")
        for row in self._maze:
            print("".join(row))
        print("--------------------------------------")

class Moves(Data):
    def __init__(self, config: Dict[str, str]) -> None:
        super().__init__(config)

    def _can_move(self, y: int, x: int) -> bool:
        size: int = len(self._maze)
        if y < 0 or x < 0 or y >= size or x >= size:
            print("🚨I can't jump over the edges.🚨")
            return False

        if self._maze[y][x] == self._config["obstacle"]:
            print("🚨You pushed me against the wall.🚨")
            return False
        
        self._position = (y, x)
        print("✅Correct move.✅")
        self._maze[y][x] = config["mouse"]
        return True

    def up(self) -> None:
        y, x = self._position
        if not self._can_move(y - 1, x): 
            return None
        self._maze[y][x] = self._config["empty"]
                
    def down(self) -> None:
        y, x = self._position       
        if not self._can_move(y + 1, x): 
            return None
        self._maze[y][x] = self._config["empty"]
    
    def right(self) -> None:
        y, x = self._position       
        if not self._can_move(y, x + 1): 
            return None
        self._maze[y][x] = self._config["empty"]

    def left(self) -> None:
        y, x = self._position       
        if not self._can_move(y, x - 1): 
            return None
        self._maze[y][x] = self._config["empty"]

# ________________________
class Maze(Moves):
    def __init__(self, config: Dict[str, str]) -> None:
        super().__init__(config)

    def _create_paths(self, x, y, width, height):
        maze: List[List[int]] = self._maze
        obstacle = self._config["obstacle"]
        empyte = self._config["empty"]

        maze[y][x] = empyte
        for dx, dy in random.sample([(0, 1), (1, 0), (0, -1), (-1, 0)], 4):
            nx, ny = x + dx * 2, y + dy * 2
            if 0 < nx < width - 1 and 0 < ny < height - 1 and maze[ny][nx] == obstacle:
                maze[y + dy][x + dx] = empyte
                self._create_paths(nx, ny, width, height)

    def create(self) -> None:
        width = self._config["size"][0]
        height = self._config["size"][1]
        obstacle = self._config["obstacle"]
        
        if not width % 2: width += 1
        if not height % 2: height += 1
        self._maze = [[obstacle] * width for _ in range(height)]

        initial_x = random.randrange(1, width - 1, 2)
        initial_y = random.randrange(1, height - 1, 2)
        self._create_paths(initial_x, initial_y, width, height)

        self._maze[0][1] = self._config["mouse"]
        self._maze[height - 1][width - 2] = self._config["exit"]
        self._position = (0, 1)
        self._exit = (height - 1, width - 2)

    def veify_win(self) -> bool:
        y, x = self._exit
        if self._maze[y][x] == self._config["mouse"]:
            return True
        return False

# ________________________
class Game:
    def __init__(self, config: Dict[str, str], instance_Maze) -> None:
        self._config: dict = config
        self._maze = instance_Maze

    def _restart_or_exit(self) -> bool:
        while True:
            option: str = (input("Y/N: ")).lower()
            match option:
                case 'y': return True
                case 'n': return False
                case _ : print("❌Invalid key.❌")

    def play(self):
        for k, v in self._config.items():
            print(f"{k}: {v}")
        
        self._maze.create()
        while True:
            self._maze.print_maze()
            print("Use the keys: (W, S, A, D).\nTo restart: R. To exit: 9.")
            option: str = (input("\nTecla: ")).lower()
            match option:
                case 'w': self._maze.up()
                case 's': self._maze.down()
                case 'd': self._maze.right()
                case 'a': self._maze.left()
                case 'r': 
                    print("😮Do you want to restart?😮")
                    if self._restart_or_exit():
                        self._maze.create()

                case '9': 
                    print("😮Do you want to exit?😮")
                    if self._restart_or_exit():
                        break

                case _ : print("❌Invalid key.❌")

            if self._maze.veify_win():
                print("🏆Congratulations, you managed to get me out.🏆")
                print("🤔Do you want to play again?🤔")
                if self._restart_or_exit():
                    self._maze.create()
                else:
                    print("Bye")
                    break

# ________________________
if __name__ == "__main__":
    # These are the default values. You can change them here.
    config: Dict[str, str] = {
        "title": "RESCUING MICKEY",
        "size": (6, 6),
        "empty": "⬜️",
        "obstacle": "⬛️",
        "mouse": "🐭",
        "exit": "🚪"
    }

    _maze = Maze(config)
    _game = Game(config, _maze)
    _game.play()

