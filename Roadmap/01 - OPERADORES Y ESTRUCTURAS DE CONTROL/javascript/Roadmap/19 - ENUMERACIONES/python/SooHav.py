# 19 - Enummeraciones

# Ejercicio

from enum import Enum
import datetime
# import pytz


class DiasDeSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

    @classmethod
    def dia(cls, numero):
        print(cls(numero).name)

    @classmethod
    def dia_actual(cls):
        # hoy = datetime.datetime.now(tz).isoweekday()
        hoy = datetime.datetime.now().isoweekday()
        print(f"Hoy es {cls(hoy).name}")


# Para usar la función que muestra el día actual
# tz = pytz.timezone('America/Buenos_Aires')
DiasDeSemana.dia_actual()
# Para usar la función que muestra un día particular
numero = int(
    input("Ingresa un número del 1 al 7 para conocer el día elegido:\n"))
DiasDeSemana.dia(numero)


# Extra


class Estado(Enum):
    PENDIENTE = 0
    ENVIADO = 1
    ENTREGADO = 2
    CANCELADO = 3


class GestionPedidos:
    def __init__(self):
        self.pedidos = {}

    def nuevo_pedido(self, id_pedido):
        self.pedidos[id_pedido] = Estado.PENDIENTE

    def cambiar_estado(self, id_pedido, nuevo_estado):
        if id_pedido in self.pedidos:
            estado_actual = self.pedidos[id_pedido]
            transiciones = {
                Estado.PENDIENTE: [Estado.ENVIADO, Estado.CANCELADO],
                Estado.ENVIADO: [Estado.ENTREGADO],
                Estado.ENTREGADO: [],
                Estado.CANCELADO: []
            }

            if nuevo_estado in transiciones[estado_actual]:
                self.pedidos[id_pedido] = nuevo_estado
                print(f"Estado del pedido {
                      id_pedido} cambiado a {nuevo_estado.name}")
            else:
                raise ValueError(f"No se puede cambiar el estado de {
                                 estado_actual.name} a {nuevo_estado.name}")
        else:
            raise ValueError(f"No se encontró el pedido con ID {id_pedido}")

    def estado_pedido(self, id_pedido):
        if id_pedido in self.pedidos:
            return self.pedidos[id_pedido]
        else:
            raise ValueError(f"No se encontró el pedido con ID {id_pedido}")


# Crear una instancia de la clase GestionPedidos
gestion = GestionPedidos()

while True:
    print("\nMenú:")
    print("1. Nuevo pedido")
    print("2. Cambiar estado de un pedido")
    print("3. Consultar estado de un pedido")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        while True:
            try:
                id_pedido = int(input("Ingrese el ID del nuevo pedido: "))
                if id_pedido in gestion.pedidos:
                    raise ValueError(f"Ya existe un pedido con ID {id_pedido}")
                else:
                    gestion.nuevo_pedido(id_pedido)
                    print(f"Nuevo pedido registrado con ID {id_pedido}")
                    break  # Salir del bucle si el ID es válido
            except ValueError:
                print("Error: Ingrese un ID válido (número entero).")

    elif opcion == "2":
        while True:
            try:
                id_pedido = int(
                    input("Ingrese el ID del pedido a modificar: "))
                nuevo_estado = Estado(int(input(
                    "Ingrese el nuevo estado (0: PENDIENTE, 1: ENVIADO, 2: ENTREGADO, 3: CANCELADO): ")))
                gestion.cambiar_estado(id_pedido, nuevo_estado)
                break  # Salir del bucle si el ID es válido
            except ValueError:
                print("Error: Ingrese un  nuevo estado.")

    elif opcion == "3":
        id_pedido = int(input("Ingrese el ID del pedido a consultar: "))
        estado_actual = gestion.estado_pedido(id_pedido)
        print(f"El estado actual del pedido {
              id_pedido} es: {estado_actual.name}")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
