import numpy as np

"""arr = np.array(
    [
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 3],
    ]
)"""

arr = np.array(
    [
        [0, 1, 0],
        [0, 0, 0],
        [0, 2, 3],
    ]
)

vacio = 0
inicio = 1
obstaculos = 2
salida = 3
print(""" ---- RESCATANDO A MICKEY ----""")
"""NO ESTAS USANDO EL ARRAY PARA NADA MELON"""


class Mickey:
    def __init__(self, posicion) -> None:
        self.posicion = posicion  # Comprobar si hay obstaculos o la salida

    def comprobar_espacio(self):  # TODO
        if self.posicion in arr == 2:
            print("Ha pillado un obstaculo")
            return False  # Necesita vovler a tirar

    def moverse_abajo(
        self,
    ):
        if self.posicion[0] < 3:  # Comprobar si hay obstaculos o la salida
            self.posicion[0] += 1
            print("\nMickey se ha movido hacia abajo")
            posicion_mickey.comprobar_espacio()  # TODO

        else:
            print("\nLlego al limite del laberinto, no puede bajar mas")

    def moverse_arriba(self):
        if self.posicion[0] > 0:
            self.posicion[0] -= 1
            print("\nMickey se ha movido hacia arriba")
        else:
            print("\nLlego al limite del laberinto, no puede subir mas")

    def moverse_izquierda(self):
        if self.posicion[1] > 0:
            self.posicion[1] -= 1
            print("\nMickey se ha movido hacia la izquierda")
        else:
            print("\nLlego al limite del laberinto, no puede moverse a la izquierda")

    def moverse_derecha(self):

        if self.posicion[1] < 3:
            self.posicion[1] += 1
            print("\nMickey se ha movido hacia la derrecha")
        else:
            print("\nLlego al limite del laberinto, no puede moverse a la derecha")

    def __str__(self) -> str:
        return f"Fila: {self.posicion[0]}\nColumna: {self.posicion[1]}\n"


posicion_mickey = Mickey([0, 1])


def menu_principal():
    print("\nMickey esta en el inicio del laberinto")

    while True:
        print(posicion_mickey)
        print("1 = abajo")
        print("2 = Arriba")
        print("3 = izquierda")
        print("4 = derecha")
        print("5 = Terminar programa")
        opcion = input("Elige siguiente movimiento\n->")
        match opcion:
            case "1":
                posicion_mickey.moverse_abajo()

            case "2":
                posicion_mickey.moverse_arriba()
            case "3":
                posicion_mickey.moverse_izquierda()

            case "4":
                posicion_mickey.moverse_derecha()

            case "5":
                break


menu_principal()
