# 33 - Rescatando a Mickey

import time
import os

mov_up = [-1, 0]
mov_down = [1, 0]
mov_left = [0, -1]
mov_right = [0, 1]

maze = [
    ["🚪","⬛️","⬜️","⬜️","⬜️","⬜️"],
    ["⬜️","⬛️","⬛️","⬜️","⬛️","⬜️"],
    ["⬜️","⬛️","⬛️","⬜️","⬛️","⬜️"],
    ["⬜️","⬜️","⬜️","⬜️","⬛️","⬜️"],
    ["⬛️","⬛️","⬛️","⬜️","⬛️","⬜️"],
    ["🐭","⬜️","⬜️","⬜️","⬜️","⬛️"] 
]

mickey = [5,0]

def mickey_move(mickey, move_to):
    to_go = [a + b for a,b in zip(mickey,move_to)]
    if to_go[0] < 0 or to_go[0] > 5 or to_go[1] < 0 or to_go[1] > 5:
        print("Por ese lado se encuentra una pared!")
        return mickey, False
    elif maze[to_go[0]][to_go[1]] == "⬛️":
        print("Por ese lado se encuentra una obstaculo!")
        return mickey, False
    elif maze[to_go[0]][to_go[1]] == "⬜️":
        print("Mickey se movio!")
        return to_go, False
    else:
        print("Mickey ha encontrado la salida!")
        return to_go, True

def print_maze():
    for row in maze:
        print("".join(row))

while True:
    os.system("cls")  
    print("El laberinto de Mickey")  
    print_maze()
    print("Elige el movimiento: ")
    print("W: arriba")
    print("S: abajo")
    print("A: izquierda")
    print("D: derecha")  
    move = input("Opción: ").upper()
    opcion = ["W","S","A","D"]
    if move not in opcion:
        print("Valor invalido")
        time.sleep(1)
        continue      

    match move:
        case "W":
            maze[mickey[0]][mickey[1]] = "⬜️"
            mickey, escape = mickey_move(mickey, mov_up)
            maze[mickey[0]][mickey[1]] = "🐭"

        case "S":
            maze[mickey[0]][mickey[1]] = "⬜️"
            mickey, escape = mickey_move(mickey, mov_down)
            maze[mickey[0]][mickey[1]] = "🐭"

        case "A":
            maze[mickey[0]][mickey[1]] = "⬜️"
            mickey, escape = mickey_move(mickey, mov_left)
            maze[mickey[0]][mickey[1]] = "🐭"
        case "D":
            maze[mickey[0]][mickey[1]] = "⬜️"
            mickey, escape = mickey_move(mickey, mov_right)
            maze[mickey[0]][mickey[1]] = "🐭"

    time.sleep(1)

    if escape:
        os.system("cls")
        print("Felicidades Mickey ha logrado escapar de Malefica!")
        print_maze()
        break