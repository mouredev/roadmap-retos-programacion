import numpy as np

arr = np.array(
    [
        [0, 0, 0, 0, 0, 0],
        [2, 2, 2, 2, 2, 2],
        [0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 3],
    ]
)

vacio = 0
inicio = [0, 3]
obstaculos = 2
salida = 3
print(""" ---- RESCATANDO A MICKEY ----""")
"""NO ESTAS USANDO EL ARRAY PARA NADA MELON"""


class Mickey:
    def __init__(self, posicion) -> None:

        fila, columna = posicion
        self.fila = fila
        self.columna = columna

    # movimientos
    def moverse_abajo(self):
        self.fila += 1
        return f"\nActual\nFila: {self.fila}\nColumna: {self.columna}"

    def moverse_arriba(self):
        self.fila -= 1
        return f"\nActual\nFila: {self.fila}\nColumna: {self.columna}"

    def moverse_izquierda(self):
        self.columna -= 1
        return f"\nActual\nFila: {self.fila}\nColumna: {self.columna}"

    def moverse_derecha(self):
        self.columna += 1
        return f"\nActual\nFila: {self.fila}\nColumna: {self.columna}"

    def __str__(self) -> str:
        return f"\nInicio\nFila: {self.fila}\nColumna: {self.columna}"


class Comprobador:

    def comprobar_obstaculo(self, fila, columna):
        return arr[fila, columna] == 2

    def comprobar_salida(self, fila, columna):
        return arr[fila, columna] == 3

    def comprobar_limite_superior(self, fila):
        return fila == 0

    def comprobar_limite_inferior(self, fila):
        return fila == 2

    def comprobar_limite_izquierdo(self, columna):
        return columna == 0

    def comprobar_limite_derecho(self, columna):
        return columna == 2


mickey = Mickey(inicio)  # Pasamos posición de inicio
comprobador = Comprobador()


def menu_principal():
    print("\nMickey esta en el inicio del laberinto")
    print(mickey)
    while True:

        print("1 = abajo")
        print("2 = Arriba")
        print("3 = izquierda")
        print("4 = derecha")
        print("5 = Terminar programa")

        opcion = input("Elige siguiente movimiento\n->")
        match opcion:
            case "1":
                if comprobador.comprobar_limite_inferior(
                    mickey.fila
                ):  # Primero comprobar que no esta en el limite. OK
                    print("Encontro el limite inferior, no puede moverse aqui")
                elif comprobador.comprobar_obstaculo(
                    mickey.fila + 1, mickey.columna
                ):  # Simulamos el movimiento hacia abajo, añádiendo +1 a la fila igual que hace la funcion moverse abajo
                    print("Encontró un obstaculo, no puede moverse aqui")

                else:
                    print(mickey.moverse_abajo())
                    print("\nMickey se ha movido hacia abajo")

                    if comprobador.comprobar_salida(mickey.fila, mickey.columna):
                        print("Enhorabuena Mickey encontró la salida")
                        break

            case "2":
                if comprobador.comprobar_limite_superior(mickey.fila):
                    print("Encontro el limite superior, no puede moverse aqui")
                elif comprobador.comprobar_obstaculo(mickey.fila - 1, mickey.columna):
                    print("Encontró un obstaculo, no puede moverse aqui")

                else:
                    print(mickey.moverse_arriba())
                    print("\nMickey se ha movido hacia arriba")
                    if comprobador.comprobar_salida(mickey.fila, mickey.columna):
                        print("Enhorabuena Mickey encontró la salida")
                        break

            case "3":
                if comprobador.comprobar_limite_izquierdo(mickey.columna):
                    print("Encontro el limite izquierdo, no puede moverse aqui")
                elif comprobador.comprobar_obstaculo(mickey.fila, mickey.columna - 1):
                    print("Encontró un obstaculo, no puede moverse aqui")

                else:
                    print(mickey.moverse_izquierda())
                    print("\nMickey se ha movido hacia izquierda")
                    if comprobador.comprobar_salida(mickey.fila, mickey.columna):
                        print("Enhorabuena Mickey encontró la salida")
                        break

            case "4":
                if comprobador.comprobar_limite_derecho(mickey.columna):
                    print("Encontro el limite derecho, no puede moverse aqui")
                elif comprobador.comprobar_obstaculo(mickey.fila, mickey.columna + 1):
                    print("Encontró un obstaculo, no puede moverse aqui")

                else:
                    print(mickey.moverse_derecha())
                    print("\nMickey se ha movido hacia derecha")
                    if comprobador.comprobar_salida(mickey.fila, mickey.columna):
                        print("Enhorabuena Mickey encontró la salida")
                        break

            case "5":
                break


menu_principal()
