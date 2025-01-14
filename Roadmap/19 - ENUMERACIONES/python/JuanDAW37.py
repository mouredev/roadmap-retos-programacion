"""* Empleando tu lenguaje, explora la definición del tipo de dato
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
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. """
from enum import Enum

# Definición como clase
class DiasSem(Enum):
    lunes = 1
    martes = 2
    miercoles = 3
    jueves = 4
    viernes = 5
    sabado = 6
    domingo = 7

# Otra forma de crearla
diasSem = Enum('diasSem', ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo'])

# Crea una operación que muestre el nombre del día de la semana dependiendo del número entero utilizado (del 1 al 7).
num_Dia = 0
while True:
    num_Dia = int(input('Escribe un número de día de la semana 1 - 7-> '))
    if num_Dia >= 1 & num_Dia <= 7:
        break
print(diasSem(num_Dia).name)

#EXTRA
class Estado(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Pedido():
    def __init__(self, id_pedido, estado=Estado.PENDIENTE):
        self.id_pedido = id_pedido
        self.estado = estado
    
    def enviarPedido(self):
        if self.estado == Estado.PENDIENTE:
            self.estado = Estado.ENVIADO
        else:
            print(f"El pedido {self.id_pedido}, ya ha sido enviado o cancelado")
    
    def entregarPedido(self):
        if self.estado == Estado.ENVIADO:
            self.estado = Estado.ENTREGADO
        else:
            print(f"El pedido {self.id_pedido}, ya ha sido entregado o cancelado")
        
    def cancelarPedido(self):
        if self.estado != Estado.ENTREGADO:
            self.estado = Estado.CANCELADO
        else:
            print(f"El pedido {self.id_pedido}, no se puede cancelar, ya ha sido entregado")
        
    def verEstado(self):
        print(f'El pedido número {self.id_pedido} está: {self.estado.name}')        

pedido1 = Pedido(1)
pedido1.verEstado()

pedido1.enviarPedido()
pedido1.verEstado()

pedido1.entregarPedido()
pedido1.verEstado()

pedido1.cancelarPedido()
pedido1.verEstado()