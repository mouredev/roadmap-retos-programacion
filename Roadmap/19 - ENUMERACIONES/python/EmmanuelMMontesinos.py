"""/*
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 */"""

# Enumeracion
from enum import Enum

class Dias(Enum):
    lunes = 1
    martes = 2
    miercoles = 3
    jueves = 4
    viernes = 5
    sabado = 6
    domingo = 7

    def numero_a_dia(self,num:int):
        try:
            print(f"El {num} es {self(num).name.title()}\n")
        except ValueError as e:
            print(f"{num} no esta dentro del rango (1/7)\n")

# Pruebas

Dias.numero_a_dia(Dias,1)

'''
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
'''

# Pedidos
class Pedidos:
    
    # Estados de los pedidos
    class Estados_Pedidos(Enum):
        PENDIENTE = "Pendiente"
        ENVIADO = "Enviado"
        ENTREGADO = "Entregado"
        CANCELADO = "Cancelado"

    total_pedidos = 0

    def __init__(self) -> None:

        Pedidos.total_pedidos += 1
        self.identificador = Pedidos.total_pedidos
        self.estado = Pedidos.Estados_Pedidos.PENDIENTE

    def info(self):
        print(f"Identificador: {self.identificador}\nEstado: {self.estado.value}\nPedidos Totales: {Pedidos.total_pedidos}\n")

    # Metodo para cambiar de estado dependiendo de su estado actual
    def cambiar_estado(self,cambio):

        if cambio.lower() == "enviado":

            if self.estado == Pedidos.Estados_Pedidos.PENDIENTE:

                print(f"Cambiando estado de {self.estado.value} a {cambio.title()}")
                self.estado = Pedidos.Estados_Pedidos.ENVIADO
                print("Cambio realizado con exito\n")

            else:

                print(f"No se puede cambiar de estado de {self.estado.value} a {cambio}\n")

        elif cambio.lower() == "entregado":

            if self.estado == Pedidos.Estados_Pedidos.ENVIADO:

                print(f"Cambiando estado de {self.estado.value} a {cambio.title()}")
                self.estado = Pedidos.Estados_Pedidos.ENTREGADO
                print("Cambio realizado con exito\n")

            else:

                print(f"No se puede cambiar de estado de {self.estado.value} a {cambio}\n")


        elif cambio.lower() == "cancelado":

            if self.estado != Pedidos.Estados_Pedidos.CANCELADO:

                print(f"Cambiando estado de {self.estado.value} a {cambio.title()}")
                self.estado = Pedidos.Estados_Pedidos.CANCELADO
                print("Cambio realizado con exito\n")

            else:

                print(f"No se puede cambiar de estado de {self.estado.value} a {cambio}\n")
        self.info()

# Pruebas
pedido_1 = Pedidos()
pedido_2 = Pedidos()
pedido_3 = Pedidos()

pedido_1.cambiar_estado("enviado")
pedido_2.cambiar_estado("entregado")
pedido_3.cambiar_estado("cancelado")

pedido_1.info()
pedido_2.info()
pedido_3.info()