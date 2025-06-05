"""
Enumeraciones
"""

#enumeraciones: Enum es una clase especial que te permite definir constantes con nombre agrupadas en una categoría. Es como crear una lista de opciones válidas con nombre propio y valor asociado.

# Importamos la clase Enum desde el módulo enum
from enum import Enum

# Definimos una clase Weekday que hereda de Enum (es una enumeración)
class Weekday(Enum):
    MONDAY = 1        # Asociamos MONDAY con el valor 1
    TUESDAY = 2       # Asociamos TUESDAY con el valor 2
    WEDNESDAY = 3     # Y así sucesivamente...
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# Definimos una función llamada get_day que recibe un número entero
def get_day(number: int):
    # Convertimos ese número a su día correspondiente usando Weekday(number)
    # y accedemos a su nombre (por ejemplo Weekday(6) es SATURDAY)
    print(Weekday(number).name)

# Llamamos a la función get_day pasando 6 como argumento
get_day(6)




""" * DIFICULTAD EXTRA (opcional):
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
 */"""


# Importamos la clase Enum desde el módulo enum
from enum import Enum

# Definimos una enumeración llamada OrderStatus para los estados posibles de un pedido
class OrderStatus(Enum):
    PENDING = 1      # Pedido pendiente
    SHIPPED = 2      # Pedido enviado
    DELIVERED = 3    # Pedido entregado
    CANCELLED = 4    # Pedido cancelado

# Definimos la clase Order para representar un pedido
class Order:

    # Atributo de clase: todos los pedidos empiezan con estado PENDING
    status = OrderStatus.PENDING

    # Método constructor que recibe un id de pedido
    def __init__(self, id: int):
        # Guarda el id en la instancia
        self.id = id

    # Método para cambiar el estado a SHIPPED
    def ship(self):
        # Verifica si el pedido está en estado PENDING antes de enviarlo
        if self.status == OrderStatus.PENDING:
            # Cambia el estado a SHIPPED
            self.status = OrderStatus.SHIPPED
            # Muestra el estado actual
            self.display_status()
        else:
            # Si no está pendiente, muestra este mensaje
            print("El pedido ya se ha enviado o cancelado")

    # Método para cambiar el estado a DELIVERED
    def deliver(self):
        # Verifica si el pedido está en estado SHIPPED antes de entregarlo
        if self.status == OrderStatus.SHIPPED:
            # Cambia el estado a DELIVERED
            self.status = OrderStatus.DELIVERED
            # Muestra el estado actual
            self.display_status()
        else:
            # Si no ha sido enviado, no se puede entregar
            print("El pedido necesita ser enviado o cancelado")

    # Método para cancelar el pedido
    def cancel(self):
        # Verifica si el pedido NO está ya entregado
        if self.status != OrderStatus.DELIVERED:
            # Cambia el estado a CANCELLED
            self.status = OrderStatus.CANCELLED
            # Muestra el estado actual
            self.display_status()
        else:
            # Si ya fue entregado, no se puede cancelar
            print("El pedido no se puede cancelar porque ya ha sido entregado")

    # Método para mostrar el estado actual del pedido
    def display_status(self):
        print(f"El estado del pedido {self.id} es: {self.status.name}")

# Creamos un pedido con id 1
order_1 = Order(1)

# Mostramos su estado actual (debería ser PENDING)
order_1.display_status()

# Intentamos entregar el pedido sin enviarlo (esto no debería funcionar)
order_1.deliver()

# Enviamos el pedido (cambia de PENDING a SHIPPED)
order_1.ship()

# Ahora sí, lo entregamos (cambia de SHIPPED a DELIVERED)
order_1.deliver()

# Intentamos cancelar un pedido ya entregado (no debería permitirlo)
order_1.cancel()


""" Enum → para definir los estados posibles de un pedido.
Verificación de estado antes de permitir cambios, respetando un flujo lógico:
*Solo se puede enviar si está pendiente.
*Solo se puede entregar si está enviado.
*Solo se puede cancelar si no está entregado.
display_status() → muestra el estado actual con .name (el nombre del Enum)"""


