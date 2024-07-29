#19 - ENUMERACIONES

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

# Importamos Enum del módulo enum para crear enumeraciones.
from enum import Enum


# Definimos una clase enum para representar los días de la semana.
class Dias(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

# Función para obtener el nombre del día de la semana dado un número entero.
def dia_de_la_semana(dia: int) -> str:
    if 1 <= dia <=7:  # Verifica si el día está en el rango válido.
        return Dias(dia).name  # Devuelve el nombre del día.

    return "Ese dia de la semana no existe"  # Mensaje de error si el día no es válido.

# Extra
# Definimos una clase enum para representar el estado de un pedido.
class Estado(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

# Clase para representar un pedido con su estado.
class Pedido:
    def __init__(self, identificador: int) -> None:
        self.identificador = identificador  # Identificador del pedido.
        self.estado = Estado.PENDIENTE  # Estado inicial del pedido.

    # Método para cambiar el estado a ENVIADO.
    def enviado(self):
        if self.estado == Estado.PENDIENTE:
            print(self.estado_actual())
            self.estado = Estado.ENVIADO
        else:
            print("El producto ya se está enviando")

    # Método para cambiar el estado a ENTREGADO.
    def entregado(self):
        if self.estado == Estado.ENVIADO:
            print(self.estado_actual())
            self.estado = Estado.ENTREGADO
        else:
            print("El pedido aún no ha sido enviado")

    # Método para cambiar el estado a CANCELADO.
    def cancelado(self):
        if self.estado == Estado.ENTREGADO:
            print(self.estado_actual())
        elif self.estado == Estado.CANCELADO:
            print(self.estado_actual())
        self.estado = Estado.PENDIENTE

    # Método para obtener una descripción del estado actual del pedido.
    def estado_actual(self):
        descripciones: dict = {
            Estado.PENDIENTE: f"El pedido {self.identificador} está pendiente",
            Estado.ENVIADO: f"El pedido {self.identificador} está siendo enviado",
            Estado.ENTREGADO: f"El pedido {self.identificador} fue entregado",
            Estado.CANCELADO: f"El pedido {self.identificador} fue cancelado"
        }
        return descripciones[self.estado]

# Se muestra la funcion del inicio
print(dia_de_la_semana(3))

# Crear instancias de Pedido.
pedido1 = Pedido(1)
pedido2 = Pedido(2)

# Cambiar y mostrar estados de los pedidos.
pedido1.enviado()
pedido2.enviado()

pedido1.entregado()
pedido1.estado = Estado.CANCELADO
pedido2.entregado()

pedido1.cancelado()
pedido2.cancelado()
