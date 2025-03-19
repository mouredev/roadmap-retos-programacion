# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -----------------------------------
# * ENUMERACIONES
# -----------------------------------
# - Una enumeración en Python es un conjunto de nombres simbólicos(miembros) 
#   que están vinculados a valores únicos.
# - se puede iterar y acceder.

# Mas info: https://docs.python.org/3/library/enum.html

"""
 * EJERCICIO 1:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
"""

from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def get_day(num: int) -> str:
    try:
        day = Weekday(num)
        return day.name
    except ValueError:
        return "'o'"

def get_num_day(day: str) -> int:
    try:
        return Weekday[day].value
    except KeyError:
        return 0

print(get_day(7))
print(get_day(3))
print(get_day(8))

print(get_num_day("TUESDAY"))
print(get_num_day("FRIDAY"))
print(get_num_day("abc"))

"""
 * EJERCICIO 2:
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

print("\nEJERCICIO 2:")

class Status(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELED = 4

class Order:
    def __init__(self, identifier):
        self.identifier = identifier
        self._status = Status.PENDING
    
    def send(self):
        print("\nEnviar:")
        if self._status == Status.PENDING:
            self._status = Status.SHIPPED
            print(self.info())
        else:
            print(f"invalid operation, ", self.info())

    def cancelled(self):
        print("\nCancelar:")
        if self._status == Status.PENDING:
            self._status = Status.CANCELED
            print(self.info())
        else:
            print(f"invalid operation, ", self.info())
    
    def delivered(self):
        print("\nEntregar:")
        if self._status == Status.SHIPPED:
            self._status = Status.DELIVERED
            print(self.info())
        else:
            print(f"invalid operation, ", self.info())

    def info(self):
        return (f"{self.identifier} is {self._status.name}")

# "Creación de pedidos"
libro1 = Order("libro1")
libro2 = Order("libro2")
libro3 = Order("libro2")

# Positivas:
print("\n-----\nOperaciones exitosas:\n-----")
libro1.send()
libro1.delivered()
libro2.cancelled()

# negativas:
print("\n-----\nOperaciones invalidas:\n-----")
libro3.delivered()
libro2.cancelled()
libro1.send()

