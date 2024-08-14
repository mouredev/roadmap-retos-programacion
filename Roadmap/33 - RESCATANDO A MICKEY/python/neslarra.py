r"""
 EJERCICIO:
 ¡Disney ha presentado un montón de novedades en su D23!
 Pero... ¿Dónde está Mickey?
 Mickey Mouse ha quedado atrapado en un laberinto mágico
 creado por Maléfica.
 Desarrolla un programa para ayudarlo a escapar.
 Requisitos:
 1. El laberinto está formado por un cuadrado de 6x6 celdas.
 2. Los valores de las celdas serán:
    - ⬜️ Vacío
    - ⬛️ Obstáculo
    - 🐭 Mickey
    - 🚪 Salida
 Acciones:
 1. Crea una matriz que represente el laberinto (no hace falta
 que se genere de manera automática).
 2. Interactúa con el usuario por consola para preguntarle hacia
 donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
 3. Muestra la actualización del laberinto tras cada desplazamiento.
 4. Valida todos los movimientos, teniendo en cuenta los límites
 del laberinto y los obtáculos. Notifica al usuario.
 5. Finaliza el programa cuando Mickey llegue a la salida.
 """
from os import system
import keyboard as kb

maze = [['⬜', '🐭', '⬜', '⬜', '⬜', '⬜'],
        ['⬜', '⬛', '⬛', '⬛', '⬜', '⬛'],
        ['⬜', '⬜', '⬜', '⬜', '⬛', '⬜'],
        ['⬜', '⬜', '⬛', '⬜', '⬜', '⬛'],
        ['⬛', '⬜', '⬜', '⬛', '⬜', '🚪'],
        ['⬜', '⬜', '⬜', '⬛', '⬜', '⬜']]
mickey_pos = [0, 1]
exit_door = [4, 5]


def draw_maze(maze: list):
    system("cls")
    print("Press key arrow to move or Escape to quit. \n")
    for r in range(0, 6):
        for c in range(0, 6):
            print(maze[r][c], end="")
        print()


def move_up(mickey_pos: list) -> list:
    if mickey_pos[0] > 0:
        if maze[mickey_pos[0] - 1][mickey_pos[1]] in ("⬜", "🚪"):
            mickey_pos = [mickey_pos[0] - 1, mickey_pos[1]]
    return mickey_pos


def move_down(mickey_pos: list) -> list:
    if mickey_pos[0] < 5:
        if maze[mickey_pos[0] + 1][mickey_pos[1]] in ("⬜", "🚪"):
            mickey_pos = [mickey_pos[0] + 1, mickey_pos[1]]
    return mickey_pos


def move_left(mickey_pos: list) -> list:
    if mickey_pos[1] > 0:
        if maze[mickey_pos[0]][mickey_pos[1] - 1] in ("⬜", "🚪"):
            mickey_pos = [mickey_pos[0], mickey_pos[1] - 1]
    return mickey_pos


def move_right(mickey_pos: list) -> list:
    if mickey_pos[1] < 5:
        if maze[mickey_pos[0]][mickey_pos[1] + 1] in ("⬜", "🚪"):
            mickey_pos = [mickey_pos[0], mickey_pos[1] + 1]
    return mickey_pos


def move(pressed_key: str, mickey_pos: list) -> list:

    match pressed_key:
        case 'flecha abajo':
            mickey_pos = move_down(mickey_pos)
        case 'flecha izquierda':
            mickey_pos = move_left(mickey_pos)
        case 'flecha derecha':
            mickey_pos = move_right(mickey_pos)
        case 'flecha arriba':
            mickey_pos = move_up(mickey_pos)
        case 'esc':
            mickey_pos =  []
    return mickey_pos


while True:
    draw_maze(maze)
    pressed_key = kb.read_event()

    if pressed_key.event_type == "down":
        mickey_prev = mickey_pos.copy()
        mickey_pos = move(pressed_key.name, mickey_pos)
        if not mickey_pos:
            break
        maze[mickey_prev[0]][mickey_prev[1]] = "⬜"
        maze[mickey_pos[0]][mickey_pos[1]] = "🐭"
        if mickey_pos == exit_door:
            print("Mickey found the door!!! You Won!!!")
            break
