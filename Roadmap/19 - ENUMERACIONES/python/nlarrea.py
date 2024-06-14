"""
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
"""

from enum import Enum


class WeekDay(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def print_week_day(day_index: int) -> None:
    if day_index < 1 or day_index > 7:
        print("You should enter a number between 1 and 7 (both included).")
        return

    print(WeekDay(day_index).name.capitalize())


print_week_day(5)  # Friday


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


class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELED = 4


class Order:
    def __init__(self, order_id: str) -> None:
        self.order_id = order_id
        self.state = OrderStatus.PENDING

        print(f"\nThe order '{self.order_id}' is {self.state.name}")

    def update_state(self):
        if (
            self.state == OrderStatus.CANCELED
            or self.state == OrderStatus.DELIVERED
        ):
            # If order is canceled or delivered -> maintain the state as it is
            return

        self.state = OrderStatus(self.state.value + 1)

    def cancel_order(self):
        if self.state != OrderStatus.DELIVERED:
            self.state = OrderStatus.CANCELED

    def print_current_state(self):
        print(f"The order '{self.order_id}' is {self.state.name}")


order_1 = Order("1234")  # pending
order_1.update_state()
order_1.print_current_state()  # shipped
order_1.update_state()
order_1.print_current_state()  # delivered
order_1.cancel_order()  # it won't work because it's delivered already
order_1.print_current_state()  # delivered

order_2 = Order("5678")  # pending
order_2.update_state()
order_2.print_current_state()  # shipped
order_2.cancel_order()
order_2.print_current_state()  # canceled
order_2.update_state()  # it won't work because it's canceled
order_2.print_current_state()  # canceled

order_3 = Order("1290")  # pending
order_3.cancel_order()
order_3.print_current_state()  # canceled
