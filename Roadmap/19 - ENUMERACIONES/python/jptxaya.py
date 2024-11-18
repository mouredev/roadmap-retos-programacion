# /*
#  * EJERCICIO:
#  * Empleando tu lenguaje, explora la definición del tipo de dato
#  * que sirva para definir enumeraciones (Enum).
#  * Crea un Enum que represente los días de la semana del lunes
#  * al domingo, en ese orden. Con ese enumerado, crea una operación
#  * que muestre el nombre del día de la semana dependiendo del número entero
#  * utilizado (del 1 al 7).
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un pequeño sistema de gestión del estado de pedidos.
#  * Implementa una clase que defina un pedido con las siguientes características:
#  * - El pedido tiene un identificador y un estado.
#  * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
#  * - Implementa las funciones que sirvan para modificar el estado:
#  *   - Pedido enviado
#  *   - Pedido cancelado
#  *   - Pedido entregado
#  *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
#  * - Implementa una función para mostrar un texto descriptivo según el estado actual.
#  * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
#  */

dia_semana = {1:"Lunes",
              2:"Martes",
              3:"Miercoles",
              4:"Jueves",
              5:"Viernes",
              6:"Sabado",
              7:"Domingo"}

def dia_semanal(dia):
    return dia_semana.get(dia)

print(dia_semanal(4))

print("Dificultad Extra")

class Pedido:

    id = ""
    order_Status = {1:"PENDIENTE",
                    2:"ENVIADO",
                    3:"ENTREGADO",
                    4:"CANCELADO"}
    
    def __init__(self, param_id) -> None:
        self.id = param_id
        self.status = 1
    
    def enviado(self) -> None:
        if self.status == 1 and self.status != 4:
            self.status = 2
    
    def entregado(self) -> None:
        if self.status == 2 and self.status != 4:
            self.status = 3
    
    def cancelado(self) -> None:
        if self.status != 3:
            self.status = 4
    
    def estado(self):
        return (self.order_Status.get(self.status))
    
    def str_pedido(self):
        print(f"Pedido: {self.id} Estado: {self.estado()}")
    
pedido1 = Pedido("id01")
pedido2 = Pedido("id02")
pedido1.str_pedido()
pedido2.str_pedido()
print("Enviando pedido1, Cancelando pedido2")
pedido1.enviado()
pedido2.cancelado()
pedido1.str_pedido()
pedido2.str_pedido()
print("Entregado pedido1, Entregado pedido2")
pedido1.entregado()
pedido2.entregado()
pedido1.str_pedido()
pedido2.str_pedido()
print("Cancelado pedido1, Entregado pedido2")
pedido1.cancelado
pedido2.entregado()
pedido1.str_pedido()
pedido2.str_pedido()

 
        