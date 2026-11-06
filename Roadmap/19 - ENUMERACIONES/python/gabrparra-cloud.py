"""
Medio
06/05/2024
#19
ENUMERACIONES
/*
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 *
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
 */
"""

from enum import Enum

class Weekday(Enum):
    MONDAY =    1
    TUESDAY =   2
    WEDNESDAY = 3
    THURSDAY =  4
    FRIDAY =    5
    SATURDAY =  6
    SUNDAY =    7

def get_day(number:int):
    print(f"el nombre es es {Weekday(number).name}")
    print(f"el valor es {Weekday(number).value}")

get_day(1)
get_day(2)
get_day(3)
get_day(4)
get_day(5)
get_day(6)


"""
Extra
"""

class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELLED = 4

class Order:

    def __init__(self, id: int, status = OrderStatus.PENDING)-> None:
        self.id= id
        self.status = status

    def ship(self):
        if self.status == OrderStatus.PENDING:
            self.status = OrderStatus.SHIPPED
            print (f"El pedido cambio a estado  {self.status.name}")
        else:
            print (f"El pedido no puede ser enviado, esta en el estado  {self.status.name}")

    def deliver(self):
        if self.status == OrderStatus.SHIPPED:
            self.status = OrderStatus.DELIVERED
            print (f"El pedido cambio a estado  {self.status.name}")
        else:
            print (f"El pedido no puede ser entregado, esta en el estado  {self.status.name}")
        
    def cancel(self):
        if self.status != OrderStatus.DELIVERED:
            self.status = OrderStatus.CANCELLED
            print (f"El pedido cambio a estado  {self.status.name}")
        else:
            print (f"El pedido no puede ser cancelado")

    def status_order(self):
        print(f"El estado del pedido {self.id} es {self.status.name}")



order01 = Order(1)
order01.status_order()
order01.ship()
order01.deliver()
order01.cancel()
