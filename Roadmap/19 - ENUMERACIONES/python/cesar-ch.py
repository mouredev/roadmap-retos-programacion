from enum import Enum


class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7


def nombre_dia(numero):
    try:
        return DiaSemana(numero).name
    except ValueError:
        return "Número de día inválido"


print(nombre_dia(1))
print(nombre_dia(3))

"""
     DIFICULTAD EXTRA
"""


class EstadoPedido(Enum):
    PENDIENTE = "pendiente"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"
    CANCELADO = "cancelado"


class Pedido:
    def __init__(self, estado):
        self.estado = estado

    def pedido_enviado(self):
        if self.estado == EstadoPedido.PENDIENTE:
            self.estado = EstadoPedido.ENVIADO
        else:
            print("El pedido no puede ser enviado en su estado actual")

    def pedido_entregado(self):
        if self.estado == EstadoPedido.ENVIADO:
            self.estado = EstadoPedido.ENTREGADO
        else:
            print("El pedido no puede ser entregado en su estado actual")

    def pedido_cancelado(self):
        if self.estado == EstadoPedido.PENDIENTE:
            self.estado = EstadoPedido.CANCELADO
        else:
            print("El pedido no puede ser cancelado en su estado actual")

    def estado_actual(self):
        return f"Estado del pedido: {self.estado.name}"


pedido1 = Pedido(EstadoPedido.PENDIENTE)
pedido2 = Pedido(EstadoPedido.ENVIADO)

print(pedido1.estado_actual()) 
pedido1.pedido_enviado()
print(pedido1.estado_actual())  

pedido2.pedido_cancelado()
print(pedido2.estado_actual())  
