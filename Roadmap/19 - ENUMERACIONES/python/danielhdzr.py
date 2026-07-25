# #19 ENUMERACIONES
#### Dificultad: Media | Publicación: 06/05/24 | Corrección: 13/05/24

## Ejercicio

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

from enum import Enum

class weekday(Enum):
    LUNES = 1
    MARTES  = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

def get_day(number: int):
    print(weekday(number).name)

get_day(1)
get_day(5)
print("**********************************")

# Estado del pedido 
class estado(Enum):
    PENDIENTE = 1  # name.value
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

# Clase para la orden
class Order:
    # Estado predeterminado
    status_envio = estado.PENDIENTE

    def __init__(self, id) -> None:
        self.id = id

    def ship(self):
        if self.status_envio == estado.PENDIENTE:  # si status de envio es pendiente cambia 
            self.status_envio = estado.ENVIADO  # cambia a enviado
            self.display_status()  # muestra el estado del pedido
        else:  # si no es pendiente, imprime mensaje
            print("El pedido ya ha sido enviado o cancelado")

    def deliver(self):
        if self.status_envio == estado.ENVIADO:
            self.status_envio = estado.ENTREGADO
            self.display_status()
        else:
            print("El pedido necesita ser enviado antes de entregarse.")

    def cancel(self):
        if self.status_envio != estado.ENTREGADO:
            self.status_envio = estado.CANCELADO
            self.display_status()
        else:
            print("El pedido no se puede cancelar ya que ya se ha entregado.")

    def display_status(self):
        print(f"El estado del pedido {self.id} es {self.status_envio.name}")


order_1 = Order(1)
order_1.display_status()
order_1.deliver()
order_1.ship()
order_1.deliver()
order_1.cancel()