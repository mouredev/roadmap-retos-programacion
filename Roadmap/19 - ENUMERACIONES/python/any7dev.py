""" /*
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
 */ """

#EJERCICIO
from enum import Enum

class Dias(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SÁBADO = 6
    DOMINGO = 7

def mostrar_dia(numero):
    print(Dias(numero).name)

mostrar_dia(2)
mostrar_dia(7)

#DIFICULTAD EXTRA
class Estados(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 0

class Pedido:

    estado = Estados.PENDIENTE

    def __init__(self, id):
        self.id = id
        
    def enviar(self):
        if (self.estado is not Estados.CANCELADO) and (self.estado is not Estados.ENTREGADO) and (self.estado is not Estados.ENVIADO):
            self.estado = Estados.ENVIADO
            print(f"Pedido {self.id} enviado")
        else:
            print(f"No se puede enviar el pedido {self.id}, su estado es {self.mostrar()}")

    def cancelar(self):
        if (self.estado is not Estados.CANCELADO) and (self.estado is not Estados.ENTREGADO):
            self.estado = Estados.CANCELADO
            print(f"Pedido {self.id} cancelado")
        else:
            print(f"No se puede cancelar el pedido {self.id}, su estado es {self.mostrar()}")

    def entregar(self):
        if (self.estado is not Estados.CANCELADO) and (self.estado is not Estados.ENTREGADO):
            self.estado = Estados.ENTREGADO
            print(f"Pedido {self.id} entregado")
        else:
            print(f"No se puede entregar el pedido {self.id}, su estado es {self.mostrar()}")

    def mostrar(self):
        return self.estado.name

pedido1 = Pedido("001")
pedido1.cancelar()

pedido2 = Pedido("002")
pedido2.enviar()

pedido3 = Pedido("003")
pedido3.entregar()
pedido3.cancelar()

pedido4 = Pedido("004")
pedido4.cancelar()
pedido4.enviar()

pedido5 = Pedido("005")
pedido5.enviar()
pedido5.entregar()