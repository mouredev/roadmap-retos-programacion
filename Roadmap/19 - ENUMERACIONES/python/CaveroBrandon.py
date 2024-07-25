"""EJERCICIO:
Empleando tu lenguaje, explora la definición del tipo de dato
que sirva para definir enumeraciones (Enum).
Crea un Enum que represente los días de la semana del lunes
al domingo, en ese orden. Con ese enumerado, crea una operación
que muestre el nombre del día de la semana dependiendo del número entero
utilizado (del 1 al 7)."""

from enum import Enum


class WeekDay(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def get_day_from_value(day_number: int) -> str:
    return WeekDay(day_number).name


"""DIFICULTAD EXTRA (opcional):
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
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. """


class Status(Enum):
    PENDING = 0
    SEND = 1
    COMPLETED = 2
    CANCELLED = 3


class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.status = Status.PENDING
        print(f'Operation successful: Order #{self.order_id} was created with {self.status.name} status')

    def send_order(self):
        if self.status.value == 0:
            self.status = Status.SEND
            print(f'Operation successful: Order #{self.order_id} set to {self.status.name} status')
        elif self.status.value == 1:
            print(f'Operation denied: Order #{self.order_id} was already SEND')
        else:
            print(f'Operation denied: {self.status.name} order cannot be changed to SEND status')

    def completed_order(self):
        if self.status.value == 1:
            self.status = Status.COMPLETED
            print(f'Operation successful: Order #{self.order_id} set to {self.status.name} status')
        elif self.status.value == 2:
            print(f'Operation denied: Order #{self.order_id} was already COMPLETED')
        else:
            print(f'Operation denied: {self.status.name} order cannot be changed to COMPLETED status')

    def cancel_order(self):
        self.status = Status.CANCELLED
        print(f'Operation successful: #Order #{self.order_id} status set to {self.status.name}')

    def get_order_status(self):
        return self.status.name


print(f'The day that represent the number 2 is: {get_day_from_value(day_number=2)}')
print(f'The day that represent the number 5 is: {get_day_from_value(day_number=5)}')
print(f'The day that represent the number 7 is: {get_day_from_value(day_number=7)}')

print('**** EXTRA ****')
print('\n**** Regular order process ****')
new_order = Order(order_id=111)
new_order.send_order()
new_order.completed_order()

print('\n**** Order cancelled ****')
new_order = Order(order_id=222)
new_order.send_order()
new_order.cancel_order()

print('\n**** Attempt to complete an order before send it ****')
new_order = Order(order_id=333)
new_order.completed_order()

print('\n**** Attempt to send the order when it\'s already completed ****')
new_order = Order(order_id=444)
new_order.send_order()
new_order.completed_order()
new_order.send_order()