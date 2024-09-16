'''
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
'''

'''
Ejercicio
'''

from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def get_day(number: int):

    print(Weekday(number).name)

get_day(1)

'''
Dificultad Extra
'''
class OrderStatus(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Order:
    def __init__(self, id: int, status=OrderStatus.PENDIENTE):
        self.id = id
        self.status = status

    def send(self):
        if self.status == OrderStatus.PENDIENTE:
            self.status = OrderStatus.ENVIADO
            self.display_status()
        else:
            print(f"El Pedido: {self.id} se ha enviado o cancelado.")

    def deliver(self):
        if self.status == OrderStatus.ENVIADO:
            self.status = OrderStatus.ENTREGADO
            self.display_status()
        else:
            print(f"No se puede entregar el Pedido: {self.id} pues no ha sido enviado.")

    def cancel(self):
        if self.status != OrderStatus.ENTREGADO:
            self.status = OrderStatus.CANCELADO
            self.display_status()
        else:
            print(f"No se puede cancelar el Pedido: {self.id} pues ya ha sido entregado.")

    def display_status(self):
        print(f'Pedido: {self.id} Estado: {self.status.name}')


order_1 = Order(1)
order_1.deliver()
order_1.send()
order_1.deliver()
order_1.cancel()

