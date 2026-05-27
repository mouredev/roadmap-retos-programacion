 
from enum import Enum

class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

def que_dia_semana(numero):
        print(DiaSemana(numero).name)
        #print(DiaSemana(numero).value)

que_dia_semana(4)

# DIFICULTAD EXTRA:

class Estado(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Pedido:
    
    estado = Estado.PENDIENTE
    
    def __init__(self, id):
        self.id = id
    
    def envio(self):
        if self.estado == Estado.PENDIENTE:
            self.estado = Estado.ENVIADO
            self.estado_pedido()
        else:
             print("Error estado envio, no puede enviarse si el estado no es pendiente")
    
    def entrega(self):
        if self.estado == Estado.ENVIADO:
            self.estado = Estado.ENTREGADO
            self.estado_pedido()
        else:
             print("Error estado entregado, no puede entregarse si no se ha enviado")
    
    def cancelar(self):
        if self.estado != Estado.ENTREGADO:
            self.estado = Estado.CANCELADO
            self.estado_pedido()
        else:
            print("Error estado cancelado, no puede cancelarse si se ha entregado")

    def estado_pedido(self):
        print(f"El pedido {self.id} se encuentra {self.estado.name}") 
        
                                    
pedido1 = Pedido(1)
pedido2 = Pedido(2)
pedido3 = Pedido(3)
pedido4 = Pedido(4)

pedido1.estado_pedido()
pedido1.envio()
pedido1.entrega()
pedido1.cancelar()

pedido2.estado_pedido()
pedido3.estado_pedido()
pedido4.estado_pedido()
pedido2.envio()
pedido2.entrega()
pedido3.cancelar()
pedido4.envio()
pedido4.cancelar()