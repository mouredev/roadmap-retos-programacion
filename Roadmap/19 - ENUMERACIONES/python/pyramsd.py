from enum import Enum

class DiasSemana(Enum):
    Lunes = 1
    Martes = 2
    Miercoles = 3
    jueves = 4
    Viernes = 5
    Sabado = 6
    Domingo = 7

def getDiaSemana(n):
    for day in DiasSemana:
        if day.value == n:
            return day.name
    return "Dia no valido"

print(getDiaSemana(2))


'''
EXTRA
'''
class EstadoPedido(Enum):
    PENDIENTE = 0
    ENVIADO = 1
    ENTREGADO = 2
    CANCELADO = 3

class Pedido:
    def __init__(self, status, id) -> None:
        self.status = status
        self.id = id
    
    def enviar_pedido(self):
        if self.status == EstadoPedido.PENDIENTE:
            self.status = EstadoPedido.ENVIADO
        else:
            print("El pedido no puede ser enviado en su estado actual")

    def pedido_entregado(self):
        if self.status == EstadoPedido.ENVIADO:
            self.status = EstadoPedido.ENTREGADO
        else:
            print("El pedido no puede ser entregado en su estado actual")

    def cancelar_pedido(self):
        if self.status == EstadoPedido.PENDIENTE:
            self.status = EstadoPedido.CANCELADO
        else:
            print("El pedido no puede ser cancelado en su estado actual")

    def estado_actual(self):
        return f"Estado actual del pedido {self.id}: {self.status.name}"


pedido1 = Pedido(EstadoPedido.PENDIENTE, 1)
print(pedido1.estado_actual())
pedido1.enviar_pedido()
print(pedido1.estado_actual())
pedido1.pedido_entregado()
print(pedido1.estado_actual())
pedido1.cancelar_pedido()

pedido2 = Pedido(EstadoPedido.PENDIENTE, 2)
print(pedido2.estado_actual())
pedido2.cancelar_pedido()
print(pedido2.estado_actual())
