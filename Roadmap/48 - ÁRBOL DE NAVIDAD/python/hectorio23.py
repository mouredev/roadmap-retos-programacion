# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

import random

def draw_tree(tree):
    for line in tree:
        print(line)
    print()

def initialize_tree(height, has_star):
    tree = []

    if has_star:
        tree.append(" " * height + "@")

    for i in range(height):
        width = 2 * i + 1
        row = " " * (height - i - 1) + "*" * width
        tree.append(row)

    trunk = " " * (height - 1) + "|||"
    tree.append(trunk)
    tree.append(trunk)

    return tree

def toggle_star(tree, height, has_star):
    has_star = not has_star
    tree = initialize_tree(height, has_star)
    print("Estrella", "añadida." if has_star else "eliminada.")
    return tree, has_star

def add_or_remove(tree, height, symbol, count, add):
    modifications = 0

    for i in range(1, height + 1):
        row = list(tree[i])
        for j in range(len(row)):
            if (add and row[j] == '*' and random.choice([True, False])) or (not add and row[j] == symbol):
                row[j] = symbol if add else '*'
                modifications += 1
            if modifications == count:
                break
        tree[i] = "".join(row)
        if modifications == count:
            break

    print(f"{'Añadido' if add else 'Eliminado'} {modifications} de {symbol}.")
    return tree

def toggle_lights(tree, height, lights_on):
    lights_on = not lights_on

    for i in range(1, height + 1):
        row = list(tree[i])
        for j in range(len(row)):
            if row[j] in ('*', '+'):
                row[j] = '+' if lights_on else '*'
        tree[i] = "".join(row)

    print("Luces", "encendidas." if lights_on else "apagadas.")
    return tree, lights_on

def main():
    height = int(input("Ingresa la altura del árbol: "))

    has_star = True
    lights_on = False

    tree = initialize_tree(height, has_star)

    while True:
        draw_tree(tree)
        option = input("Opciones: [estrella, bolas, luces, apagar, salir]: ").strip().lower()

        if option == "estrella":
            tree, has_star = toggle_star(tree, height, has_star)
        elif option == "bolas":
            tree = add_or_remove(tree, height, 'o', 2, True)
        elif option == "luces":
            tree = add_or_remove(tree, height, '+', 3, True)
        elif option == "apagar":
            tree, lights_on = toggle_lights(tree, height, lights_on)
        elif option == "salir":
            print("Gracias por decorar el árbol!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
