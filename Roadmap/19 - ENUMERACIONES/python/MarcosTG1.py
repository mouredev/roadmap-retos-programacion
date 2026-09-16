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

class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

def asignar_dia(id: int) -> None:
    print(DiaSemana(id).name)

asignar_dia(4)

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
    CANCELADO = 0
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3

class Pedido():

    def __init__(self, id: int):
        self.id = id
        self.estado = Estado(1)
    
    def enviado(self) -> str:
        if self.estado.name == "PENDIENTE":
            self.estado = Estado(2)
            return self.estado.name
        else:
            print("Estado no actualizado, ya que el pedido no está pendiente.")

    def cancelado(self) -> str:
        self.estado = Estado(0)
        return self.estado.name
    
    def pendiente(self) -> str:
        self.estado = Estado(1)
        return self.estado.name
    
    def entregado(self) -> str:
        if self.estado.name == "ENVIADO":
            self.estado = Estado(3)
            return self.estado.name
        else:
            print("Estado no actualizado, ya que el pedido no ha sido enviado.")
    
    def show_status(self) -> None:
        print(f"El pedido se encuentra actualente en el siguiente estado: {self.estado.name.lower()}.")
        
        
class RegistroEntregas():

    def __init__(self):
        self.registro_entregas: set[int] = set()
    
    def add_id_entregado(self, pedido: Pedido) -> None:
        if pedido.estado == Estado.ENTREGADO:
            self.registro_entregas.add(pedido.id)
            print("Pedido añadido correctamente al registro.")
        else:
            print(f"Asegúrate de que el estado del pedido sea `entregado` en lugar de {pedido.estado.name.lower()}.")
    
    def show_ids_delivered(self) -> None:
        print(self.registro_entregas)


registro = RegistroEntregas()

pedido_1 = Pedido(878)
print(pedido_1.estado)

pedido_1.entregado()
    
pedido_1.enviado()
pedido_1.show_status()
pedido_1.entregado()
print(pedido_1.estado.name)
pedido_1.show_status()

pedido_2 = Pedido(777)
pedido_2.enviado()

registro.add_id_entregado(pedido_1)
registro.add_id_entregado(pedido_2)

registro.show_ids_delivered()


