maze = [
    ["🐭", "◼️", "◼️", "◼️", "◼️", "◼️"],
    ["◽", "◼️", "◼️", "◼️", "◼️", "◼️"],
    ["◽", "◼️", "◼️", "◼️", "◽", "◼️"],
    ["◽", "◽", "◽", "◽", "◽", "◽"],
    ["◼️", "◽", "◼️", "◽", "◼️", "◼️"],
    ["◼️", "◽", "◼️", "◽", "◽", "◽"],
    ["◽", "◽", "◼️", "◼️", "◼️", "📤"]
]


def print_maze():
    for row in maze:
        print("".join(row))


micky_position = [0, 0]  # Posición inicial de Mickey Mouse
print("Bienvenido a la aventura de Mickey Mouse!")
print("Mickey Mouse se encuentra atrapado en un laberinto y necesita tu ayuda para escapar.")
print("El laberinto es el siguiente:")
print_maze()

# Preguntar al usuario si quiere jugar
play = input(
    "¿Quieres ayudar a Mickey Mouse a escapar del laberinto? (s/n): ").lower()
if play != "s":
    print("¡Hasta luego!")
    exit()

while True:
    # Preguntar al usuario por la dirección
    direction = input(
        "¿En qué dirección quieres mover a Mickey Mouse? \n[u] arriba \n[d] abajo \n[l] izquierda \n[r] derecha \n: ").lower()

    current_row, current_col = micky_position
    new_row, new_col = current_row, current_col
    # Mover a Mickey Mouse en la dirección elegida

    match direction:
        case "u":
            # Código para mover hacia arriba
            new_row = current_row - 1
        case "d":
            # Código para mover hacia abajo
            new_row = current_row + 1
        case "l":
            # Código para mover hacia la izquierda
            new_col = current_col - 1
        case "r":
            # Código para mover hacia la derecha
            new_col = current_col + 1
        case _:
            print("Dirección no válida. Intenta de nuevo.")
            continue
    # Verificar límites del laberinto
    if not (0 <= new_row < len(maze) and 0 <= new_col < len(maze[0])):
        print("¡No puedes salir del laberinto! Intenta de nuevo.")
        continue
    # Verificar si la nueva posición es un muro
    else:
        if maze[new_row][new_col] == "◼️":
            print("¡Has chocado con un muro! Intenta de nuevo.")
            continue
        # Verificar si la nueva posición es la salida
        elif maze[new_row][new_col] == "📤":
            print("¡Felicidades! Mickey Mouse ha encontrado la salida del laberinto.")
            break
        # Actualizar la posición de Mickey Mouse en el laberinto
        else:
            maze[current_row][current_col] = "◽"
            maze[new_row][new_col] = "🐭"
            micky_position = [new_row, new_col]
            print(
                f"Mickey Mouse se ha movido a la posición ({new_row}, {new_col})")
            print("El laberinto actualizado es el siguiente:")
            print_maze()
