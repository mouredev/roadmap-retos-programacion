""" /*
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
 */ """

from enum import Enum

#EJERCICIO

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def get_day(number: int):
    print(Weekday(number))

get_day(1)
get_day(2)
get_day(3)
get_day(4)
get_day(5)
get_day(6)
get_day(7)

#DIFICULTAD EXTRA

class order_status(Enum):
    Pending = 1
    Shipped = 2
    Delivered = 3
    Cancelled = 4

class order():

    status = order_status.Pending

    def __init__(self, id):
        self.id = id

    def ship(self):
        if self.status == order_status.Pending:
            self.status = order_status.Shipped
            print("El pedido ya ha sido enviado.")
        else:
            print("El pedido ya ha sido enviado o cancelado.")

    def deliver(self):
        if self.status == order_status.Shipped:
            self.status = order_status.Delivered
            print("El pedido ya se ha enviado.")
        else:
            print("El pedido necesita ser enviado antes de entregarse.")

    def cancel(self):
        if self.status == order_status.Pending:
            self.status = order_status.Cancelled
            print("El pedido se ha cancelado.")
        elif self.status == order_status.Shipped:
            print("El pedido no puede ser cancelado porque ya se ha enviado.")
        elif self.status == order_status.Delivered:
            print("El pedido no puede ser cancelado porque ya se ha entregado.")
        else:
            print("El pedido ya ha sido cancelado previamente.")

    def display_status(self):
        print(f"El estado del pedido {self.id} es {self.status.name}")

Order1 = order(1)
Order1.display_status()
Order1.deliver()
Order1.display_status()
Order1.ship()
Order1.display_status()
Order1.deliver()
Order1.display_status()