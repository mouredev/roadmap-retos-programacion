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

def obtener_nombre_dia(numero):
    try:
        return DiaSemana(numero).name
    except ValueError:
        return "Número inválido. Por favor, introduce un número del 1 al 7."

# Ejemplo de uso
for i in range(1, 8):
    print(f"{i}: {obtener_nombre_dia(i)}")


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

from enum import Enum

class EstadoPedido(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Pedido:
    def __init__(self, identificador):
        self.identificador = identificador
        self.estado = EstadoPedido.PENDIENTE

    def enviar(self):
        if self.estado == EstadoPedido.PENDIENTE:
            self.estado = EstadoPedido.ENVIADO
        else:
            print("El pedido no puede ser enviado en su estado actual.")

    def cancelar(self):
        if self.estado in [EstadoPedido.PENDIENTE, EstadoPedido.ENVIADO]:
            self.estado = EstadoPedido.CANCELADO
        else:
            print("El pedido no puede ser cancelado en su estado actual.")

    def entregar(self):
        if self.estado == EstadoPedido.ENVIADO:
            self.estado = EstadoPedido.ENTREGADO
        else:
            print("El pedido no puede ser entregado en su estado actual.")

    def mostrar_estado(self):
        estados_descriptivos = {
            EstadoPedido.PENDIENTE: "El pedido está pendiente.",
            EstadoPedido.ENVIADO: "El pedido ha sido enviado.",
            EstadoPedido.ENTREGADO: "El pedido ha sido entregado.",
            EstadoPedido.CANCELADO: "El pedido ha sido cancelado."
        }
        return estados_descriptivos[self.estado]

def mostrar_menu():
    print("\nMenú de Gestión de Pedidos")
    print("1. Crear pedido")
    print("2. Enviar pedido")
    print("3. Cancelar pedido")
    print("4. Entregar pedido")
    print("5. Mostrar estado del pedido")
    print("6. Salir")

def main():
    pedidos = {}
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            identificador = input("Introduce el identificador del pedido: ")
            pedidos[identificador] = Pedido(identificador)
            print(f"Pedido {identificador} creado.")
        elif opcion == '2':
            identificador = input("Introduce el identificador del pedido a enviar: ")
            if identificador in pedidos:
                pedidos[identificador].enviar()
                print(f"Pedido {identificador} enviado.")
            else:
                print("Pedido no encontrado.")
        elif opcion == '3':
            identificador = input("Introduce el identificador del pedido a cancelar: ")
            if identificador in pedidos:
                pedidos[identificador].cancelar()
                print(f"Pedido {identificador} cancelado.")
            else:
                print("Pedido no encontrado.")
        elif opcion == '4':
            identificador = input("Introduce el identificador del pedido a entregar: ")
            if identificador in pedidos:
                pedidos[identificador].entregar()
                print(f"Pedido {identificador} entregado.")
            else:
                print("Pedido no encontrado.")
        elif opcion == '5':
            identificador = input("Introduce el identificador del pedido: ")
            if identificador in pedidos:
                print(pedidos[identificador].mostrar_estado())
            else:
                print("Pedido no encontrado.")
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

if __name__ == "__main__":
    main()
