# -- exercise
from enum import Enum


class Days(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7


def show_day(day: int) -> str:
    return Days(day).name


print(show_day(3))


# -- extra challenge
class OrderState(Enum):
    PENDING = 1
    SENT = 2
    DELIVERED = 3
    CANCELED = 4


class Order:
    def __init__(self, order_id: int):
        self.order_id = order_id
        self.state = OrderState.PENDING

    def send_order(self):
        if self.state == OrderState.PENDING:
            self.state = OrderState.SENT
            return True
        return False

    def deliver_order(self):
        if self.state == OrderState.SENT:
            self.state = OrderState.DELIVERED
            return True
        return False

    def cancel_order(self):
        if self.state == OrderState.PENDING:
            self.state = OrderState.CANCELED
            return True
        return False

    def get_state(self):
        return self.state.name


order1 = Order(1)
order2 = Order(2)
order3 = Order(3)

print(order1.get_state())
print(order2.get_state())

print(order1.send_order())
print(order2.send_order())

print(order1.get_state())
print(order2.get_state())

print(order1.deliver_order())
print(order2.deliver_order())


print(order1.get_state())
print(order2.get_state())

print(order1.cancel_order())
print(order2.cancel_order())
