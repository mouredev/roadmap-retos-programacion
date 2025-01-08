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
tablero = [["🐭","⬛️","⬛️","⬛️","⬛️","⬛️" ],
           ["⬜️","⬜️","⬜️","⬛️","⬛️","⬛️" ],
           ["⬛️","⬛️","⬜️","⬜️","⬛️","⬛️" ],
           ["⬛️","⬛️","⬛️","⬜️","⬜️","⬜️" ],
           ["⬜️","⬜️","⬜️","⬛️","⬜️","⬜️" ],
           ["⬜️","⬛️","⬛️","⬜️","⬜️","🚪" ]
           ]

def draw_tablero():
    for row in tablero:
        print("".join(row))

draw_tablero()

mickey_pos = [0,0]


while True:
    draw_tablero()
    print("¿Dónde está Mickey?")
    print("1. Arriba")
    print("2. Abajo")
    print("3. Izquierda")
    print("4. Derecha")
    print("5. Salir")
    direction = input("Elige una opcion: ")

    prev_row, prev_col = mickey_pos
    next_row, next_col = prev_row, prev_col

    match direction:
        case "1":
            next_row = prev_row - 1
        case "2":
            next_row = prev_row + 1
        case "3":
            next_col = prev_col - 1
        case "4":
            next_col = prev_col + 1
        case "5":
            print("Has decidido salir del juego, hasta luego.!")
            break
    if next_row < 0 or next_row > 5 or next_col < 0 or next_col > 5:
        print("Te has salido del laberinto")
        continue
    else:
        if tablero[next_row][next_col] == "⬛️":
            print("En esa direccion hay un obstaculo")
            continue
        elif tablero[next_row][next_col] == "🚪":
            print("Has encontrado la salida")
            tablero[prev_row][prev_col] == "⬜️"
            tablero[next_row][next_col] = "🐭"
            break
            
        else:
            tablero[prev_row][prev_col] == "⬜️"
            tablero[next_row][next_col] = "🐭"
            mickey_pos = [next_row, next_col]
            print(f"posicion mickey {mickey_pos}")
