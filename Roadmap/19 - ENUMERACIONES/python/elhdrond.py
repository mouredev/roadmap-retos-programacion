from enum import Enum

"""
ENUMS
"""


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


get_day(1)
get_day(3)
# get_day(8)

"""
    EXTRA EXERCISE
"""


class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELLED = 4


class Order:

    def __init__(self, id) -> None:
        self.id = id
        self.status = OrderStatus.PENDING

    def ship(self):
        if self.status == OrderStatus.PENDING:
            self.status = OrderStatus.SHIPPED
            self.display_status()
        else:
            print("Order has already been shipped or cancelled.")

    def deliver(self):
        if self.status == OrderStatus.SHIPPED:
            self.status = OrderStatus.DELIVERED
            self.display_status()
        else:
            print("Order must be shipped before it can be delivered.")

    def cancel(self):
        if self.status != OrderStatus.DELIVERED:
            self.status = OrderStatus.CANCELLED
            self.display_status()
        else:
            print("Order cannot be cancelled as it has already been delivered.")

    def display_status(self):
        print(f"Order {self.id} status: {self.status.name}")


order_1 = Order(1)
order_1.display_status()
order_1.deliver()       # fails: not shipped yet
order_1.ship()
order_1.deliver()
order_1.cancel()        # fails: already delivered

order_2 = Order(2)
order_2.display_status()
order_2.ship()
order_2.cancel()        # cancelled before delivery
order_2.deliver()       # fails: already cancelled
