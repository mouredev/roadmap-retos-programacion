import numpy as np

arr = np.array(
    [
        [0, 0, 0, 1, 0, 0],
        [2, 2, 0, 2, 0, 2],
        [0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 3],
    ]
)
print(""" ---- RESCATANDO A MICKEY ----""")
print(
    """
Leyenda
libre = 0
Mickey = 1
obstaculos = 2
salida = 3"""
)
# quizas leyenda para el movimiento


class Mickey:
    def __init__(self, posicion) -> None:

        fila, columna = posicion
        self.fila = fila
        self.columna = columna

    # movimientos
    def moverse_abajo(self):
        self.fila += 1
        return "\nMickey se ha movido hacia abajo"

    def moverse_arriba(self):
        self.fila -= 1
        return "\nMickey se ha movido hacia arriba"

    def moverse_izquierda(self):
        self.columna -= 1
        return "\nMickey se ha movido hacia izquierda"

    def moverse_derecha(self):
        self.columna += 1
        return "\nMickey se ha movido hacia derecha"


class Comprobador:

    def comprobar_obstaculo(self, fila, columna):
        return arr[fila, columna] == 2

    def comprobar_salida(self, fila, columna):
        return arr[fila, columna] == 3


mickey = Mickey(posicion=[0, 3])  # Pasamos posición de inicio
comprobador = Comprobador()
posicion_anterior = 0
posicion_actual = 1


def intentar_movimiento(direccion, mickey):  # TODO
    if (
        direccion == "1"
        and mickey.fila == 0
        or comprobador.comprobar_obstaculo(mickey.fila + 1, mickey.columna)
    ):
        return False

    elif (
        direccion == "2"
        and mickey.fila == 5
        or comprobador.comprobar_obstaculo(mickey.fila - 1, mickey.columna)
    ):
        return False

    elif (
        direccion == "3"
        and mickey.columna == 0
        or comprobador.comprobar_obstaculo(mickey.fila, mickey.columna - 1)
    ):
        return False

    elif (
        direccion == "4"
        and mickey.columna == 5
        or comprobador.comprobar_obstaculo(mickey.fila, mickey.columna + 1)
    ):
        return False

    else:
        return True


def menu_principal():
    print("\nMickey esta en el inicio del laberinto")
    while True:
        arr[mickey.fila, mickey.columna] = posicion_actual
        print(f"\n{arr}\n")

        print("1 = abajo")
        print("2 = Arriba")
        print("3 = izquierda")
        print("4 = derecha")
        print("5 = Terminar programa")

        opcion = input("Elige siguiente movimiento\n->")
        match opcion:
            case "1":
                if not intentar_movimiento("1", mickey):  # TODO

                    print("No puede moverse aqui")

                else:
                    arr[mickey.fila, mickey.columna] = posicion_anterior
                    print(mickey.moverse_abajo())

                    if comprobador.comprobar_salida(mickey.fila, mickey.columna):
                        print("Enhorabuena Mickey encontró la salida")
                        break

            case "2":
                if not intentar_movimiento("2", mickey):  # TODO

                    print("No puede moverse aqui")

                else:
                    arr[mickey.fila, mickey.columna] = posicion_anterior
                    print(mickey.moverse_arriba())
                    if comprobador.comprobar_salida(mickey.fila, mickey.columna):
                        print("Enhorabuena Mickey encontró la salida")
                        break

            case "3":
                if not intentar_movimiento("3", mickey):  # TODO

                    print("No puede moverse aqui")

                else:
                    arr[mickey.fila, mickey.columna] = posicion_anterior
                    print(mickey.moverse_izquierda())
                    if comprobador.comprobar_salida(mickey.fila, mickey.columna):
                        print("Enhorabuena Mickey encontró la salida")
                        break

            case "4":
                if not intentar_movimiento("4", mickey):  # TODO

                    print("No puede moverse aqui")

                else:
                    arr[mickey.fila, mickey.columna] = posicion_anterior
                    print(mickey.moverse_derecha())
                    if comprobador.comprobar_salida(mickey.fila, mickey.columna):
                        print("Enhorabuena Mickey encontró la salida")
                        break

            case "5":
                break


menu_principal()
