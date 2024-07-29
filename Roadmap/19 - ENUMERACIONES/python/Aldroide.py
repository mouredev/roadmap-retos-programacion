"""
    Ejercicio
    EXplora la definicion del tipo de dato oara definir enumeraciónes (ENUM)
    Crea un Enum que represente los dias de las semanas del lunes al domingo en ese orden.
    Con ese enumerado, crea una operación de muestre el dia de la semana dependeiendo del 
    número entero utilizando del 1 al 7
"""

from enum import Enum


class week(Enum):
    Lunes = 1
    Martes = 2
    Miercoles = 3
    Jueves = 4
    Viernes = 5
    Sabado = 6
    Domingo = 7


def get_day(num: int) -> str:
    try:
        day = week(num)
        return day.name
    except ValueError:
        return "No Existe"


def get_num_day(day: str) -> int:
    try:
        return week[day].value
    except KeyError:
        return "No Existe"


print(f"El dia 7 es: {get_day(7)}")
print(f"El dia 7 es: {get_day(3)}")
print(f"El dia 7 es: {get_day(8)}")
print(f"El martes tiene el numero: {get_num_day('Martes')}")
print(f"El jueves tiene el numero: {get_num_day('Jueves')}")
print(f"Diciembre tiene el numero: {get_num_day('Diciembre')} \n")

"""
    Realiza un pequeño sistema de gestion de estado de pedidos
    Implementa una clase que defina un pedido con las siguientes caracteristicas:
        * El pedido tiene un identificador y un estado
        * El estado es un Enum con estos valores:
            - Pendiente
            - Enviado
            - Entregado
            - Cancelado
        * Implementa las funciones que sirvan para modificar el estado:
            - Pedido enviado
            - Pedido cancelado
            - Pedido entregado
        (Establece una lógica, por ejemplo no se puede entregar si no se ha enviado etc.)
        Implementa una función para mostrar un texto descriptivo segun el estado actual
        Crea diferentes pedidos y muestra cómo se interactúa con ellos.
"""


class Estado(Enum):
    Pendiente = 1
    Enviado = 2
    Entregado = 3
    Cancelado = 4


class Pedidos:

    estado = Estado.Pendiente

    def __init__(self, id_pedido):
        self.id_pedido = id_pedido

    def enviar(self):
        if self.estado == Estado.Pendiente:
            self.estado = Estado.Enviado
            self.mostrar_estado()
        else:
            self.mostrar_estado()

    def entregar(self):
        if self.estado == Estado.Enviado:
            self.estado = Estado.Entregado
            self.mostrar_estado()
        else:
            self.mostrar_estado()

    def cancelar(self):
        if self.estado != Estado.Entregado:
            self.estado = Estado.Cancelado
            self.mostrar_estado()
        else:
            self.mostrar_estado()

    def mostrar_estado(self):
        print(
            f"El estado del paquete {self.id_pedido}  es: {self.estado.name}")


print("\n==== Sistema de pedidos====\n")
pedido1 = Pedidos('P01')
# pedido1.mostrar_estado()
pedido1.entregar()
pedido1.enviar()
pedido1.entregar()
pedido1.cancelar()
