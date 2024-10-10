from enum import Enum



"""
Ejercicio
"""

class Semana(Enum):

    LUNES=1
    MAERTES=2
    MIERCOLES=3
    JUEVES=4
    VIERNES=5
    SABADO=6
    DOMINGO=7

def dia(num_dia: int):
   print(Semana(num_dia).name)

dia(5)


"""
Extra
"""
class Estado(Enum):
    PENDIENTE= 1
    ENVIADO=2
    ENTREGADO=3
    CANCELADO=4

class  Pedido():
    estado= Estado.PENDIENTE

    def __init__(self, numero:int) -> None:
        self.numero= numero
        
    
    def enviar(self):
        if self.estado == Estado.PENDIENTE:
            self.estado= Estado.ENVIADO
            self.mostrar_estado()
        else:
            print("El pedido ya fue enviado o cancelado")

    def entregar(self):
        if self.estado == Estado.ENVIADO:
            self.estado= Estado.ENTREGADO
            self.mostrar_estado()
        else:
            print("El pedido tiene que ser enviado antes de entregarse")

    def cancelar(self):
        if self.estado != Estado.ENTREGADO:
            self.estado= Estado.CANCELADO
            self.mostrar_estado()
        else:
            print("El pedido ya fue entregado no se puede cancelar")

    def mostrar_estado(self):
        print(f"El el estado del pedido {self.numero} es {self.estado.name}")


pedido1=Pedido(1)
pedido1.mostrar_estado()
pedido1.entregar()
pedido1.enviar()
#pedido1.entregar()
pedido1.cancelar()
