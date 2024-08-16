####################################
# Author: Luis Rodriguez
# GitHub: https://github/lurtur
# Date: 15 August 2024
####################################

# /*
#  * EJERCICIO:
#  * ¡Disney ha presentado un montón de novedades en su D23! 
#  * Pero... ¿Dónde está Mickey?
#  * Mickey Mouse ha quedado atrapado en un laberinto mágico 
#  * creado por Maléfica.
#  * Desarrolla un programa para ayudarlo a escapar.
#  * Requisitos:
#  * 1. El laberinto está formado por un cuadrado de 6x6 celdas.
#  * 2. Los valores de las celdas serán:
#  *    - ⬜️ Vacío
#  *    - ⬛️ Obstáculo
#  *    - 🐭 Mickey
#  *    - 🚪 Salida
#  * Acciones:
#  * 1. Crea una matriz que represente el laberinto (no hace falta
#  * que se genere de manera automática).
#  * 2. Interactúa con el usuario por consola para preguntarle hacia
#  * donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
#  * 3. Muestra la actualización del laberinto tras cada desplazamiento.
#  * 4. Valida todos los movimientos, teniendo en cuenta los límites
#  * del laberinto y los obtáculos. Notifica al usuario.
#  * 5. Finaliza el programa cuando Mickey llegue a la salida.
#  */

import os

os.system('clear')

board = [ 
    ['M', 'V', 'V', 'O', 'O', 'O'], 
    ['O', 'O', 'V', 'V', 'V', 'V'], 
    ['O', 'O', 'O', 'O', 'O', 'V'], 
    ['V', 'V', 'V', 'V', 'V', 'V'], 
    ['V', 'O', 'O', 'O', 'O', 'O'], 
    ['V', 'V', 'V', 'V', 'V', 'S'], 
    ]

UP = '0'
RIGHT = '1'
DOWN = '2'
LEFT = '3'

def display_board():
    board_str = ""
    for row in board:
        board_str += ' '.join(row)
        board_str += '\n'
    print()
    print(board_str)

def find_mickey(board: list):
    coords = tuple()
    for row, row_data in enumerate(board):
        for col, col_data in enumerate(row_data):
            if col_data == "M":
                coords = (row, col)
                break

    return coords

def move_up():
    coord = find_mickey(board)
    row = coord[0]
    col = coord[1]
    
    board[row-1][col], board[row][col]  = board[row][col], board[row-1][col]

def move_down():
    coord = find_mickey(board)
    row = coord[0]
    col = coord[1]
    
    board[row][col], board[row + 1][col]  = board[row + 1][col], board[row][col]
 
def move_right():
    coord = find_mickey(board)
    row = coord[0]
    col = coord[1]
    
    board[row][col], board[row][col+1] = board[row][col+1], board[row][col]

def move_left():
    coord = find_mickey(board)
    row = coord[0]
    col = coord[1]
    
    board[row][col-1], board[row][col]  = board[row][col], board[row][col-1]

def commands_menu():
    print("Commands menu:")
    print("UP: 0")
    print("RIGHT: 1")
    print("DOWN: 2")
    print("LEFT: 3")
    option = input("Select the direction you want Mickey to move: ")

    if option == UP:
        move_up()
    elif option == RIGHT:
        move_right()
    elif option == DOWN:
        move_down()
    elif option == LEFT:
        move_left()
    

def main():
    while True:
        display_board()
        commands_menu()

main()