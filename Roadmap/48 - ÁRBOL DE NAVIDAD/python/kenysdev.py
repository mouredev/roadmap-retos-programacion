# _____________________________________
# https://github.com/kenysdev
# 2024 - Python
# _____________________________________
# #48 ÁRBOL DE NAVIDAD
# ------------------------------------

"""
* EJERCICIO:
 * ¡Ha comenzado diciembre! Es hora de montar nuestro
 * árbol de Navidad...
 * 
 * Desarrolla un programa que cree un árbol de Navidad
 * con una altura dinámica definida por el usuario por terminal.
 * 
 * Ejemplo de árbol de altura 5 (el tronco siempre será igual):
 * 
 *     *
 *    ***
 *   *****
 *  *******
 * *********
 *    |||
 *    |||
 *
 * El usuario podrá seleccionar las siguientes acciones:
 * 
 * - Añadir o eliminar la estrella en la copa del árbol (@)
 * - Añadir o eliminar bolas de dos en dos (o) aleatoriamente
 * - Añadir o eliminar luces de tres en tres (+) aleatoriamente
 * - Apagar (*) o encender (+) las luces (conservando su posición)
 * - Una luz y una bola no pueden estar en el mismo sitio
 *
 * Sólo puedes añadir una estrella, y tantas luces o bolas
 * como tengan cabida en el árbol. El programa debe notificar
 * cada una de las acciones (o por el contrario, cuando no
 * se pueda realizar alguna).
 """

# ____________________________________________________________________________
import random
import time
import os

class ChristmasTree:
    def __init__(self, size) -> None:
        self.__size: int = size
        self.__mtx = [[" " for _ in range(size * 2 - 1)] for _ in range(size)]
        self.__star: tuple = (0, size -1)
        self.__tree_top: list = []
        self.__balls: list = []
        self.__lights: list = []

    def print_tree(self) -> None:
        print()
        for row in self.__mtx:
            print("".join(row))

        spaces = (size * 2 - 4) // 2
        print(" " * spaces + "|||")
        print(" " * spaces + "|||")

    def create_tree(self) -> None:
        center = self.__size - 1
        for i in range(self.__size):
            ast = "*" * (i * 2 + 1)
            for j in range(len(ast)):
                col = center - i + j
                self.__mtx[i][col] = ast[j]
                self.__tree_top.append((i, col))

        self.__tree_top.pop(0)

    def add_remove_star(self) -> None:
        r, c = self.__star
        if self.__mtx[r][c] == "*":
            self.__mtx[r][c] = "@"
            return
        
        self.__mtx[r][c] = "*"

    def add_balls(self) -> None:
        if len(self.__tree_top) < 2:
            print("Ya no hay espacio para poner bolas.")
            return

        random_locations = random.sample(self.__tree_top, 2)
        for e in random_locations:
            self.__balls.append(e)
            self.__tree_top.remove(e)
            self.__mtx[e[0]][e[1]] = "o"

    def remove_balls(self) -> None:
        if not self.__balls:
            print("No hay bolas que eliminar.")
            return
            
        random_locations = random.sample(self.__balls, 2)
        for e in random_locations:
            self.__balls.remove(e)
            self.__tree_top.append(e)
            self.__mtx[e[0]][e[1]] = "*"

    def add_lights(self):
        if len(self.__tree_top) < 3:
            print("Ya no hay espacio para poner luces.")
            return

        random_locations = random.sample(self.__tree_top, 3)
        for e in random_locations:
            self.__lights.append(e)
            self.__tree_top.remove(e)
            self.__mtx[e[0]][e[1]] = "+"

    def remove_lights(self):
        if not self.__lights:
            print("Ya no hay luces que eliminar.")
            return

        random_locations = random.sample(self.__lights, 3)
        for e in random_locations:
            self.__lights.remove(e)
            self.__tree_top.append(e)
            self.__mtx[e[0]][e[1]] = "*"

    def on_off_lights(self):
        if not self.__lights:
            print("No hay luces.")
            return

        for e in self.__lights:
            if self.__mtx[e[0]][e[1]] == "*":
                self.__mtx[e[0]][e[1]] = "+"
            else:
                self.__mtx[e[0]][e[1]] = "*"

    def automatic_lights(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            for e in self.__lights:
                if self.__mtx[e[0]][e[1]] == "*":
                    self.__mtx[e[0]][e[1]] = "+"
                else:
                    self.__mtx[e[0]][e[1]] = "*"

            self.print_tree()
            time.sleep(1)

# ____________________________________________________________________________
def menu(menu: str, tree) -> None:
    while True:
        tree.print_tree()
        print(menu)
        option: str = input("Opción: ")

        match option:
            case '1': 
                tree.add_remove_star()
            case '2': 
                tree.add_balls()
            case '3': 
                tree.remove_balls()
            case '4': 
                tree.add_lights()
            case '5': 
                tree.remove_lights()
            case '6': 
                tree.on_off_lights()
            case '7':
                tree.automatic_lights( )
            case '8':
                break
            case _ : 
                print("Opción inválida.")

def get_size() -> int:
    while True:
        size: str = input("Tamaño: ")
        if size.isdigit() and int(size) % 2 != 0 and int(size) >=3:
            return int(size)

        print("Debe ser un número impar >= 3.")

MENU = """
1 - Agregar/Remover estrella.
2 - Agregar bolas.    | 3 - Quitar bolas.
4 - Agregar luces.    | 5 - Quitar luces.
6 - Encender/Apagar luces.
7 - Luces automáticas.| 8 - Salir
"""

if __name__ == "__main__":
    size: int = get_size()
    christmas_tree = ChristmasTree(size)
    christmas_tree.create_tree()
    menu(MENU, christmas_tree)
    
