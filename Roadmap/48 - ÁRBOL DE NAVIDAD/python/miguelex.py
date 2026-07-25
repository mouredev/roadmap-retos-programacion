import random

def create_tree(height, has_star, decorations, lights_on):
    tree = []

    # Estrella opcional
    if has_star:
        tree.append(" " * (height - 1) + "@")

    # Ramas
    for i in range(1, height + 1):
        line = " " * (height - i)
        for j in range(2 * i - 1):
            if decorations.get(i, {}).get(j):
                line += decorations[i][j]
            else:
                line += "*"
        tree.append(line)

    # Tronco
    trunk_padding = " " * (height - 2)
    tree.append(trunk_padding + "|||")
    tree.append(trunk_padding + "|||")

    return tree

def display_tree(tree):
    print("\n".join(tree))

def add_random_decoration(decorations, height, deco_type, count):
    added = 0
    while added < count:
        row = random.randint(1, height)
        col = random.randint(0, 2 * row - 2)

        if row not in decorations:
            decorations[row] = {}

        if col not in decorations[row]:
            decorations[row][col] = deco_type
            added += 1

def remove_random_decoration(decorations, deco_type, count):
    removed = 0
    for row in list(decorations.keys()):
        for col in list(decorations[row].keys()):
            if decorations[row][col] == deco_type and removed < count:
                del decorations[row][col]
                removed += 1

def toggle_lights(decorations, lights_on):
    for row in decorations:
        for col in decorations[row]:
            if decorations[row][col] == "+":
                decorations[row][col] = "+" if lights_on else "*"

def main():
    height = int(input("Ingrese la altura del árbol: "))
    has_star = True
    decorations = {}
    lights_on = True

    while True:
        tree = create_tree(height, has_star, decorations, lights_on)
        display_tree(tree)

        print("\nOpciones:")
        print("1. Añadir/Eliminar estrella")
        print("2. Añadir bolas (o)")
        print("3. Eliminar bolas (o)")
        print("4. Añadir luces (+)")
        print("5. Eliminar luces (+)")
        print("6. Apagar/Encender luces")
        print("7. Salir")

        option = int(input("Seleccione una opción: "))

        if option == 1:
            has_star = not has_star
            print("Estrella añadida." if has_star else "Estrella eliminada.")
        elif option == 2:
            add_random_decoration(decorations, height, "o", 2)
            print("Bolas añadidas.")
        elif option == 3:
            remove_random_decoration(decorations, "o", 2)
            print("Bolas eliminadas.")
        elif option == 4:
            add_random_decoration(decorations, height, "+", 3)
            print("Luces añadidas.")
        elif option == 5:
            remove_random_decoration(decorations, "+", 3)
            print("Luces eliminadas.")
        elif option == 6:
            lights_on = not lights_on
            toggle_lights(decorations, lights_on)
            print("Luces encendidas." if lights_on else "Luces apagadas.")
        elif option == 7:
            print("¡Feliz Navidad!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
