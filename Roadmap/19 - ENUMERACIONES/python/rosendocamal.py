"""
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
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
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
"""

from enum import Enum

class Day(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

days = Enum('Day', [('LUNES', 1), ('MARTES', 2), ('MIERCOLES', 3), ('JUEVES', 4), ('VIERNES', 5), ('SABADO',6), ('DOMINGO',7)])

print(Day.LUNES.name, Day.LUNES.value)

print(days.LUNES.name, days.LUNES.value)

def obtener_weekday(day: int):
    return (Day(day).name)

print(obtener_weekday(5))


#### EXTRA ####

class EstadoPedido(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Pedido():
    def __init__(self, id: int, status: int):
        self.identificador = id
        self.estado = status

    def __str__(self):
        return f"PEDIDO NO. {self.identificador}\nESTADO: {EstadoPedido(self.estado).name}"

class SistemaGestorEstadoPedido():
    def __init__(self):
        self.pedidos: dict[int, Pedido] = {}

    def crear_pedido(self, id: int, status: int):
        if id in self.pedidos.keys():
            print("Pedido ya existe, consulta su estado.")
        else:
            estado_pendiente = EstadoPedido.PENDIENTE == status
            if estado_pendiente:
                self.pedidos[id] = Pedido(id, status)
            else:
                print(f"Los nuevos paquetes solo admiten el estado {EstadoPedido.PENDIENTE.name}")

    def enviar_pedido(self, id: int):
        if id in self.pedidos.keys():
            pedido = self.pedidos[id]
            está_pendiente = EstadoPedido.PENDIENTE == pedido.estado
            if está_pendiente:
                pedido.estado = EstadoPedido.ENVIADO
                print(f"El pedido {id} ha sido enviado.")
            else:
                print(f"El pedido {id} no se puede enviar si está cancelado o entregado, o si está en curso el envío.")
        else:
            print(f"Pedido {id} no existe.")

    def cancelar_pedido(self, id: int):
        if id in self.pedidos.keys():
            pedido = self.pedidos[id]
            no_está_entregado = EstadoPedido.ENTREGADO != pedido.estado
            if no_está_entregado:
                pedido.estado = EstadoPedido.CANCELADO
                print(f"El pedido {id} se canceló.")
            else:
                print(f"El pedido {id} no se puede cancelar porque ya fue entregado.")
        else:
            print(f"Pedido {id} no existe.")

    def entregar_pedido(self, id: int):
        if id in self.pedidos.keys():
            pedido = self.pedidos[id]
            está_en_envío = EstadoPedido.ENVIADO == pedido.estado
            if está_en_envío:
                pedido.estado = EstadoPedido.ENTREGADO
                print(f"El pedido {id} ha sido entregado.")
            else:
                print(f"El pedido {id} no se puede entregar por estado {EstadoPedido.PENDIENTE.name} o {EstadoPedido.CANCELADO.name}")
        else:
            print(f"Pedido {id} no existe.")


    def consultar_pedido(self, id: int):
        if id in self.pedidos.keys():
            print(self.pedidos[id])
        else:
            print("No existe el pedido.")

sistema_armazon = SistemaGestorEstadoPedido()

print(); print(); print()

# Crear pedidos
sistema_armazon.crear_pedido(1, EstadoPedido.PENDIENTE)
sistema_armazon.crear_pedido(2, EstadoPedido.PENDIENTE)
sistema_armazon.crear_pedido(3, EstadoPedido.PENDIENTE)
sistema_armazon.crear_pedido(4, EstadoPedido.PENDIENTE)
sistema_armazon.crear_pedido(5, EstadoPedido.PENDIENTE)
sistema_armazon.crear_pedido(6, EstadoPedido.PENDIENTE)
print()

# Consultar pedidos
sistema_armazon.consultar_pedido(1)
sistema_armazon.consultar_pedido(15)
sistema_armazon.consultar_pedido(2)
sistema_armazon.consultar_pedido(14)
sistema_armazon.consultar_pedido(3)
sistema_armazon.consultar_pedido(13)
sistema_armazon.consultar_pedido(4)
sistema_armazon.consultar_pedido(12)
sistema_armazon.consultar_pedido(5)
sistema_armazon.consultar_pedido(11)
sistema_armazon.consultar_pedido(6)
print()

# Cancelar 3 pedidos y enviar 3 pedidos
sistema_armazon.cancelar_pedido(1)
sistema_armazon.cancelar_pedido(3)
sistema_armazon.cancelar_pedido(5)
sistema_armazon.enviar_pedido(2)
sistema_armazon.enviar_pedido(4)
sistema_armazon.enviar_pedido(6)
print()

# Consultar pedidos
sistema_armazon.consultar_pedido(1)
sistema_armazon.consultar_pedido(2)
sistema_armazon.consultar_pedido(3)
sistema_armazon.consultar_pedido(4)
sistema_armazon.consultar_pedido(5)
sistema_armazon.consultar_pedido(6)
print()

# Enviar 3 pedidos, cancelar un envío y entregar 2 pedidos
sistema_armazon.enviar_pedido(1)
sistema_armazon.enviar_pedido(3)
sistema_armazon.enviar_pedido(2)
sistema_armazon.cancelar_pedido(2)
sistema_armazon.entregar_pedido(4)
sistema_armazon.entregar_pedido(6)
print()

# Consultar pedidos
sistema_armazon.consultar_pedido(1)
sistema_armazon.consultar_pedido(2)
sistema_armazon.consultar_pedido(3)
sistema_armazon.consultar_pedido(4)
sistema_armazon.consultar_pedido(5)
sistema_armazon.consultar_pedido(6)
print()

# Entregar 4 pedidos, cancelar 2 entregados
sistema_armazon.entregar_pedido(2)
sistema_armazon.entregar_pedido(4)
sistema_armazon.entregar_pedido(6)
sistema_armazon.entregar_pedido(11)
sistema_armazon.cancelar_pedido(4)
sistema_armazon.cancelar_pedido(6)