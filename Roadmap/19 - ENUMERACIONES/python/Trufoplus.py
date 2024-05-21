###############################################################################
### ENUMERACIONES:
### (https://docs.python.org/es/3.14/howto/enum.html#enum-basic-tutorial)
###############################################################################
from enum import Enum

# Definimos el Enum para los dias de la semana
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# Solicitamos el dia de la semana para los numeros de 1 al 7
for day in range(1, 8): 
    print(Weekday(day).name)
    
###############################################################################
### DIFICULTAD EXTRA
###############################################################################

class OrderStatus(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    CANCELADO = 3
    ENTREGADO = 4

class Order():
    def __init__(self, id:str):
        self.id = id
        self.status = OrderStatus(1)       
    
    def change_status(self):
        print("\nSelecciona el nuevo estado del pedido (del 2 al 4): ")
        new_status = OrderStatus(int(input("2:ENVIADO, 3:CANCELADO, 4:ENTREGADO: ")))
            
        if self.status == OrderStatus.CANCELADO:
            print("*EL pedido ha sido cancelado, no se puede modificar")
        elif new_status.value <= self.status.value:
            print(f"*El pedido ya ha sido {self.status.name.lower()} no se puede cambiar a {new_status.name.lower()}")
        else:
            self.status = new_status
            print(f"Pedido cambiado a {self.status.name.lower()}")
        print(self)
        self.new_change()
        
    def new_change(self):
        new_change = input("\n¿quieres cambiar el estado (si/no): ").lower()
        if new_change == "si":
            self.change_status()
                      
    def __str__(self):
        return f"\nEstado del pedido:\nId: {self.id}\nStatus: {self.status.name.capitalize()}" 

def new_order():
    id = input("identificador del pedido: ")    
    return Order(id)


my_order = new_order()
print(my_order)
my_order.change_status()
