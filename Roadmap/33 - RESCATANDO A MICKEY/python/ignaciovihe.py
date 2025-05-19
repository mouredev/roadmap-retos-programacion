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
 * del laberinto y los obstáculos. Notifica al usuario.
 * 5. Finaliza el programa cuando Mickey llegue a la salida.
"""


"""
He querido realizar el ejercicio con clases para practicar SOLID. Se podía haber resuelto de forma mucho mas sencilla.
"""

import os
from abc import ABC, abstractmethod

def clear_console():# Sierve para borrar la consola y que el tablero quede siempre en el mismo sitio
    os.system('cls' if os.name == 'nt' else 'clear')


maze = [["⬜️","⬛️","🚪","⬜️","⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬛️"],
        ["⬜️","⬛️","⬛️","⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️"],
        ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬛️","⬜️","⬜️","⬛️"],
        ["⬜️","⬜️","⬛️","⬜️","⬛️","⬛️","⬜️","⬛️","⬜️","⬛️","⬛️","⬜️"],
        ["⬜️","⬛️","⬜️","⬜️","⬛️","⬛️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️"],
        ["⬜️","⬛️","⬛️","⬛️","⬛️","⬜️","⬜️","⬜️","⬛️","⬜️","⬜️","⬜️"],
        ["⬜️","⬛️","⬜️","⬛️","⬜️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬜️"],
        ["⬜️","⬛️","⬜️","⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
        ["⬜️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬜️","⬛️","⬛️","⬜️","⬜️"],
        ["⬜️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬜️","⬜️","⬜️","⬛️","⬜️"],
        ["⬜️","⬛️","⬜️","⬛️","⬜️","⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️"],
        ["⬛️","🐭","⬜️","⬛️","⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️"],
        ["⬜️","⬛️","⬜️","⬛️","⬜️","⬜️","⬛️","⬛️","⬛️","⬛️","⬜️","⬜️"],
        ["⬜️","⬛️","⬜️","⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️"]]

class Maze:#Clase que contiene el laberinto y sus proiedades.
    def __init__(self, grid):
        self.grid = grid
        self.obstacles, self.mickey, self.exit = self.update_maze_properties()

    def __getitem__(self, index):# Este metodo hace que cuando accedo a la instacia de Maze con indices no tengo que acceder a maze.grid
        return self.grid[index]
    
    def __len__(self):
        return len(self.grid)# Igualmente dice que cuando acceda a len de la instancia de Maze este accediendo directamente a len de maze.grid

    def update_maze_properties(self):
        current_obstacles = []
        mickey = exit = None #Mejora la seguridad
        for i, line in enumerate(self.grid):
            for j, column in enumerate(line):
                if column != "⬜️":
                    if column == "⬛️":
                        current_obstacles.append((i, j))
                    elif column == "🐭":
                        mickey = (i, j)
                    elif column == "🚪":
                        exit = (i, j)
        return current_obstacles, mickey, exit


class MazePrinter:#Esta clase sieve para pintar el laberinto
    def __init__(self, maze: Maze):
        self.maze = maze

    def print_maze(self):
        for line in self.maze:
            for cell in line:
                print(cell, end="")
            print()


class CellChecker:# Esta clase se encarga de comprobar las situaciones en el tablero
    def __init__(self, maze: Maze):
        self.maze = maze

    def is_inside_maze(self, i:int, j:int):
        return 0<= i < len(self.maze)  and   0<= j < len(self.maze[0]) # Puedo acceder directamente a self.maze como si fuera grid por la funcion __getitem__

    def is_obstacle(self, i:int, j:int):
        return (i, j) in self.maze.obstacles

    def is_exit(self, i:int, j: int):
        return (i, j) in self.maze.exit

    def is_mickey(self, i:int, j: int):
        return (i, j) in self.maze.mickey
    

class GameMessenger:# Esta clase se encarga de imprimir los mensajes de feedback
    def invalid_direction(self):
        print("Elige una opción válida")

    def mickey_blocked(self):
        print("Mickey no puede continuar por ahí")

    def mickey_wins(self):
        print("FELICIDADES! - HAS LIBERADO A MICKEY")
    

class MoveStrategy(ABC):# Interfaz/Clase abstracta de los posibles movimientos.
    @abstractmethod
    def matches(self, direction: str) -> bool:
        pass
    @abstractmethod
    def get_movement(self) -> tuple[int, int]:
        pass

class MoveLeft(MoveStrategy):#Implementaciones concretas de los posibles movimientos
    def matches(self, direction): return direction == "a"
    def get_movement(self): return (0, -1)

class MoveUpLeft(MoveStrategy):
    def matches(self, direction): return direction == "q"
    def get_movement(self): return (-1, -1)

class MoveUp(MoveStrategy):
    def matches(self, direction): return direction == "w"
    def get_movement(self): return (-1, 0)

class MoveUpRight(MoveStrategy):
    def matches(self, direction): return direction == "e"
    def get_movement(self): return (-1, 1)

class MoveRight(MoveStrategy):
    def matches(self, direction): return direction == "d"
    def get_movement(self): return (0, 1)

class MoveDownRight(MoveStrategy):
    def matches(self, direction): return direction == "c"
    def get_movement(self): return (1, 1)

class MoveDown(MoveStrategy):
    def matches(self, direction): return direction == "s"
    def get_movement(self): return (1, 0)

class MoveDownLeft(MoveStrategy):
    def matches(self, direction): return direction == "z"
    def get_movement(self): return (1, -1)

class MovementManager:# Esta clase se encarga de manejar los posibles movimientos
    def __init__(self, maze: Maze, cell_checker: CellChecker, strategies):
        self.maze = maze
        self.cell_checker = cell_checker
        self.strategies = strategies
        
    def calculate_movement(self, direction: str):# Obtiene el movimiento segun la opcion elegida
        for strategie in self.strategies:
            if strategie.matches(direction):
                return strategie.get_movement()
        return None    
            
    def move(self, direction: str):# Realiza el movimiento y devuelve el estado de lo que ha ocurrido. Movimiento normal, bloqueado, final.
        movement = self.calculate_movement(direction)
        if movement is None:
            return "invalid"
                
        new_i = self.maze.mickey[0] + movement[0]
        new_j = self.maze.mickey[1] + movement[1]

        if self.cell_checker.is_inside_maze(new_i, new_j) and not self.cell_checker.is_obstacle(new_i, new_j):
            old_i, old_j = self.maze.mickey
            self.maze[old_i][old_j]= "⬜️"
            self.maze[new_i][new_j] = "🐭"
            self.maze.mickey = (new_i, new_j)
            
            if self.maze.mickey == self.maze.exit:
                return "win"
            return "moved"
        else:
            return "blocked"


def main():# Se encarga del flujo del programa
    my_maze = Maze(maze)
    printer = MazePrinter(my_maze)
    cell_checker = CellChecker(my_maze)
    movement_strategies = [
            MoveLeft(), MoveUpLeft(), MoveUp(), MoveUpRight(), MoveRight(), MoveDownRight(), MoveDown(), MoveDownLeft()
        ]
    movement_manager = MovementManager(my_maze, cell_checker, movement_strategies)
    messenger = GameMessenger()

    finish = False
    print("--Welcome to Mickey Maze--")
    printer.print_maze()

    while not finish:
        print("Movimientos:")
        print("a. Izquierda")
        print("q. Arriba izquierda")
        print("w. Arriba")
        print("e. Arriba derecha")
        print("d. Derecha")
        print("c. Abajo derecha")
        print("s. Abajo")
        print("z. Abajo izquierda")

        option = input("Introduce a donde quieres moverte:")
        clear_console()
        result = movement_manager.move(option)

        printer.print_maze()

        match result:
            case "invalid":
                messenger.invalid_direction()
            case "blocked":
                messenger.mickey_blocked()
            case "win":
                messenger.mickey_wins()
                finish = True

main()