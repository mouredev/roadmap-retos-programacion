from enum import Enum

#EJERCICIO

class Weekday(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7

def get_day(number:int):
    print(Weekday(number).name)

get_day(1)


#EJERCICIO EXTRA

class Estado(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class order:

    def __init__(self, id:int):
        self.id = id
        self.state = Estado.PENDIENTE

    def OrderSended(self):
        if self.state == Estado.PENDIENTE:
            self.state = Estado.ENVIADO
            print("Enviando pedido")
        else:
            print("El pedido no existe")

    def OrderDelivered(self):
        if self.state == Estado.ENVIADO:
            self.state = Estado.ENTREGADO
            print("Pedido entregado")
        else:
            print("El pedido no esta enviado")
    
    def OrderCancelled(self):
        if self.state != Estado.ENTREGADO:
            self.state = Estado.CANCELADO
            print("Pedido cancelado")
        else:
            print("El pedido no existe")

    def print(self):
        print(f"El pedido {self.id}, se encuentra en estado de {self.state.name}.")

order_1 = order(1)
order_1.print()
order_1.OrderSended()
order_1.OrderDelivered()
order_1.print()


order_2 = order(2)
order_2.print()
order_2.OrderSended()
order_2.OrderCancelled()
order_2.print()