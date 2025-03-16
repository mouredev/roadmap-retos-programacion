# Ejercicio:

from enum import Enum

class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

def obtener_dia(numero):
    dias = {
        1: DiaSemana.LUNES,
        2: DiaSemana.MARTES,
        3: DiaSemana.MIERCOLES,
        4: DiaSemana.JUEVES,
        5: DiaSemana.VIERNES,
        6: DiaSemana.SABADO,
        7: DiaSemana.DOMINGO
    }
    if numero in dias:
        return dias[numero].name
    else:
        return "Número inválido"

# Ejemplos de uso
print(obtener_dia(1))
print(obtener_dia(5))
print(obtener_dia(8))


# Dificultad extra:

from enum import Enum

class EstadoPedido(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Pedido:
    def __init__(self, id_pedido):
        self.id_pedido = id_pedido
        self.estado = EstadoPedido.PENDIENTE

    def enviar_pedido(self):
        if self.estado == EstadoPedido.PENDIENTE:
            self.estado = EstadoPedido.ENVIADO
            print(f"El pedido {self.id_pedido} ha sido enviado.")
        else:
            print(f"No se puede enviar el pedido {self.id_pedido} porque su estado actual es {self.estado.name}.")

    def cancelar_pedido(self):
        if self.estado == EstadoPedido.PENDIENTE or self.estado == EstadoPedido.ENVIADO:
            self.estado = EstadoPedido.CANCELADO
            print(f"El pedido {self.id_pedido} ha sido cancelado.")
        else:
            print(f"No se puede cancelar el pedido {self.id_pedido} porque su estado actual es {self.estado.name}.")

    def entregar_pedido(self):
        if self.estado == EstadoPedido.ENVIADO:
            self.estado = EstadoPedido.ENTREGADO
            print(f"El pedido {self.id_pedido} ha sido entregado.")
        else:
            print(f"No se puede entregar el pedido {self.id_pedido} porque su estado actual es {self.estado.name}.")

    def mostrar_estado(self):
        print(f"El pedido {self.id_pedido} tiene el estado: {self.estado.name}")

# Ejemplo de uso
pedido1 = Pedido("P001")
pedido1.mostrar_estado()  

pedido1.enviar_pedido()
pedido1.mostrar_estado()  

pedido1.entregar_pedido()
pedido1.mostrar_estado()  

pedido1.cancelar_pedido()  

pedido2 = Pedido("P002")
pedido2.cancelar_pedido()
pedido2.mostrar_estado()  
