"""
Exercise
"""
from enum import Enum


class Weekday(Enum):
    LUNES = 1
    MARTES = 2
    MIÉRCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SÁBADO = 6
    DOMINGO = 7


def get_weekday_name(day_number):
    # Validate if the input is within the correct range
    if 1 <= day_number <= 7:
        return Weekday(day_number).name
    else:
        raise ValueError("Número fuera de rango. Ingrese un número del 1 al 7.")


"""
Extra
"""


class EstadoPedido(Enum):
    PENDIENTE = auto()
    ENVIADO = auto()
    ENTREGADO = auto()
    CANCELADO = auto()


class Pedido:
    def __init__(self, id):
        self.id = id
        self.estado = EstadoPedido.PENDIENTE

    def enviar_pedido(self):
        if self.estado == EstadoPedido.PENDIENTE:
            self.estado = EstadoPedido.ENVIADO
        else:
            raise ValueError("Solo los pedidos pendientes pueden ser enviados.")

    def cancelar_pedido(self):
        if self.estado in {EstadoPedido.PENDIENTE, EstadoPedido.ENVIADO}:
            self.estado = EstadoPedido.CANCELADO
        else:
            raise ValueError("Solo los pedidos pendientes o enviados pueden ser cancelados.")

    def entregar_pedido(self):
        if self.estado == EstadoPedido.ENVIADO:
            self.estado = EstadoPedido.ENTREGADO
        else:
            raise ValueError("Solo los pedidos enviados pueden ser entregados.")

    def mostrar_estado(self):
        estado_descripcion = {
            EstadoPedido.PENDIENTE: f"El pedido {self.id} está pendiente.",
            EstadoPedido.ENVIADO: f"El pedido {self.id} ha sido enviado.",
            EstadoPedido.ENTREGADO: f"El pedido {self.id} ha sido entregado.",
            EstadoPedido.CANCELADO: f"El pedido {self.id} ha sido cancelado."
        }
        return estado_descripcion[self.estado]


if __name__ == "__main__":
    print(get_weekday_name(3))  # Should print "MIERCOLES"

    pedido1 = Pedido(1)
    print(pedido1.mostrar_estado())
    pedido1.enviar_pedido()
    print(pedido1.mostrar_estado())
    pedido1.entregar_pedido()
    print(pedido1.mostrar_estado())

    pedido2 = Pedido(2)
    print(pedido2.mostrar_estado())
    pedido2.cancelar_pedido()
    print(pedido2.mostrar_estado())

    pedido3 = Pedido(3)
    print(pedido3.mostrar_estado())
    pedido3.enviar_pedido()
    print(pedido3.mostrar_estado())
