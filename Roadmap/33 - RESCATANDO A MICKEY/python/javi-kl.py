import numpy as np

arr = np.array(
    [
        [0, 0, 0, 5, 0, 0],
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
Mickey = 5
obstaculos = 2
salida = 3"""
)


class Mickey:
    def __init__(self, fila, columna) -> None:

        self.fila = fila
        self.columna = columna

    # movimientos
    def moverse(self, delta_fila, delta_columna):

        self.fila += delta_fila
        self.columna += delta_columna


class Comprobador:
    def comprobar_obstaculo(self, fila, columna):
        return arr[fila, columna] == 2

    def comprobar_salida(self, fila, columna):
        return arr[fila, columna] == 3


def intentar_movimiento(direccion, mickey, comprobador):
    nueva_fila = mickey.fila + direccion["delta_fila"]
    nueva_columna = mickey.columna + direccion["delta_columna"]
    if nueva_fila < 0 or nueva_fila > 5 or nueva_columna < 0 or nueva_columna > 5:
        print("Encontró el límite")
        return False

    if comprobador.comprobar_obstaculo(nueva_fila, nueva_columna):
        print("Obstáculo encontrado")
        return False

    else:
        arr[mickey.fila, mickey.columna] = 0  # Limpiar posición anterior
    mickey.moverse(direccion["delta_fila"], direccion["delta_columna"])  # Mover Mickey
    return True


mickey = Mickey(0, 3)  # Pasamos posición de inicio
comprobador = Comprobador()


def menu_principal():
    direcciones = {
        "1": {
            "delta_fila": 1,
            "delta_columna": 0,
            "nombre": "abajo",
        },
        "2": {
            "delta_fila": -1,
            "delta_columna": 0,
            "nombre": "arriba",
        },
        "3": {
            "delta_fila": 0,
            "delta_columna": -1,
            "nombre": "izquierda",
        },
        "4": {
            "delta_fila": 0,
            "delta_columna": 1,
            "nombre": "derecha",
        },
    }
    print("\nMickey esta en el inicio del laberinto")
    while True:
        arr[mickey.fila, mickey.columna] = 5  # Nueva posición de Mickey
        print(f"\n{arr}\n")

        print("1 = abajo")
        print("2 = Arriba")
        print("3 = izquierda")
        print("4 = derecha")
        print("5 = Terminar programa")

        opcion = input("Elige siguiente movimiento\n->")
        if opcion == "5":
            print("¡Hasta luego!")
            break
        elif opcion in direcciones:
            if intentar_movimiento(direcciones[opcion], mickey, comprobador):
                if comprobador.comprobar_salida(mickey.fila, mickey.columna):
                    arr[mickey.fila, mickey.columna] = 5  # Mostrar Mickey en la salida
                    print(f"\n{arr}\n")
                    print("¡Enhorabuena! Mickey encontró la salida")
                    break
            else:
                print("No puede moverse aquí")
        else:
            print("Opción no válida")


menu_principal()
