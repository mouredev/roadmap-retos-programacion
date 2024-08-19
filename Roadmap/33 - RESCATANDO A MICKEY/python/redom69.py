"""
/*
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
 * del laberinto y los obtáculos. Notifica al usuario.
 * 5. Finaliza el programa cuando Mickey llegue a la salida.
 */
"""

import random


# Constantes
VACIO = "⬜️"
OBSTACULO = "⬛️"
MICKEY = "🐭"
SALIDA = "🚪"

def generateMaze(width, height, total=10):

    maze = [[VACIO for _ in range(width)] for _ in range(height)]

    
    mickeyPos = (random.randint(0, height - 1), random.randint(0, width - 1))
    maze[mickeyPos[0]][mickeyPos[1]] = MICKEY

    while True:
        end = (random.randint(0, height - 1), random.randint(0, width - 1))
        if end != mickeyPos:
            maze[end[0]][end[1]] = SALIDA
            break
    
    obstacles = 0
    while obstacles < total:
        obstacles_pos = (random.randint(0, height - 1), random.randint(0, width - 1))
        if maze[obstacles_pos[0]][obstacles_pos[1]] == VACIO:
            maze[obstacles_pos[0]][obstacles_pos[1]] = OBSTACULO
            obstacles += 1
    
    return maze, mickeyPos, end

def showMaze(maze):
    for row in maze:
        print("".join(row))

def isValid(newMove,maze):
    x,y = newMove
    if -7 <= x <= 7 and -7 <= y <= 7:
        if maze[x][y] != OBSTACULO:
            return True
    return False 

def moveMickey(maze,mickeyPos,move):
    x,y = mickeyPos

    if move == 'w' :
        newMove= (x-1,y)
    elif  move == 's':
        newMove = (x+1,y)
    elif move == 'a':
        newMove = (x,y-1)
    elif  move == 'd':
        newMove = (x,y+1)
    else:
        newMove = mickeyPos

    if isValid(newMove,maze):
        maze[x][y] = VACIO
        mickeyPos = newMove
        maze[newMove[0]][newMove[1]]= MICKEY

    return  mickeyPos



def main():
    width = 6
    height = 6
    maze, mickeyPos, end = generateMaze(width, height)

    while True:
        showMaze(maze)
        move = input("Mueve a Mickey (w/a/s/d): ")
        mickeyPos = moveMickey(maze,mickeyPos,move)    

        if mickeyPos == end :
            print("¡Mickey ha llegado a la salida!",MICKEY)
            break



if __name__ == "__main__":
    main()