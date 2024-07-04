from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def get_day(number: int):
    print(Weekday(number).name)

get_day(7)
get_day(1)

### Ejercicio Exra ###

class OrderStatus(Enum):
    PENDING = 1
    SENT = 2
    DELIVERED = 3
    CANCELLED = 4

class Order:
    def __init__(self, identifier):
        self.identifier = identifier
        self.status = OrderStatus.PENDING

    def send(self):
        if self.status == OrderStatus.PENDING:
            self.status = OrderStatus.SENT
        else:
            print(f"El pedido {self.identifier} no se puede enviar porque su estado actual es {self.status.name}")

    def cancel(self):
        if self.status in [OrderStatus.PENDING, OrderStatus.SENT]:
            self.status = OrderStatus.CANCELLED
        else:
            print(f"El pedido {self.identifier} no se puede cancelar porque su estado actual es {self.status.name}")

    def deliver(self):
        if self.status == OrderStatus.SENT:
            self.status = OrderStatus.DELIVERED
        else:
            print(f"El pedido {self.identifier} no se puede entregar porque su estado actual es {self.status.name}")

    def show_status(self):
        status_text = {
            OrderStatus.PENDING : "pendiente",
            OrderStatus.SENT : "enviado",
            OrderStatus.DELIVERED : "entregado",
            OrderStatus.CANCELLED : "cancelado"
        }
        return f"El pedido {self.identifier} está {status_text[self.status]}"
    
order1 = Order(1)
order2 = Order(2)

print(order1.show_status())
order1.send()
print(order1.show_status())
order1.deliver()
print(order1.show_status())

print(order2.show_status())
order2.cancel()
print(order2.show_status())
order2.deliver()
print(order2.show_status())