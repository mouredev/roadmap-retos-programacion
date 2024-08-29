"""
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
"""

grid = [
    ['🐭', '⬛️', '⬜️', '⬜️', '⬜️', '⬛️'],
    ['⬜️', '⬜️', '⬜️', '⬛️', '⬜️', '⬜️'],
    ['⬛️', '⬜️', '⬛️', '⬛️', '⬛️', '⬜️'],
    ['⬜️', '⬜️', '⬛️', '⬜️', '⬜️', '⬜️'],
    ['⬜️', '⬛️', '⬜️', '⬜️', '⬛️', '⬛️'],
    ['⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '🚪']
]

row, col = 0, 0
invalid_move = False
won_game = False

def print_grid():
    """Printing updated"""
    print("\n")
    for row in grid:
        print(' '.join(row))

def win_check():
    """Checking if the player has won"""
    if grid[row][col] == '🚪':
        return True
    else:
        return False

print("Bienvenido a la aventura de Mickey Mouse")
print("Mickey Mouse ha quedado atrapado en un laberinto mágico creado por Maléfica")
print_grid()

print("Dale indicaciones a Mickey para salir de aquí y escribe SALIR en cualquier momento para salir del juego.")
print("Presiona arriba (E), abajo (X), izquierda (S) y derecha (D) y luego <ENTER>.")

while True:
    if won_game:
        print("Mickey Mouse ah encontrado la salida!")
        break

    if invalid_move:
        print("Movimiento inválido. Inténtalo de nuevo.")

    direction = input("a donde quieres que vaya?: ")

    # Keyword to exit the game
    if direction.lower() == 'salir':
        print("Lamento que tengas que irte, vuelve pronto!")
        break

    if direction.lower() == 'e':
        if row > 0 and grid[row - 1][col] != '⬛️':
            grid[row][col] = '⬜️'
            row -= 1
            won_game = win_check()
            grid[row][col] = '🐭'
        else:
            invalid_move = True
    elif direction.lower() == 'x':
        if row < 5 and grid[row + 1][col] != '⬛️':
            grid[row][col] = '⬜️'
            row += 1
            won_game = win_check()
            grid[row][col] = '🐭'
        else:
            invalid_move = True
    elif direction.lower() == 's':
        if col > 0 and grid[row][col - 1] != '⬛️':
            grid[row][col] = '⬜️'
            col -= 1
            won_game = win_check()
            grid[row][col] = '🐭'
        else:
            invalid_move = True
    elif direction.lower() == 'd':
        if col < 5 and grid[row][col + 1] != '⬛️':
            grid[row][col] = '⬜️'
            col += 1
            won_game = win_check()
            grid[row][col] = '🐭'
        else:
            invalid_move = True

    print_grid()
