from enum import Enum


class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7


def obtener_nombre_dia(numero):
    if 1 <= numero <= 7:
        return DiaSemana(numero).name.capitalize()
    else:
        return "Número de día no válido"


numero_dia = 6
print(f"El día {numero_dia} es {obtener_nombre_dia(numero_dia)}")


# Ejercicio extra


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
            print(f"Pedido {self.identificador} enviado.")

    def pedido_entregado(self):
        if self.estado == EstadoPedido.ENVIADO:
            self.estado = EstadoPedido.ENTREGADO
            print(f"Pedido {self.identificador} entregado.")

    def pedido_cancelado(self):
        if self.estado != EstadoPedido.ENTREGADO:
            self.estado = EstadoPedido.CANCELADO
            print(f"Pedido {self.identificador} cancelado.")

    def mostrar_estado(self):
        estado_descripcion = {
            EstadoPedido.PENDIENTE: "El pedido está pendiente de envío.",
            EstadoPedido.ENVIADO: "El pedido ha sido enviado pero aún no ha sido entregado.",
            EstadoPedido.ENTREGADO: "El pedido ha sido entregado con éxito.",
            EstadoPedido.CANCELADO: "El pedido ha sido cancelado.",
        }
        print(
            f"Estado del pedido {self.identificador}: {estado_descripcion[self.estado]}"
        )


# Ejemplo de uso
pedido1 = Pedido("0001")
pedido1.mostrar_estado()
pedido1.pedido_enviado()
pedido1.mostrar_estado()
pedido1.pedido_entregado()
pedido1.mostrar_estado()

pedido2 = Pedido("0002")
pedido2.mostrar_estado()
pedido2.pedido_cancelado()
pedido2.mostrar_estado()
