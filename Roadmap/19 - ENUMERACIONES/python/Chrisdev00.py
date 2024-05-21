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

class WeekDays(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def day_name(num):
    try:
        day = WeekDays(num)
        return day.name.capitalize()
    except ValueError:
        return "Numero del dia invalido"
    
print(day_name(4))
print(day_name(1))
print(day_name(7))
print(day_name(8))

######## -----------------------------------  EXTRA  ------------------------------------- ################

class OrderState(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Pedido:

    def __init__(self, identificador, estado):
        self.identificador = identificador
        self.estado = estado

    def upgrade_state(self, new_state):
        if new_state in OrderState:
            self.estado = new_state
            print(f"El estado del pedido {self.identificador} ha sido actualizado a {self.estado.name}")
        else:
            print(f"El pedido {self.identificador} no se pudo enviar.")
    
    def send_order(self):
        if self.estado == OrderState.PENDIENTE:
            self.upgrade_state(OrderState.ENVIADO)
        else:
            print("El pedido no se pudo enviar porque no esta pendiente")

    def order_delivered(self):
        if self.estado == OrderState.ENVIADO:
            self.upgrade_state(OrderState.ENTREGADO)
        else:
            print(f"El pedido {self.identificador} no se pudo marcar como entregado porque no fue enviado aun")
    
    def cancel_order(self):
        if self.estado != OrderState.CANCELADO or self.estado != OrderState.ENTREGADO:
            self.upgrade_state(OrderState.CANCELADO)
        else:
            print("El pedido ya esta cancelado")



pedido1 = Pedido(identificador=3, estado=OrderState.PENDIENTE)

pedido1.send_order()
print(f"El pedido {pedido1.identificador}: Estado - {pedido1.estado.name}")

pedido1.cancel_order()
print(f"El pedido {pedido1.identificador}: Estado - {pedido1.estado.name}")

pedido1.order_delivered()
print(f"El pedido {pedido1.identificador}: Estado - {pedido1.estado.name}")

pedido1.cancel_order()
pedido1.order_delivered()