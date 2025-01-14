# 19 Enumerates
import uuid
from enum import Enum


class Weekdays(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7

def show_day(num):
    print(Weekdays(num).name)

show_day(2)

# Extra

class ShipStatus(Enum):
    PENDING = 1
    SENT = 2
    DELIVERED = 3
    CANCELED = 4

class Order:

    def __init__(self):
        self.id = uuid.uuid4()
        self.state: ShipStatus = ShipStatus.PENDING

    def send(self):
        if self.state != ShipStatus.PENDING:
            print("Can't send non pending order")
        else:
            self.state = ShipStatus.SENT
            print(f"Order {self.id} sent")

    def cancel(self):
        if self.state not in [ShipStatus.SENT, ShipStatus.PENDING]:
            print("Can't cancel non sent or pending order")
        else:
            self.state = ShipStatus.CANCELED
            print(f"Order {self.id} cancelled")

    def deliver(self):
        if self.state not in [ShipStatus.SENT]:
            print("Can't deliver non sent order")
        else:
            self.state = ShipStatus.DELIVERED
            print(f"Order {self.id} delivered")

order_1 = Order()
order_1.deliver()
order_1.send()
order_1.cancel()
order_1.send()
order_1.deliver()

order_2 = Order()
order_2.send()
order_2.deliver()
order_1.cancel()