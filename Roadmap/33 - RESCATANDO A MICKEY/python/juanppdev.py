"""
EJERCICIO:
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

import random

# Definimos los símbolos del laberinto
VACIO = '⬜️'
OBSTACULO = '⬛️'
MICKEY = '🐭'
SALIDA = '🚪'

# Generamos el laberinto de forma automática
def generar_laberinto():
    laberinto = [[VACIO for _ in range(6)] for _ in range(6)]
    # Colocamos obstáculos aleatorios
    for _ in range(8):
        x, y = random.randint(0, 5), random.randint(0, 5)
        laberinto[x][y] = OBSTACULO
    # Colocamos a Mickey y la salida
    laberinto[0][0] = MICKEY
    laberinto[5][5] = SALIDA
    return laberinto

# Imprimimos el laberinto
def imprimir_laberinto(laberinto):
    for fila in laberinto:
        print(' '.join(fila))
    print()

# Movemos a Mickey en el laberinto
def mover_mickey(laberinto, direccion):
    # Encontramos la posición actual de Mickey
    for i in range(6):
        for j in range(6):
            if laberinto[i][j] == MICKEY:
                x, y = i, j
                break

    # Calculamos la nueva posición
    if direccion == 'arriba':
        nuevo_x, nuevo_y = x - 1, y
    elif direccion == 'abajo':
        nuevo_x, nuevo_y = x + 1, y
    elif direccion == 'izquierda':
        nuevo_x, nuevo_y = x, y - 1
    elif direccion == 'derecha':
        nuevo_x, nuevo_y = x, y + 1
    else:
        print("Dirección no válida")
        return False

    # Validamos el movimiento
    if 0 <= nuevo_x < 6 and 0 <= nuevo_y < 6:
        if laberinto[nuevo_x][nuevo_y] == VACIO or laberinto[nuevo_x][nuevo_y] == SALIDA:
            laberinto[x][y] = VACIO
            laberinto[nuevo_x][nuevo_y] = MICKEY
            return True
        elif laberinto[nuevo_x][nuevo_y] == OBSTACULO:
            print("¡Hay un obstáculo en esa dirección!")
            return False
    else:
        print("¡Movimiento fuera de los límites del laberinto!")
        return False

# Programa principal
def main():
    laberinto = generar_laberinto()
    imprimir_laberinto(laberinto)

    while True:
        direccion = input("¿Hacia dónde quieres mover a Mickey? (arriba, abajo, izquierda, derecha): ").strip().lower()
        if mover_mickey(laberinto, direccion):
            imprimir_laberinto(laberinto)
            # Verificamos si Mickey ha llegado a la salida
            if laberinto[5][5] == MICKEY:
                print("¡Mickey ha escapado del laberinto!")
                break

if __name__ == "__main__":
    main()
