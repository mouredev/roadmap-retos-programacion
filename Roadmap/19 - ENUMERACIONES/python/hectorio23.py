# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23 
from enum import Enum

class EstadoPedido(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

# Clase Pedido
class Pedido:
    def __init__(self, _id):
        self.id = _id
        self.estado = EstadoPedido.PENDIENTE

    #Metodo para marcar el pedido como enviado
    def marcar_enviado(self):
        if self.estado == EstadoPedido.PENDIENTE:
            self.estado = EstadoPedido.ENVIADO
            print(f"El pedido con ID { self.id } ha sido enviado.")
        else:
            print(f"El pedido con ID { self.id } no se puede enviar en su estado actual.")

    #Metodo para marcar el pedido como entregado
    def marcar_entregado(self):
        if self.estado == EstadoPedido.ENVIADO:
            self.estado = EstadoPedido.ENTREGADO
            print(f"El pedido con ID { self.id } ha sido entregado.")
        else:
            print(f"El pedido con ID { self.id } no se puede entregar en su estado actual.")

    # Función para cancelar el pedido
    def cancelar_pedido(self):
        if self.estado != EstadoPedido.CANCELADO:
            self.estado = EstadoPedido.CANCELADO
            print(f"El pedido con ID { self.id } ha sido cancelado.")
        else:
            print(f"El pedido con ID { self.id } ya está cancelado.")

    # Función para mostrar el estado del pedido
    def mostrar_estado(self):
        estado_str = {
            EstadoPedido.PENDIENTE: "Pendiente",
            EstadoPedido.ENVIADO: "Enviado",
            EstadoPedido.ENTREGADO: "Entregado",
            EstadoPedido.CANCELADO: "Cancelado"
        }
        print(f"Estado del pedido con ID { self.id }: { estado_str[self.estado] }")

# Definición del Enum para los días de la semana
class Week(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

# Función para mostrar el nombre del día de la semana
def nombre_dia_semana(numero_dia):
    try:
        dia = Week(numero_dia)
        return dia.name.capitalize()  # Devuelve el nombre del día con la primera letra mayúscula
    except ValueError:
        return "Número de día inválido"

# Ejemplo de uso
print("************ EJERCICIO ***************")

day = 4
print(f"El día { day } es: {nombre_dia_semana(day)}")

print("\n************ EJERCICIO EXTRA ***************")

# Crear pedidos
pedido1 = Pedido(1)
pedido2 = Pedido(2)

# Mostrar el estado inicial de los pedidos
pedido1.mostrar_estado()
pedido2.mostrar_estado()

# Interactuar con los pedidos
pedido1.marcar_enviado()
pedido2.marcar_enviado()
pedido1.marcar_entregado()
pedido2.cancelar_pedido()

# Mostrar el estado final de los pedidos
pedido1.mostrar_estado()
pedido2.mostrar_estado()

