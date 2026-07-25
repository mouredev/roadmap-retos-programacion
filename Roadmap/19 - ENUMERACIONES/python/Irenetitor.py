from enum import Enum

#Exercise
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY =  4
    FRIDAY =  5
    SATURDAY = 6
    SUNDAY = 7

def get_day(number: int):
    print(Weekday(number).name)

get_day(4)

#Extra Exercise

class OrderStatus(Enum):
    Pending = 1
    Shipped = 2
    Delivered = 3
    Canceled = 4

class Order:

    def __init__(self, id) -> None:
        self.id = id
        self.status = OrderStatus.Pending

    def ship(self):
        if self.status == OrderStatus.Pending:
            self.status = OrderStatus.Shipped
            self.display_status()
        else:
            print("The order has been shipped or cancelled")

    def deliver(self):
        if self.status == OrderStatus.Shipped:
            self.status = OrderStatus.Delivered
            self.display_status()
        else:
            print("The order has been shipped or cancelled")


    def cancel(self):
        if self.status not in (OrderStatus.Shipped, OrderStatus.Delivered):
            self.status = OrderStatus.Canceled
            self.display_status()
        else:
            print("The order can't be canceled, it has been shipped or delivered already")


    def display_status(self):
        print(f"the status of your order {self.id} is {self.status.name}")


order_1 = Order(1)
order_1.display_status()
order_1.deliver()
order_1.ship()
order_1.cancel()
order_1.deliver()
