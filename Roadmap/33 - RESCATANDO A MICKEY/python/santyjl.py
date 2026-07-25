# #33 RESCATANDO A MICKEY
#### Dificultad: Fácil | Publicación: 12/08/24 | Corrección: 19/08/24

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

import os
import time

laberinto= [
    ["🐭","⬜️","⬜️","⬛️","⬜️","⬛️"],
    ["⬜️","⬛️","⬛️","⬜️","⬜️","⬛️"],
    ["⬜️","⬜️","⬛️","⬛️","⬛️","⬜️"],
    ["⬛️","⬜️","⬜️","⬛️","⬜️","⬜️"],
    ["⬜️","⬜️","⬜️","⬜️","⬜️","⬜️"],
    ["⬛️","⬜️","⬛️","⬜️","⬜️","🚪"]
]

def formatear_laberinto():
    for linea in laberinto:
        print("".join(linea))

    print()

print( "Mickey Mouse ha quedado atrapado en un laberinto mágico creado por Maléfica.")

coordenadas_mickey:list = [0,0]

while True:
    formatear_laberinto()

    print("""
          (W)- Arriba,
          (S)- Abajo,
          (A)- Izquierda,
          (D)- Derecha
          """)
    accion:str = input("Elige el movimiento que hara Mickey Mouse para salir del laberinto: ")

    linea_actual, columna_actual = coordenadas_mickey
    linea_nueva, columna_nueva = linea_actual, columna_actual

    match accion.lower():
        case "w":
            linea_nueva = linea_actual - 1
        case "s":
            linea_nueva = linea_actual + 1

        case "a":
            columna_nueva = columna_actual - 1

        case "d":
            columna_nueva = columna_actual + 1
        case _:
            print("Dirección no válida.\n")
            continue

    if linea_nueva < 0 or columna_nueva < 0 or linea_nueva > 5 or columna_nueva > 5:
        print("este movimiento no es posible")
        time.sleep(1)
        os.system("cls")
        continue

    elif "⬛️" == laberinto[linea_nueva][columna_nueva]:
        print("En este camino hay un obstaculo, no puedes pasar, busca otro camino.")
        print("")
        time.sleep(1)
        os.system("cls")
        continue

    else:
        if "🚪" == laberinto[linea_nueva] [columna_nueva]:
            print("Felicidades, has logrado escapar del laberinto")
            break

        else:
            laberinto[linea_actual] [columna_actual] = "⬜"
            laberinto[linea_nueva] [columna_nueva] = "🐭"
            coordenadas_mickey = [linea_nueva , columna_nueva]
            time.sleep(1.5)
            os.system("cls")
            continue
