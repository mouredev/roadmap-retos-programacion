from enum import Enum

"""
Enumeraciones
"""

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    
def get_day(id : int):
    print(Weekday(id).name.title())
    
get_day(1)

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
"""

class Status(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Order():
    
    status = Status.PENDIENTE
    
    def __init__(self, id : int) -> None:
        self.id = id
        

    
    def ship(self):
        if self.status == Status.PENDIENTE:
            self.status = Status.ENVIADO
            self.display_status()
            
    def deliver(self):
        if self.status == Status.ENVIADO:
            self.status = Status.ENTREGADO
        self.display_status()
            
    def cancel(self):
        if self.status != Status.ENTREGADO:
            self.status = Status.CANCELADO
        self.display_status()
        
    def display_status(self):
        print(f"Order: {self.id} : Status : {self.status}")
    
    

        
        
order_1 = Order(1)
order_1.display_status()
order_1.ship()
order_1.deliver()

order_2 = Order(2)
order_2.display_status()
order_2.ship()
order_2.cancel()
