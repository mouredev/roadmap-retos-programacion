"""
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
"""

from enum import Enum

class DayOfWeek(Enum):

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRYDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def get_name_day_of_week(number: int):
    return DayOfWeek(number)

def get_number_day_of_week(name: str):
    return DayOfWeek[name]

day = get_name_day_of_week(2)
print(day)
print(day.name)

day = get_number_day_of_week("WEDNESDAY")
print(day)
print(day.value)


"""
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

from datetime import datetime

class OrderStatus(Enum):
    CANCELED = 0
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3

class Order():

    total_orders = 0

    def __init__(self):
        Order.total_orders += 1
        self.id = f"ORD-{datetime.now().year}-{str(Order.total_orders).zfill(3)}"
        self.status = OrderStatus.PENDING
        self.print_status()

    def change_status(self):
        if 0 < self.status.value < 3:
            self.status = OrderStatus(self.status.value + 1)
            self.print_status()
        else:
            print(f"No se puede modificar el estado del pedido {self.id}. - Pedido entregado o cancelado.")

    def cancel_order(self):
        if self.status == OrderStatus.PENDING:
            self.status = OrderStatus.CANCELED
            self.print_status()
        else:
            print(f"No se puede cancelar el pedido {self.id} debido a que ya ha sido enviado, entregado o cancelado.")

    def print_status(self):
        match self.status:
            case OrderStatus.CANCELED:
                print(f"El pedido {self.id} fue cancelado.")
            case OrderStatus.PENDING:
                print(f"El envío {self.id} esta en preparación y será enviado en breve.")
            case OrderStatus.SHIPPED:
                print(f"El envío {self.id} ya ha sido envíado y lo recibirá pronto.")
            case OrderStatus.DELIVERED:
                print(f"El envío {self.id} ha sido entregado.")
            




order1 = Order()
order2 = Order()
order3 = Order()
order2.cancel_order()
order1.change_status()
order2.change_status()
order1.change_status()
order3.change_status()
order3.change_status()



