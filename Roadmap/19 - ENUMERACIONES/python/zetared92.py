# RETO 19 ENUMERACIONES
from enum import Enum

"""
CREAR UN ENUM QUE REPRESENTE LOS DÍAS DE LA SEMANA Y CREAR
UNA OPERACIÓN QUE MUESTRE EL NOMBRE DEL DÍA DEPENDIENDO DEL
NÚMERO ENTERO UTILIZADO (1-7)
"""

class Week(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def get_day(number: int):
    print(Week(number).name)

get_day(4)
get_day(6)



# Extra

print("🧩 DIFICULTAD EXTRA - SISTEMA DE GESTIÓN DEL ESTADO DE LOS PEDIDOS 🧩")

class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELLED = 4

class Order:

    status = OrderStatus.PENDING

    def __init__(self, id) -> None:
        self.id = id

    def ship(self):
        if self.status == OrderStatus.PENDING:
            self.status = OrderStatus.SHIPPED
            self.display_status()
        else:
            print("ORDER ISSUED OR CANCELED")

    def deliver(self):
        if self.status == OrderStatus.SHIPPED:
            self.status = OrderStatus.DELIVERED
            self.display_status()
        else:
            print("THE ORDER NEEDS TO BE SHIPPED BEFORE BEING DELIVERED")

    def cancel(self):
        if self.status != OrderStatus.DELIVERED:
            self.status = OrderStatus.CANCELLED
            self.display_status()
        else:
            print("ORDER SENT, CANNOT BE CANCELLED")

    def display_status(self):
        print(f"THE STATUS OF THE ORDER {self.id} IS {self.status.name}")

First_Order = Order(1)
First_Order.display_status()
First_Order.deliver()
First_Order.ship()
First_Order.deliver()
First_Order.cancel()        