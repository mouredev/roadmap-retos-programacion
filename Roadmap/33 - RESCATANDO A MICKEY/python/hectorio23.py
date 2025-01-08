# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23
import subprocess

# Imprime el estado actual del laberinto
def print_labyrinth(labyrinth):
    for row in labyrinth:
        print(" ".join(row))
    print()

# Mueve a Mickey a una nueva posición y valida el movimiento
def move_mickey(labyrinth, mickey_x, mickey_y, new_x, new_y):
    # Validación de límites del laberinto
    if new_x < 0 or new_x >= 6 or new_y < 0 or new_y >= 6:
        print("Movimiento inválido, fuera de los límites del laberinto.")
        return mickey_x, mickey_y, False
    # Validación de obstáculos
    if labyrinth[new_x][new_y] == '⬛️':
        print("Movimiento inválido, obstáculo en el camino.")
        return mickey_x, mickey_y, False

    # Actualiza la posición de Mickey
    labyrinth[mickey_x][mickey_y] = '⬜️' # Limpia la posición anterior
    mickey_x, mickey_y = new_x, new_y

    # Verificación si Mickey ha llegado a la salida
    if labyrinth[mickey_x][mickey_y] == '🚪':
        print("¡Mickey ha escapado!")
        return mickey_x, mickey_y, True

    labyrinth[mickey_x][mickey_y] = '🐭' # Actualiza la posición de Mickey
    return mickey_x, mickey_y, False

# Definición inicial del laberinto
labyrinth = [
    ['⬜️', '⬜️', '⬜️', '⬛️', '⬛️', '⬛️'],
    ['⬛️', '⬛️', '⬜️', '⬛️', '🚪', '⬛️'],
    ['⬛️', '⬛️', '⬜️', '⬛️', '⬜️', '⬛️'],
    ['⬛️', '⬛️', '⬜️', '⬜️', '⬜️', '⬛️'],
    ['⬛️', '⬛️', '⬜️', '⬛️', '⬛️', '⬛️'],
    ['🐭', '⬜️', '⬜️', '⬛️', '⬛️', '⬛️']
]

# Posición inicial de Mickey
mickey_x, mickey_y = 5, 0
escaped = False

# Ciclo principal de interacción con el usuario
while not escaped:
    subprocess.call(['clear'])

    print_labyrinth(labyrinth)  # Muestra el estado actual del laberinto
    direction = input("Introduce dirección (arriba, abajo, izquierda, derecha): ")

    # Procesa la dirección ingresada y mueve a Mickey si es válido
    if direction == "arriba":
        mickey_x, mickey_y, escaped = move_mickey(labyrinth, mickey_x, mickey_y, mickey_x - 1, mickey_y)
    elif direction == "abajo":
        mickey_x, mickey_y, escaped = move_mickey(labyrinth, mickey_x, mickey_y, mickey_x + 1, mickey_y)
    elif direction == "izquierda":
        mickey_x, mickey_y, escaped = move_mickey(labyrinth, mickey_x, mickey_y, mickey_x, mickey_y - 1)
    elif direction == "derecha":
        mickey_x, mickey_y, escaped = move_mickey(labyrinth, mickey_x, mickey_y, mickey_x, mickey_y + 1)
    else:
        print("Dirección inválida. Intenta nuevamente.")
