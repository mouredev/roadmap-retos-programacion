from enum import Enum

# EJERCICIO
"""
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    
def get_day(value: int) -> str:
    if 1 <= value <= 7 :
        return Weekday(value).name     
    raise ValueError(f"el número: {value} no está permitido")
        
result = get_day(8)
print(result)
"""

# EXTRA

class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELLED = 4
    
class Order:
    
    def __init__(self, id):
        self.id = id
        self.status = OrderStatus.PENDING
        
    def ship(self):
        if self.status is OrderStatus.PENDING:
            self.status = OrderStatus.SHIPPED
            self.display_status()
        else:
            print(f"No se puede enviar un pedido en estado {self.status.name}") 
        
    def deliver(self):
        if self.status is OrderStatus.SHIPPED:
            self.status = OrderStatus.DELIVERED
            self.display_status()
        else:
            print(f"No se puede entregar un pedido en estado {self.status.name}")  
                    
    def cancel(self):
        if self.status in (OrderStatus.PENDING, OrderStatus.SHIPPED):
            self.status = OrderStatus.CANCELLED
            self.display_status()
        else:
            print(f"No se puede cancelar un pedido en estado {self.status.name}")   
 
    def display_status(self):
        print(f"El estado del pedido {self.id} es {self.status.name}") 


if __name__ == "__main__":
    # entregar sin enviar
    order_6 = Order(6)
    order_6.deliver()

    # cancelar dos veces
    order_2 = Order(2)
    order_2.cancel()
    order_2.cancel()

    # entregar un pedido cancelado
    order_3 = Order(3)
    order_3.cancel()
    order_3.deliver()

    # flujo completo
    order_5 = Order(5)
    order_5.ship()
    order_5.ship()
    order_5.deliver()
    order_5.cancel()