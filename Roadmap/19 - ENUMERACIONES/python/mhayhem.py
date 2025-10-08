# @Author Mhayhem

from enum import Enum
import random


# EJERCICIO:
# Empleando tu lenguaje, explora la definición del tipo de dato
# que sirva para definir enumeraciones (Enum).
# Crea un Enum que represente los días de la semana del lunes
# al domingo, en ese orden. Con ese enumerado, crea una operación
# que muestre el nombre del día de la semana dependiendo del número entero
# utilizado (del 1 al 7).


class Week(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7
    
    def get_day_name(num: int):
        print(Week(num).name)


# DIFICULTAD EXTRA (opcional):
# Crea un pequeño sistema de gestión del estado de pedidos.
# Implementa una clase que defina un pedido con las siguientes características:
# - El pedido tiene un identificador y un estado.
# - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
# - Implementa las funciones que sirvan para modificar el estado:
#   - Pedido enviado
#   - Pedido cancelado
#   - Pedido entregado
#   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
# - Implementa una función para mostrar un texto descriptivo según el estado actual.
# - Crea diferentes pedidos y muestra cómo se interactúa con ellos.

class ProductOrderStatus(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    CANCELADO = 3
    ENTREGADO = 4
    
    
        
    
class Order:
    def __init__(self, id: int, product: str):
        self.id = id
        self.product = product
        self.status = ProductOrderStatus.PENDIENTE
    
    def __str__(self):
        return f"Pedido: {self.id}; Producto: {self.product}; Estado: {self.status.name.capitalize()}."
    
    def status_change(self, num: int):
        if ProductOrderStatus(num).name == "ENTREGADO" and self.status != ProductOrderStatus.ENVIADO:
            print(f"No se puede entregar el pedido con ID {self.id}, su estado es {self.status.name.capitalize()}")
        elif ProductOrderStatus(num).name == "CANCELADO" and self.status == ProductOrderStatus.ENTREGADO:
            print(f"El pedido con ID {self.id} no se puede cancelar por que su estado es {self.status.name.capitalize()}")
        elif ProductOrderStatus(num).name == "ENVIADO" and self.status == ProductOrderStatus.CANCELADO:
            print(f"El pedido con ID {self.id} no se puede enviar por que su estado es {self.status.name.capitalize()}")
        else:
            self.status = ProductOrderStatus(num)
            print(f"Pedido ID {self.id} es {self.status.name.capitalize()}")


def order_create(array: list[Order]):
    print("Creando Pedido.")
    
    product = input("Producto: \n")
    id = random.randint(100, 999)
    
    print(f"Pedido creado con ID {id}, Producto: {product}")
    order = Order(id, product)
    
    
    array.append(order)
    
    return array
    
def show_orders(array: list[Order]):
    return [f"{item.id} {item.product} {item.status.name.capitalize()}" for item in array]
     
    

def order_management(array: list[Order]):
    while True:
        print("\n")
        if not array:
            print("No hay pedidos en cola.")
            order_create(array)
        else:
            print("C. Crear nuevo pedido.\n"
                "A. Actualizar estado del Pedido.\n"
                "M. Mostrar Pedidos.\n"
                "D. descripcion del pedido.\n"
                "S. Salir del gestor de pedidos.\n")
            option = input().lower()
            match option:
                case "c":
                    order_create(array)
                case "a":
                    print(show_orders(array))
                    try:
                        order_update = int(input("Pedido que quiere actualizar: (id).\n"))
                        found = False
                        for item in array:
                            if item.id == order_update:
                                found = True
                                print("Nuevo estado del pedido.\n"
                                    "2. Enviado.\n"
                                    "3. Cancelar.\n"
                                    "4. Entregado.\n")
                                status = input()
                                match status:
                                    case "2":
                                        num = 2
                                    case "3":
                                        num = 3
                                    case "4":
                                        num = 4
                                
                                item.status_change(num)
                        if not found:
                            print(f"No hay ningún pedido con el id {order_update}.")
                    except ValueError:
                        print("El ID solo pueden ser números")
                    
                case "m":
                    print(show_orders(array))
                
                case "d":
                    print("Id del pedido: \n")
                    try:
                        id_description = int(input())
                        for item in array:
                            if  item.id == id_description:
                                print(item)
                    except ValueError:
                        print("El ID solo pueden ser números")
                case "s":
                    print("Saliendo del gestor de pedidos.")
                    break
        print("\n")
                
if __name__=="__main__":
    order_list = []
    order_management(order_list)