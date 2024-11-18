import os, platform

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" * EJERCICIO:
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
 * del laberinto y los obstáculos. Notifica al usuario.
 * 5. Finaliza el programa cuando Mickey llegue a la salida."""


labyrinth =[["🐭","⬛️","⬛️","⬜️","⬜️","⬜️"],
            ["⬜️","⬜️","⬛️","⬜️","⬛️","⬜️"],
            ["⬛️","⬜️","⬛️","⬜️","⬜️","⬜️"],
            ["⬛️","⬜️","⬛️","⬜️","⬜️","⬛️"],
            ["⬜️","⬜️","⬛️","⬜️","⬜️","🚪"],
            ["⬜️","⬜️","⬜️","⬜️","⬛️","⬜️"]]

def show_labyrinth(labyrinth):
    for rows in labyrinth:
        print()
        for columns in rows:
            print(columns, end='') 
    print()

def movements(next_row, next_column, mickey_position):
    if next_column > 5 or next_column < 0 or next_row < 0 or next_row > 5 or labyrinth[next_row][next_column] == '⬛️':
        print("No se puede seguir en esa dirección, pruebe de nuevo")
        next_row, next_column = row, column
        show_labyrinth(labyrinth)

    elif labyrinth[next_row][next_column] == '🚪':
        print("¡¡Has encontrado la salida del laberinto!!")
        labyrinth[row][column] = '⬜️'
        labyrinth[next_row][next_column] = '🐭'
        mickey_position = [-1, -1]
        show_labyrinth(labyrinth)
        
    else:
        labyrinth[row][column] = '⬜️'
        labyrinth[next_row][next_column] = '🐭'
        mickey_position = [next_row, next_column]
        show_labyrinth(labyrinth)
    return mickey_position 

mickey_position = [0,0]

show_labyrinth(labyrinth)

while mickey_position != [-1, -1]:
    row, column = mickey_position

    next_row, next_column = row, column

    movement = input("""\n\nElija un movimiento para guiar a Mickey por el laberinto:
              n - Subir
              s - Bajar
              w - Izquierda
              e - Derecha
              ---> """).lower()    
              
    if movement != "n" and movement != "s" and movement != "w" and movement != "e":
        print("comando no válido, pruebe de nuevo")
        show_labyrinth(labyrinth)
        continue

    else:
        if movement == "n":
            next_row = row - 1
            
        elif movement == "s":
            next_row = row + 1
           
        elif movement == "w":
            next_column = column - 1
            
        elif movement == "e":
            next_column = column + 1
           
    mickey_position = movements(next_row, next_column, mickey_position)
    
    



