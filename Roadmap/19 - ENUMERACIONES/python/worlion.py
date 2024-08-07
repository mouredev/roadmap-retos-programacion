from enum import Enum

"""
    EJERCICIO: Enumeraciones
"""

# Enumeración de los días de la semana
class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

def dia_semana(numero):
    if numero < 1 or numero > 7:
        return "Día no válido"
    return DiaSemana(numero).name

print(f"Dia 1 : {dia_semana(1)} ") # LUNES
print(f"Dia 7 : {dia_semana(7)} ") # DOMINGO
print(f"Dia 8 : {dia_semana(8)} ") # Día no válido
print(f"Dia 0 : {dia_semana(0)} ") # Día no válido

"""
    DIFICULTAD EXTRA (opcional): Pedidos
"""

print("\n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n")

class EstadoPedido(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4
    
class Pedido:
    def __init__(self, identificador):
        self.identificador = identificador
        self.estado = EstadoPedido.PENDIENTE

    def pedido_enviado(self):
        if self.estado == EstadoPedido.PENDIENTE:
            self.estado = EstadoPedido.ENVIADO
        else:
            print("No se puede enviar el pedido")

    def pedido_cancelado(self):
        if self.estado == EstadoPedido.PENDIENTE:
            self.estado = EstadoPedido.CANCELADO
        else:
            print("No se puede cancelar el pedido")

    def pedido_entregado(self):
        if self.estado == EstadoPedido.ENVIADO:
            self.estado = EstadoPedido.ENTREGADO
        else:
            print("No se puede entregar el pedido")

    def mostrar_estado(self):
        return f"Pedido {self.identificador} : {self.estado.name}"
    
    def __str__(self):
        return self.mostrar_estado()

pedido1 = Pedido(1)
pedido2 = Pedido(2)
pedido3 = Pedido(3)

print(pedido1)
pedido1.pedido_enviado()
print(pedido1)
pedido1.pedido_entregado()
print(pedido1)
pedido1.pedido_cancelado()
print(pedido1)

print(pedido2)
pedido2.pedido_entregado()
print(pedido2)
pedido2.pedido_cancelado()
print(pedido2)

print(pedido3)
pedido3.pedido_enviado()
print(pedido3)
pedido3.pedido_entregado()
print(pedido3)
pedido3.pedido_cancelado()
print(pedido3)

