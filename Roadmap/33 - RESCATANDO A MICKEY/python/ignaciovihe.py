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

import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


maze = [["⬜️","⬛️","🚪","⬜️","⬜️","⬜️"],
        ["⬜️","⬛️","⬛️","⬛️","⬛️","⬜️"],
        ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️"],
        ["⬜️","⬜️","⬛️","⬜️","⬛️","⬜️"],
        ["⬜️","⬛️","⬜️","⬜️","⬛️","⬜️"],
        ["⬜️","🐭","⬜️","⬛️","⬛️","⬜️"]]

class Maze:
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
    
    def print_maze(self):
        for line in self.grid:
            print(f"{line} ")

class CellChecker:
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
    
class MovementManager:
    def __init__(self, maze: Maze, cell_checker: CellChecker):
        self.maze = maze
        self.cell_checker = cell_checker

    def move(self, direction: str):
        match direction:
            case "a":
                movement = (0, -1)
            case "w":
                movement = (-1, 0)
            case "d":
                movement = (0, 1)
            case "s":
                movement = (1, 0)
            case _:
                print("Elige una opción valida")
                return False
                
        new_i, new_j = (self.maze.mickey[0] + movement[0], self.maze.mickey[1] + movement[1])
        if self.cell_checker.is_inside_maze(new_i, new_j) and not self.cell_checker.is_obstacle(new_i, new_j):
            old_i, old_j = self.maze.mickey
            self.maze[old_i][old_j]= "⬜️"
            self.maze[new_i][new_j] = "🐭"
            self.maze.mickey = (new_i, new_j)
            self.maze.print_maze()
        else:
            self.maze.print_maze()
            print("Michey no puede continuar por ahí")
        if self.maze.mickey == self.maze.exit:
            print("FELICIDADES! - HAS LIBERADO A MICKEY")
            return True
        return False


        




def main():
    my_maze = Maze(maze)
    movement_manager = MovementManager(my_maze, CellChecker(my_maze))
    finish = False
    print("--Welcome to Mickey Maze--")
    my_maze.print_maze()
    while not finish:
        print("Movimientos:")
        print("a. Izquierda")
        print("w. Arriba")
        print("d. Derecha")
        print("s. Abajo")

        option = input("Introduce a donde quieres moverte:")
        clear_console()
        finish = movement_manager.move(option)
main()