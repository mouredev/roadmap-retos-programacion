"""
19 - ENUMERACIONES

Autor de la solución: Oriaj3	

Teoría: 

Las enumeraciones son una forma de representar un conjunto de valores constantes
con nombres descriptivos. En Python, las enumeraciones se pueden crear utilizando
la clase Enum del módulo enum. Las enumeraciones son útiles para representar
valores que no cambian durante la ejecución del programa, como los días de la
semana, los meses del año, los colores, etc.

"""

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
from enum import Enum

class Weekday(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

def get_weekday(num: int):
    for day in Weekday:
        if day.value == num:
            return day.name
    return "Error"    
print(get_weekday(5))

"""
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

class Estado(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Pedido():
    siguiente_id: int=1 
    estado: Estado= Estado.PENDIENTE
    
    def __init__(self):
        self.id = Pedido.siguiente_id
        Pedido.siguiente_id += 1

    def enviar(self):
        self.estado = Estado.ENVIADO
        print(f"Enviando pedido {self.id}")

    def entregar(self):
        if self.estado == Estado.ENVIADO:
            self.estado = Estado.ENTREGADO
            print(f"Entregado pedido {self.id}")
        else:
            print(f"No se puede entregar el pedido {self.id}")

    def cancelar(self):
        if self.estado == Estado.ENTREGADO:
            print(f"No se puede cancelar un pedido entregado, id: {self.id}")
        else:
            self.estado = Estado.CANCELADO
            print(f"Cancelado el pedido {self.id}")
        
    def get_estado(self):
        print(f"El estado del pedido {self.id} es {self.estado.name}")


#Ejemplo de uso
#Pedido1
pedido1 = Pedido()
pedido1.enviar()
pedido1.entregar()
pedido1.cancelar()
pedido1.get_estado() 

#Pedido2
pedido2 = Pedido()
pedido2.enviar()
pedido2.cancelar()
pedido2.get_estado()

#Pedido3
pedido3 = Pedido()
pedido3.entregar()
pedido3.get_estado()

#Pedido4
pedido4 = Pedido()
pedido4.cancelar()
pedido4.get_estado()

#Pedido5
pedido5 = Pedido()
pedido5.enviar()
pedido5.entregar()
pedido5.get_estado()
