from enum import Enum
from datetime import date
from typing import Literal

"""/*
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7). """

class WeekDay(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    @classmethod
    def today(cls):
        print("Today is %s" % cls(date.today().isoweekday()).name)


WeekDay.today() # Today is Friday

def show_week_day(num: Literal[1, 2, 3, 4, 5, 6, 7]):
    try:
        day = WeekDay(num)
        print(f"The day is {day.name}")

    except ValueError:
        print("Invalid Week Number")


for i in range(1, 8):
    show_week_day(i)

"""
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

class OrderState(Enum):
    PENDING = 0
    SENDED = 1
    DELIVERED = 2
    CANCELED = 3

class Order:
    def __init__(self, identificator: int):
        self.identificator = identificator
        print(f"Orden creada, identificador: {self.identificator}")
        self._state = OrderState.PENDING

    def send(self):
        if self._state == OrderState.PENDING:
            self._state = OrderState.SENDED
        else:
            raise ValueError(f"No se puede enviar el pedido. Estado: {self._state.name}")
        
    def cancel(self):
        if self._state in (OrderState.PENDING, OrderState.SENDED):
            self._state = OrderState.CANCELED
        else:
            raise ValueError(f"No se puede cancelar el pedido. Estado: {self._state.name}")
        
    def deliver(self):
        if self._state == OrderState.SENDED:
            self._state = OrderState.DELIVERED
        else:
            raise ValueError(f"No se puede entregar el pedido. Estado: {self._state.name}")

    def current_state(self):
        description = {
            OrderState.PENDING: "Pendiente",
            OrderState.SENDED: "Enviado",
            OrderState.CANCELED: "Cancelado",
            OrderState.DELIVERED: "Entregado"
        }
        return f"Pedido: {self.identificator}, Estado: {description[self._state]}"
    

# Uso

if __name__ == "__main__":
    print("-----Gestión de Pedidos-----")
    order1 = Order(1)
    print(order1.current_state())
    order1.send()
    print(order1.current_state())
    order1.deliver()
    print(order1.current_state())

    order2 = Order(2)
    order2.send()
    print(order2.current_state())
    order2.cancel()
    print(order2.current_state())

    order3 = Order(3)
    order3.send()
    order3.deliver()
    print(order3.current_state())

    try:
        order3.cancel()
    except ValueError as e:
        print(f"Error: {type(e).__name__},", e)