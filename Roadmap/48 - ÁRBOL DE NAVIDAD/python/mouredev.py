import random


class ChristmasTree:

    def __init__(self, height: int):

        self.height = height
        self.tree = [
            [" " for _ in range(2 * height - 1)]
            for _ in range(height)
        ]

        for i in range(height):
            for j in range(height - i - 1, height + i):
                self.tree[i][j] = "*"

        self.trunk = [
            [" " for _ in range(2 * height - 1)]
            for _ in range(2)
        ]

        for i in range(2):
            for j in range(height - 2, height + 1):
                self.trunk[i][j] = "|"

        self.star = False
        self.balls = []
        self.lights = []
        self.lights_on = False

    def display_tree(self):
        for index, row in enumerate(self.tree):
            if index == 0 and self.star:
                print("".join(row).replace("*", "@"))
            else:
                print("".join(row))
        for row in self.trunk:
            print("".join(row))

    def add_star(self):
        if self.star:
            print("Ya existe una estrella en el árbol.")
        else:
            self.star = True
            print("Se ha puesto la estrella en el árbol.")

    def remove_star(self):
        if not self.star:
            print("No existe una estrella en el árbol para quitar.")
        else:
            self.star = False
            print("Se ha quitado la estrella en el árbol.")

    def add_balls(self):
        available = self.available()
        if len(available) < 2:
            print("No hay suficiente espacio para añadir más bolas.")
        else:
            selected = random.sample(available, 2)
            for i, j in selected:
                self.tree[i][j] = "o"
                self.balls.append((i, j))
            print("Se han añadido 2 bolas al árbol.")

    def remove_balls(self):
        if len(self.balls) < 2:
            print("No hay suficientes bolas para quitar.")
        else:
            selected = random.sample(self.balls, 2)
            for i, j in selected:
                self.tree[i][j] = "*"
                self.balls.remove((i, j))
            print("Se han eliminado 2 bolas del árbol.")

    def add_lights(self):
        available = self.available()
        if len(available) < 3:
            print("No hay suficiente espacio para añadir más luces.")
        else:
            selected = random.sample(available, 3)
            for i, j in selected:
                self.tree[i][j] = "+" if self.lights_on else "*"
                self.lights.append((i, j))
            print("Se han añadido 3 luces al árbol.")

    def remove_lights(self):
        if len(self.lights) < 2:
            print("No hay suficientes luces para quitar.")
        else:
            selected = random.sample(self.lights, 3)
            for i, j in selected:
                self.tree[i][j] = "*"
                self.lights.remove((i, j))
            print("Se han eliminado 3 luces del árbol.")

    def toggle_lights(self, turn_on):
        if not self.lights:
            print("No hay luces en el árbol.")

        self.lights_on = turn_on
        for i, j in self.lights:
            self.tree[i][j] = "+" if turn_on else "*"
        print(f"Las luces fueron {'encendidas' if turn_on else 'apagadas'}.")

    def available(self):
        available_tree = [
            (i, j) for i in range(1, self.height) for j in range(
                self.height - i - 1, self.height + i) if self.tree[i][j] == "*"
        ]
        if not self.lights_on:
            for i, j in self.lights:
                available_tree.remove((i, j))
        return available_tree


height = input("Introduce la altura del árbol: ")

if height.isdigit() and int(height) > 0:

    tree = ChristmasTree(int(height))

    while True:

        tree.display_tree()

        print("\nAcciones:")
        print("1. Añadir estrella")
        print("2. Quitar estrella")
        print("3. Añadir bolas")
        print("4. Quitar bolas")
        print("5. Añadir luces")
        print("6. Quitar luces")
        print("7. Encender luces")
        print("8. Apagar luces")
        print("9. Salir")

        action = input("Selecciona una acción: ")

        match action:
            case "1":
                tree.add_star()
            case "2":
                tree.remove_star()
            case "3":
                tree.add_balls()
            case "4":
                tree.remove_balls()
            case "5":
                tree.add_lights()
            case "6":
                tree.remove_lights()
            case "7":
                tree.toggle_lights(True)
            case "8":
                tree.toggle_lights(False)
            case "9":
                print("¡Feliz Navidad!")
                break
            case _:
                print("Opción no válida.")

    else:
        print(f"Altura '{height}' no válida")
