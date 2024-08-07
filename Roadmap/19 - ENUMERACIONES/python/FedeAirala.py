# #19 ENUMERACIONES

"""
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
"""
from enum import Enum

class days (Enum):
    Lunes = 1
    Martes = 2
    Miércoles = 3
    Jueves = 4
    Viernes = 5
    Sábado = 6
    Domingo = 7

days_list = [d for d in days]

for day in days_list:
    print (f"El día {days(day).value} es {day.name}")


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
 
"""
class Estado(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4
    
class Pedido ():
    
    def __init__(self,id, estado = Estado.PENDIENTE):
        self.id = id
        self.estado = estado
    
    def enviar(self):
        if self.estado == Estado.PENDIENTE:
            self.estado = Estado.ENVIADO
        else:
            print (f"El estado del pedido {self.id} se encuentra {self.estado.name} para poder enviar debe estar en {Estado.PENDIENTE.name}")
        
    def entregar(self):
        if self.estado == Estado.ENVIADO:
            self.estado = Estado.ENTREGADO
        else:
            print (f"El estado del pedido {self.id} se encuentra {self.estado.name} para poder entregar debe estar en {Estado.ENVIADO.name}")    
    
    def cancelar(self):
        if self.estado != Estado.ENTREGADO:
            self.estado = Estado.CANCELADO
        else:
            print ("El pedido ya fue entregado")
    
    def mostrar_estado(self):
        print (f"El estado del pedido {self.id} es {self.estado.name}")
        

pedido_1 = Pedido(1)
pedido_2 = Pedido(2)
pedido_1.enviar()
pedido_1.mostrar_estado()
pedido_2.mostrar_estado()
pedido_2.cancelar()
pedido_2.mostrar_estado()
pedido_3 = Pedido (3)
pedido_3.mostrar_estado()
pedido_3.entregar()


