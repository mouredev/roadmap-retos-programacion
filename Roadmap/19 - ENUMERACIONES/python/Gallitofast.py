#Enumeraciones Python
from enum import Enum
class Weekdays(Enum):
    Monday=1
    Tuesday=2
    Wednesday=3
    Thursday=4
    Friday=5
    Saturday=6
    Sunday=7

    @classmethod
    def get_day(cls,num):
        #this function to return the day name
        try:
            return cls(num).name
        except ValueError:
            return "Error, {num} is not a valid number, the week only have 7 days you fool!"
    
if __name__=="__main__":
    for i in range (1,8):
        print(f"Day {i} : {Weekdays.get_day(i)}")
    print(f"\nFourth day is: {Weekdays.get_day(4)}")

    """Dificultad extra"""

class Orderstatus(Enum):
    Pending=1
    Shipping=2
    Delivered=3
    Canceled=4
class Order:
    status=Orderstatus.Pending
    def __init__(self,id) -> None:
        self.id=id

    def ship(self):
        if self.status==Orderstatus.Pending:
           self.status=Orderstatus.Shipping
           self.display_status()
        else:
            print("The order has already been shipped or cancelled")

    def deliver(self):
        if self.status == Orderstatus.Shipping:
            self.status = Orderstatus.Delivered
            self.display_status()
        else:
            print("The order has to been sent before deliver")

    def cancel(self):
        if self.status != Orderstatus.Delivered:
            self.status= Orderstatus.Canceled
            self.display_status()
        else:
            print("The order cannot be cancelled since it has already been delivered")

    def display_status(self):
        print(f"El status de el envio({self.id}) es: {self.status.name}")


first_order = Order(1)
first_order.display_status()
first_order.deliver()
first_order.ship()
first_order.deliver()
first_order.cancel()