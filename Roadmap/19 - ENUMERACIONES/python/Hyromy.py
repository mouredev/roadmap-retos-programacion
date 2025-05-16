from enum import Enum

class Calendar(Enum):
    lunes = 1
    martes = 2
    miercoles = 3
    jueves = 4
    viernes = 5
    sabado = 6
    domingo = 7

    def get_day_by_number(num):
        return Calendar(num)

day = Calendar.get_day_by_number(2)
print(day.name)

# ---- DIFICULTAD EXTRA ----

class Estados(Enum):
    PENDIENTE = 0
    ENVIADO = 1
    ENTREGADO = 2
    CANCELADO = -1

class Pedidos:
    def __str__(self):
        return f"Pedidos id={self.id}, estado={self.estado}"

    def __init__(self, id):
        self.id = id
        self.estado = Estados(0)
        self.anterior_estado = None

    def enviar(self):
        if not self.estado == Estados.PENDIENTE:
            raise Exception(f"El pedido no se puede enviar con estado: {self.estado}")

        self.estado = Estados(1)
        self.anterior_estado = Estados(0)


    def cancelar(self):
        if self.estado == Estados.ENTREGADO:
            raise Exception(f"El pedido no se puede cancelar con estado: {self.estado}")

        self.estado = Estados(-1)

    def entregado(self):
        if not self.estado == Estados.ENVIADO:
            raise Exception(f"El pedido no se puede entregar con estado: {self.estado}")

        self.estado = Estados(2)
        self.anterior_estado = Estados(1)

pedido1 = Pedidos(1)
print(pedido1)
pedido1.cancelar()
print(pedido1)
print()

pedido2 = Pedidos(2)
print(pedido2)
pedido2.enviar()
print(pedido2)
pedido2.entregado()
print(pedido2)
try:
    pedido2.cancelar()
except:
    pass
print(pedido2)
print()

pedido3 = Pedidos(3)
print(pedido3)
pedido3.enviar()
print(pedido3)
pedido3.cancelar()
print(pedido3)
try:
    pedido3.entregado()
except:
    pass
print(pedido3)