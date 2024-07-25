from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def get_day_name(number):
    try:
        day = Weekday(number)
        return day.name
    except ValueError:
        return "Error"

print(get_day_name(2))
print(get_day_name(6))
print(get_day_name(4))


#Extra
class Status(Enum):
    sent = "Sent"
    pending = "Pending"
    cancel = "Cancel"
    delivered = "Delivered"

class Order:

    def __init__(self,id:int,status:Status) -> None:
        self.id = id
        self.status = status
    
    def get_status(self):
        return self.status.value    
    def set_sent(self):
        if self.status == Status.pending:
            self.status = Status.sent
        else:
            print(f'Current status is {self.status.name} could not be change to sent')

    def set_delivered(self):
        if self.status == Status.sent:
            self.status = Status.delivered
        else:
            print("Status is not sent so could not be changed to delivered")                
    def cancel(self):
        if self.status == Status.delivered:
            print("Order was delivered could not be cancelled") 
        else:
            self.status = Status.cancel   

order1 = Order(1,Status.pending)
print(order1.get_status())
order1.set_delivered()
order1.set_sent()
print(order1.get_status())
order1.set_delivered()
print(order1.get_status())
order1.cancel()

order2 = Order(2,Status.pending)
order2.cancel()
print(order2.get_status())