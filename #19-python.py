'''
* EJERCICIO:
* Empleando tu lenguaje, explora la definición del tipo de dato
* que sirva para definir enumeraciones (Enum).
* Crea un Enum que represente los días de la semana del lunes
* al domingo, en ese orden. Con ese enumerado, crea una operación
* que muestre el nombre del día de la semana dependiendo del número entero
* utilizado (del 1 al 7).
'''
from enum import Enum
print ("*"*60)

class Dias(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

def semana(dia:int):
    print(Dias(dia).name)

semana(3)
semana(7)

print ("*"*60)


'''
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
- Implementa una función para mostrar un texto descriptivo según el estado actual.
* - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
'''
class Estado(Enum):
    PENDIENTE = 1
    ENVIADO = 2 
    ENTREGADO = 3 
    CANCELADO = 4


class Pedido:

    estado = Estado.PENDIENTE

    def __init__(self, ident: int): 
        self.ident = ident

    def enviar(self):
        if self.estado == Estado.PENDIENTE:
            self.estado = Estado.ENVIADO
        else:
            print(f"El pedido {self.ident} no se puede enviar si no está pendiente")    
        print(self.mostrar_estado())
    def entregar(self):
        if self.estado == Estado.ENVIADO:
            self.estado = Estado.ENTREGADO
        else:
            print(f"El pedido {self.ident} no se puede entregar si no está enviado") 
        print(self.mostrar_estado())
    def cancelar(self):
        if self.estado == Estado.ENTREGADO:
            self.estado = Estado.CANCELADO
        else:
            print(f"El pedido {self.ident} no se puede cancelar si no está entregado")    
        print(self.mostrar_estado())

    def mostrar_estado(self):
        print(f"El pedido {self.ident} esta en estado {self.estado.name}\n" + "-"*35)               
        return ""                

#Pruebas con dos pedidos
Orden = Pedido(1)
Orden.enviar()
Orden.entregar()
Orden.cancelar()

Orden = Pedido(2)
Orden.entregar()
Orden.cancelar()
Orden.enviar()
Orden.entregar()
Orden.enviar()
Orden.cancelar()
