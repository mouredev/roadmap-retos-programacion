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
import random
import os

class ChristmastTree:
    def __init__(self, size: int) -> None:
        self.size = size
        self.branches = ["*"] * (size**2)
        self.available_branches = (size ** 2) -1
        self.trunk = " " * ((((size * 2) - 1) - 3) // 2) + "|||" + " " * ((((size * 2) - 1) - 3) // 2) + "\n"
        self.star = False
        self.balls = []
        self.lights = []
        self.turned_on = False

class TreeRender:
    def __init__(self, tree: ChristmastTree) -> None:
        self.tree = tree

    def display_tree(self):
        for row in range(1, self.tree.size + 1):
            row_start = 0
            if row != 1:
                row_start = (row-1) **2
            actual_branch = self.tree.branches[row_start: (row ** 2)]
            actual_branch = "".join(actual_branch)
            print(actual_branch.center((self.tree.size * 2)-1))
        print(self.tree.trunk * 2)

class TreeDecorator:
    def __init__(self, tree: ChristmastTree) -> None:
        self.tree = tree

    def toggle_star(self):
        if self.tree.star:
            self.tree.branches[0] = "*"
            self.tree.star = False
        else:
            self.tree.branches[0] = "@"
            self.tree.star = True

    def add_balls(self):
        if self.tree.available_branches >= 1:
            exclude = self.tree.balls + self.tree.lights
            free_branches = [b for b in range(1, self.tree.size ** 2) if b not in exclude]
            new_balls = random.sample(free_branches, min(2,self.tree.available_branches))
            for ball in new_balls:
                self.tree.branches[ball] = "o"
                self.tree.balls.append(ball)
            self.tree.available_branches -= len(new_balls)
        else:
            print("No hay suficiente espacio para más bolas")

    def delete_balls(self):
        if self.tree.balls:
            old_balls = random.sample(self.tree.balls, min(2,len(self.tree.balls)))
            for ball in old_balls:
                self.tree.branches[ball] = "*"
                self.tree.balls.remove(ball)
            self.tree.available_branches += len(old_balls)

        else:
            print("No hay bolas en el árbol.")

    def add_lights(self):
        if self.tree.available_branches >= 1:
            exclude = self.tree.balls + self.tree.lights
            free_branches = [b for b in range(1, self.tree.size ** 2) if b not in exclude]
            new_lights = random.sample(free_branches, min(3,self.tree.available_branches))
            for light in new_lights:
                if self.tree.turned_on:
                    self.tree.branches[light] = "+"
                self.tree.lights.append(light)
            self.tree.available_branches -= len(new_lights)
        else:
            print("No hay suficiente espacio para más luces.")

    def delete_lights(self):
        if self.tree.lights:
            old_lights = random.sample(self.tree.lights, min(3,len(self.tree.lights)))
            for light in old_lights:
                if self.tree.turned_on:
                    self.tree.branches[light] = "*"
                self.tree.lights.remove(light)
            self.tree.available_branches += len(old_lights)

        else:
            print("No hay luces en el árbol.")

    def toggle_lights(self):
        if self.tree.lights:
            if self.tree.turned_on:
                for light in self.tree.lights:
                    self.tree.branches[light] = "*"
                    self.tree.turned_on = False
            else:
                for light in self.tree.lights:
                    self.tree.branches[light] = "+"
                    self.tree.turned_on = True
        else:
            print("No hay luces en el árbol")

class TreeController:
    def __init__(self, tree: ChristmastTree, tree_decorator: TreeDecorator, tree_render: TreeRender) -> None:
        self.tree = tree
        self.tree_decorator = tree_decorator
        self.tree_render = tree_render

    def run(self):

        while True:
            
            print("\n--- Menú ---")
            print("1. Poner/quitar estrella")
            print("2. Añadir bolas")
            print("3. Quitar bolas")
            print("4. Añadir luces")
            print("5. Quitar luces")
            print("6. Encender/apagar luces")
            print("0. Salir")

            self.tree_render.display_tree()
            choice = "a"
            while not choice.isdigit() or int(choice) not in range(0,7):
                choice = input("Elige una opción correcta: ")
            clear_console()
            match choice:
                case "1":
                    self.tree_decorator.toggle_star()
                case "2":
                    self.tree_decorator.add_balls()
                case "3":
                    self.tree_decorator.delete_balls()
                case "4":
                    self.tree_decorator.add_lights()
                case "5":
                    self.tree_decorator.delete_lights()
                case "6":
                    self.tree_decorator.toggle_lights()
                case "0":
                    break

def clear_console():
    """
    Limpia la consola, tneiendo en cuenta el sistema operativo.
    """
    os.system('cls' if os.name =='nt' else 'clear')


tree_size = "a"
while not tree_size.isdigit():
    tree_size = input("Introduce el tamaño del árbol: ")
my_chrismast_tree = ChristmastTree(int(tree_size))
tree_decorator = TreeDecorator(my_chrismast_tree)
tree_render = TreeRender(my_chrismast_tree)
tree_controller = TreeController(my_chrismast_tree, tree_decorator, tree_render)

tree_controller.run()
