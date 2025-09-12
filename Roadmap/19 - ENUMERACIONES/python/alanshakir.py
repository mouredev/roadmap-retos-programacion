"""
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

class WeekDay(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def week_day(day):
    print(WeekDay(day).name)
week_day(4)

#EXTRA

class Status(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Order():
    status = Status.PENDIENTE
    def __init__(self, id_order) -> None:
        self.id = id_order
    
    def display_order(self):
        print(f"La orden {self.id} tiene el siguiente estado: {self.status.name}")

    def send_order(self):
        if self.status == Status.PENDIENTE:
            self.status = Status.ENVIADO
            self.display_order()
        else:
            print("El pedido no se encuentra PENDIENTE")
    
    def cancel_order(self):
        if self.status != Status.ENTREGADO:
            self.status = Status.CANCELADO
            self.display_order()
        else:
            print("El pedido se encuentra ENTREGADO")

    def deliver_order(self):
        if self.status == Status.ENVIADO:
            self.status = Status.ENTREGADO
            self.display_order()
        else:
            print("El pedido necesita ser enviado")
