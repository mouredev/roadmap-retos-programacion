# EJERCICIO:
# Empleando tu lenguaje, explora la definición del tipo de dato
# que sirva para definir enumeraciones (Enum).
# Crea un Enum que represente los días de la semana del lunes
# al domingo, en ese orden. Con ese enumerado, crea una operación
# que muestre el nombre del día de la semana dependiendo del número entero
# utilizado (del 1 al 7).

from enum import Enum


class DiasSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7


def mostrar_dia_semana() -> None:
    dia = input("Introduce el numero del dia de la semana: ")
    if not dia.isdigit() or int(dia) < 1 or int(dia) > 7:
        print("Error, el numero del dia de la semana debe ser entre 1 y 7")
        return mostrar_dia_semana()
    else:
        dia = int(dia)
        print(DiasSemana(dia).name)


mostrar_dia_semana()


#
# DIFICULTAD EXTRA (opcional):
# Crea un pequeño sistema de gestión del estado de pedidos.
# Implementa una clase que defina un pedido con las siguientes características:
# - El pedido tiene un identificador y un estado.
# - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
# - Implementa las funciones que sirvan para modificar el estado:
#   - Pedido enviado
#   - Pedido cancelado
#   - Pedido entregado
#   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
# - Implementa una función para mostrar un texto descriptivo según el estado actual.
# - Crea diferentes pedidos y muestra cómo se interactúa con ellos.


class EstadoPedido(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4


class Pedido:
    def __init__(self, id: int, estado: EstadoPedido = EstadoPedido.PENDIENTE) -> None:
        self.id = id
        self.estado = estado

    def enviar(self) -> None:
        if self.estado == EstadoPedido.PENDIENTE:
            self.estado = EstadoPedido.ENVIADO
            print(f"El pedido {self.id} ha sido enviado")
        else:
            print(
                f"El pedido {self.id} no puede ser enviado porque su estado es {self.estado.name}"
            )

    def cancelar(self) -> None:
        if self.estado == EstadoPedido.PENDIENTE:
            self.estado = EstadoPedido.CANCELADO
            print(f"El pedido {self.id} ha sido cancelado")
        else:
            print(
                f"El pedido {self.id} no puede ser cancelado porque su estado es {self.estado.name}"
            )

    def entregar(self) -> None:
        if self.estado == EstadoPedido.ENVIADO:
            self.estado = EstadoPedido.ENTREGADO
            print(f"El pedido {self.id} ha sido entregado")
        else:
            print(
                f"El pedido {self.id} no puede ser entregado porque su estado es {self.estado.name}"
            )

    def mostrar_estado(self) -> None:
        print(f"El estado del pedido {self.id} es {self.estado.name}")


pedidos = [
    Pedido(1, EstadoPedido.PENDIENTE),
    Pedido(2, EstadoPedido.ENVIADO),
    Pedido(3, EstadoPedido.ENTREGADO),
    Pedido(4, EstadoPedido.CANCELADO),
]

for pedido in pedidos:
    pedido.mostrar_estado()
    pedido.enviar()
    pedido.entregar()
    pedido.cancelar()
    pedido.mostrar_estado()