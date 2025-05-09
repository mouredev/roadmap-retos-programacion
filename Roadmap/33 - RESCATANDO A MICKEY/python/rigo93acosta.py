'''
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
'''

maze = [
    ['🐭', '⬛️', '⬜️', '⬜️', '⬜️', '⬜️'],
    ['⬜️', '⬜️', '⬜️', '⬛️', '⬜️', '⬛️'],
    ['⬜️', '⬜️', '⬜️', '⬜️', '⬛️', '⬜️'],
    ['⬛️', '⬜️', '⬛️', '⬜️', '⬛️', '⬜️'],
    ['⬛️', '⬜️', '⬛️', '⬜️', '⬜️', '⬜️'],
    ['⬛️', '⬜️', '⬜️', '⬛️', '⬛️', '🚪']
]


mickey = [0, 0]
door_out = lambda x, y: maze[x][y] == '🚪'

def chart_end():
    print(f"{45*'*'}")
    print("¡Felicidades! Mickey ha salido del laberinto")
    print(f"{45*'*'}")

def maze_print(maze):
    for row in maze:
        for cell in row:
            print(str(cell).ljust(1), end="")
        print()

maze_print(maze)

while True:
    print("\nHacia donde se tiene que desplazar Mickey?")
    print("[w] Arriba")
    print("[s] Abajo")
    print("[a] Izquierda")
    print("[d] Derecha")
    direction = input("Dirección: ")
    
    current_row, current_col = mickey
    new_row, new_col = current_row, current_col

    match direction:
        
        case "w":
            new_row -= 1

        case "s":
            new_row += 1
        case "a":
            new_col -= 1
        case "d":
            new_col += 1
        case _:
            print("Dirección no válida")
            continue
    
    if new_row < 0 or new_row >= len(maze) or new_col < 0 or new_col >= len(maze):
        print("Desplezamiento fuera del laberinto.")
        print("Movimiento no válido.")
        continue
    else:
        if maze[new_row][new_col] == '⬛️':
            print("Hay un obstáculo.")
            print("Movimiento no válido.")
            continue
        elif door_out(new_row, new_col):
            maze[current_row][current_col] = '⬜️'
            maze[new_row][new_col] = '🐭'
            mickey = [new_row, new_col]
            maze_print(maze)
            chart_end()
            break
        else:
            maze[current_row][current_col] = '⬜️'
            maze[new_row][new_col] = '🐭'
            mickey = [new_row, new_col]
            maze_print(maze)
    
