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


class WeekDays(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def get_day_name(day: int) -> str:
    return WeekDays(day).name.lower()


print(get_day_name(6))


""""
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


class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELED = 4


class Order:
    status = OrderStatus.PENDING

    def __init__(self, id) -> None:
        self.id = id

    def ship(self):
        if self.status == OrderStatus.PENDING:
            self.status = OrderStatus.SHIPPED
            self.display_status()
        else:
            print("El pedido ya ha sido enviado o cancelado")

    def deliver(self):
        if self.status == OrderStatus.SHIPPED:
            self.status = OrderStatus.DELIVERED
            self.display_status()
        elif self.status == OrderStatus.DELIVERED:
            print("El pedido ya ha sido entregado.")
        elif self.status == OrderStatus.CANCELED:
            print("El pedido ha sido cancelado.")
        else:
            print("El pedido necesita ser enviado antes de entregarse.")

    def cancel(self):
        if self.status != OrderStatus.DELIVERED:
            self.status = OrderStatus.CANCELED
            self.display_status()
        else:
            print("El pedido no se puede cancelar ya que ya se ha entregado.")

    def display_status(self):
        print(f"El estado del pedido {self.id} es {self.status.name}")


my_order = Order(12336)
my_order.display_status()
my_order.ship()
my_order.deliver()

my_order_2 = Order(12337)
my_order_2.ship()
my_order_2.cancel()
my_order_2.deliver()
