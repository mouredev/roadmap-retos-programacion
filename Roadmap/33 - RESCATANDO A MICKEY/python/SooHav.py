# 33 RESCATANDO A MICKEY
import numpy as np


def crear_laberinto(filas, columnas, obstaculos=0.3):
    if filas < 3 or columnas < 3:
        raise ValueError(
            "El laberinto debe tener al menos 3 filas y 3 columnas")

    laberinto = np.empty((filas, columnas), dtype=object)

    fila_entrada = np.random.randint(0, filas-2)
    fila_salida = np.random.randint(fila_entrada + 2, filas)
    columna_entrada = np.random.randint(0, columnas-2)
    columna_salida = np.random.randint(columna_entrada, columnas)
    laberinto[fila_entrada, columna_entrada] = "🐭"
    laberinto[fila_salida, columna_salida] = "🚪"

    for i in range(filas):
        for j in range(columnas):
            if laberinto[i, j] is None:
                if np.random.random() > obstaculos:
                    laberinto[i, j] = "⬜"
                else:
                    laberinto[i, j] = "⬛"

    return laberinto


def encontrar_coordenadas(matriz, dato):
    filas, columnas = matriz.shape
    for i in range(filas):
        for j in range(columnas):
            if matriz[i, j] == dato:
                return (i, j)
    return None


def movimiento(coordenadas1, coordenadas2):
    fila, columna = coordenadas1[0] + \
        coordenadas2[0], coordenadas1[1] + coordenadas2[1]
    return (fila, columna)

# Función para mostrar el menú


def menu():
    while True:
        print("Menú:")
        print("1. Generar Laberinto")
        print("2. Mover a Mikey")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        try:
            return int(opcion)
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número entero.")


while True:
    opcion = menu()

    if opcion == 1:
        try:
            filas = int(input("Ingrese el número de filas: "))
            columnas = int(input("Ingrese el número de columnas: "))
            obstaculos = float(
                input("Ingrese el porcentaje de obstáculos (entre 0.2 y 0.7): "))
            laberinto = crear_laberinto(filas, columnas, obstaculos)
            for celda in laberinto:
                print("".join(celda))
        except ValueError:
            print("Intente nuevamente")

    elif opcion == 2:

        while True:
            coordenadas_mikey = encontrar_coordenadas(laberinto, "🐭")
            coordenadas_salida = encontrar_coordenadas(laberinto, "🚪")

            if coordenadas_mikey == coordenadas_salida:
                print("¡Mikey encontró la salida!")
                break

            elif coordenadas_mikey is None:
                print("Primero debe generar un laberinto.")
                break

            else:
                print(f"Mikey se encuentra en {coordenadas_mikey}")
                opcion_movimiento = int(
                    input("1. sur, 2. oeste, 3. este, 4. norte Ingrese una opción: "))
                coordenadas_movimiento = [(1, 0), (0, -1), (0, 1), (-1, 0)]

                if 1 <= opcion_movimiento <= 4:
                    nueva_coordenada = movimiento(
                        coordenadas_mikey, coordenadas_movimiento[opcion_movimiento - 1])
                    fila, columna = nueva_coordenada

                    if 0 <= fila < laberinto.shape[0] and 0 <= columna < laberinto.shape[1]:

                        if laberinto[fila, columna] == "⬜":
                            laberinto[coordenadas_mikey[0],
                                      coordenadas_mikey[1]] = "⬜"
                            laberinto[fila, columna] = "🐭"
                            for celda in laberinto:
                                print("".join(celda))
                            print(f"Mikey se mueve a {nueva_coordenada}")
                        elif laberinto[fila, columna] == "🚪":
                            print("¡Mikey encontró la salida!")
                            laberinto[coordenadas_mikey[0],
                                      coordenadas_mikey[1]] = "⬜"
                            for celda in laberinto:
                                print("".join(celda))
                            break
                        else:
                            print(
                                "¡Movimiento inválido! Mikey no puede moverse allí.")

                            opcion = int(
                                input("Debes elegir una opcion: 1 (continua) 2 (finaliza): "))

                            match opcion:
                                case 1:
                                    continue
                                case 2:
                                    print("Mikey no pudo salir!!")
                                    break

                    else:
                        print("¡Movimiento inválido! Mikey está fuera del laberinto.")
                else:
                    print("Opción inválida. Por favor, ingrese una opción válida.")

    elif opcion == 3:
        print("¡Hasta la próxima!")
        break
