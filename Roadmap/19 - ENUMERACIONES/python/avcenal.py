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
from time import sleep

class Weekdays(Enum):
    Lunes = 1
    Martes = 2
    Miércoles = 3
    Jueves = 4
    Viernes = 5
    Sábado = 6
    Domingo = 7

def find_weekday(num):
    print(f"El día de la semana correspondiente al {num} es el {Weekdays(num).name}")

while True:
    number = int(input("Introduce un número del 1 al 7: "))
    if number > 7 or number < 1:
        print ("El número ha de ser mayor que 1 y menor que 7")
    else:
        find_weekday(number)
        break

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

class Status(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Order():
    def __init__(self,id): #se inicializa un pedido directamente como pendiente
        self.id = id
        self.status = Status.PENDIENTE

    def check_id(self,num):
        if int(num) == int(self.id):
            return True
        else:
            return False

    def show_order(self):
        print(f"NÚMERO DE PEDIDO: {self.id}")
        print(f"ESTADO: {self.status.name}")
        print("\n")
    
    def send_order(self):
        if self.status == Status.CANCELADO:
            print("El pedido no puede ser enviado porque está cancelado")
        elif self.status == Status.ENTREGADO:
            print("El pedido no puede ser enviado porque ya está entregado")
        elif self.status == Status.ENVIADO:
            print("El pedido ya ha sido enviado previamente")
        else:
            self.status = Status.ENVIADO
            print(f"Pedido {self.id} ENVIADO")
        print("\n")

    def cancel_order(self):
        if self.status == Status.ENVIADO:
            print("El pedido no puede ser cancelado porque ya se ha enviado")
        elif self.status == Status.ENTREGADO: #or self.status == Status.ENVIADO:
            print("El pedido no se puede cancelar porque ya está entregado")
        elif self.status == Status.CANCELADO:
            print("El pedido ya ha sido cancelado anteriormente")
        else:
            self.status = Status.CANCELADO
            print(f"Pedido {self.id} CANCELADO")
        print("\n")

    def order_delivered(self):
        if self.status == Status.CANCELADO:
            print("El pedido no se puede entregar porque está cancelado")
        elif self.status == Status.ENTREGADO:
            print("El pedido ya ha sido entregado anteriormente")
        elif self.status != Status.ENVIADO:
            print("El pedido no ha sido enviado aún, no se puede marcar como entregado")
        else:
            self.status = Status.ENTREGADO
            print(f"Pedido {self.id} ENTREGADO")
        print("\n")

print("\n")
print("TE DOY LA BIENVENIDA AL PROGRAMA DE GESTIÓN DE PEDIDOS")
orders = list()
while True:
    option  = input("¿Qué quieres hacer?\n - Registrar un nuevo pedido(N)\n - Mostrar el estado de un pedido(S)\n - Enviar un pedido(E)\n - Cancelar un pedido(C)\n - Marcar un pedido como entregado(D)\n - Mostrar todos los pedidos(A)\n - Salir(O)\nIntroduce la opción ---->").lower()
    if len(orders)==0 and option != "n":
            print("No hay pedidos registrados en el sistema...")
            print("\n")
            sleep(1)
    else:
        if option == "n":
            num_order = int(input("Entendido, dime el número de pedido: "))
            for element in orders:
                if int(num_order) == int(element.id):
                    print(f"El pedido {num_order} se encuentra ya registrado en sistema")
                    break
            else:
                new_order = Order(num_order)
                orders.append(new_order)
                print(f"Pedido con ID {num_order} creado y almacenado en el sistema")
            sleep(1)
        elif option == "s":
            order_id = input("Ok, dime el id del pedido que quieres ver: ")
            for order in orders:
                if order.check_id(order_id):
                    print("A continuación te muestro el pedido solicitado:")
                    order.show_order()
                    break
            else:
                print("No hay ningún pedido con ese id...")
            sleep(1)
        elif option == "e":
            order_id = input("Vale, dime el id del pedido que quieres marcar como enviado: ")
            for order in orders:
                if order.check_id(order_id):
                    order.send_order()
                    break
            else:
                print("No hay pedidos con ese id...")
            sleep(1)
        elif option == "c":
            order_id = input("Entendido, dime el id del pedido que deseas cancelar: ")
            for order in orders:
                if order.check_id(order_id):
                    order.cancel_order()
                    break
            else:
                print("No existe ningún pedido con ese id en el sistema...")
            sleep(1)
        elif option == "d":
            order_id = input("Perfecto, dime el id del pedido que quieres marcar como entregado: ")
            for order in orders:
                if order.check_id(order_id):
                    order.order_delivered()
                    break
            else:
                print("No hay ningún pedido en el sistema con ese id...")
            sleep(1)
        elif option == "a":
            print("Estos son los pedidos que hay en el sistema:")
            print("\n")
            for order in orders:
                order.show_order()
            sleep(1)
        elif option == "o":
            print("GRACIAS POR USAR EL PROGRAMA DE GESTIÓN DE PEDIDOS. HASTA PRONTO.")
            print("\n")
            break
        else:
            print("La opción no es válida, prueba de nuevo...")
            sleep(1)
        print("\n")
