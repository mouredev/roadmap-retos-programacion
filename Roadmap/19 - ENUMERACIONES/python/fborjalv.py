from enum import Enum

"""
/*
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).

"""


class days_of_week(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def show_day(number):
    print(days_of_week(number).name)

show_day(5)

"""

DIFICULTAD EXTRA (opcional):
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

class OrderStatus(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Order:

    status = OrderStatus.PENDIENTE
    def __init__(self, id) -> None:
        self.id = id

    def pedido_enviado(self):
        if self.status == OrderStatus.PENDIENTE:
            print("Hemos enviado el pedido")
            self.status = OrderStatus.ENVIADO
            self.estado_actual()
        else:
            print("Pedido no disponible para enviar")


    def pedido_entregado(self):
        if self.status == OrderStatus.ENVIADO:
            self.status = OrderStatus.ENTREGADO
            print("Hemos entregado el pedido")
            self.estado_actual()
        else:
            print("El pedido aún no está en reparto")

    def pedido_cancelado(self):
        if self.status == OrderStatus.ENTREGADO or  self.status == OrderStatus.ENVIADO:
            print("No se puede cancelar el pedido")
            self.estado_actual()
        else:
            self.status = OrderStatus.CANCELADO
            self.estado_actual()
    def estado_actual(self):
        print(f"ESTADO ACTUAL DEL PEDIDO: {self.status.name}")


new_order = Order(19)

print(new_order.status.name)
new_order.pedido_enviado()
new_order.pedido_entregado()
new_order.pedido_cancelado()