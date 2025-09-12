# /*
#  * EJERCICIO:
#  * Empleando tu lenguaje, explora la definición del tipo de dato
#  * que sirva para definir enumeraciones (Enum).
#  * Crea un Enum que represente los días de la semana del lunes
#  * al domingo, en ese orden. Con ese enumerado, crea una operación
#  * que muestre el nombre del día de la semana dependiendo del número entero
#  * utilizado (del 1 al 7).

from enum import Enum

class Week_days(Enum):
    monday = 1
    tuesday = 2
    wednesday =3
    thrusday = 4
    friday = 5
    saturday = 6
    sunday = 7

   
    
def get_week(index):
    return Week_days(index).name



print(Week_days(1))
print(Week_days.monday.name)
print(Week_days.monday.value)
print(get_week(3))

 

#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un pequeño sistema de gestión del estado de pedidos.
#  * Implementa una clase que defina un pedido con las siguientes características:
#  * - El pedido tiene un identificador y un estado.
#  * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
#  * - Implementa las funciones que sirvan para modificar el estado:
#  *   - Pedido enviado
#  *   - Pedido cancelado
#  *   - Pedido entregado
#  *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
#  * - Implementa una función para mostrar un texto descriptivo según el estado actual.
#  * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
#  */

import time
import os

class Pedido :

    def __init__(self, serial=1) -> None:
        self.serial = serial
        self.ID = self.Estado.PENDIENTE.name
        

    class Estado (Enum):
        PENDIENTE = 1
        ENVIADO = 2
        ENTREGADO = 3
        CANCELADO = 4
    
    def  Enviar(self):
         if self.ID == self.Estado.PENDIENTE.name:
             self.ID = self.Estado.ENVIADO.name
             print(f"Pedido {self.serial} ha sido enviado ")
         elif self.ID == self.Estado.CANCELADO.name:
             print(f"Pedido {self.serial} esta Cancelado")
         else:
            print(f"Pedido {self.serial} no puede ser Enviado  porque porque no esta pendiente")

    def MostrarEstado(self):
        return f"el Estado actual del pedido {self.serial} es : {self.ID}"
    
    def Cancelar(self):
        if self.ID == self.Estado.CANCELADO.name:
             print(f"Pedido {self.serial} ya esta Cancelado")
             return True
            
        elif self.ID != self.Estado.ENTREGADO.name:
            self.ID = self.Estado.CANCELADO.name
            print(f"Pedido {self.serial} ha sido Cancelado ")
        else:
            print(f"Pedido {self.serial} no puede ser Cancelado porque ya se entrego")
        return False

    def Entregar(self):
        if self.ID == self.Estado.ENVIADO.name:
            self.ID = self.Estado.ENTREGADO.name
            print(f"Pedido {self.serial} ha sido Entregado ")
        elif self.ID == self.Estado.CANCELADO.name:
             print(f"Pedido {self.serial} esta Cancelado")
        else:
            print(f"Pedido {self.serial} no puede ser ENtregado porque no se ha enviado")


 
def buscar_pedido(ped):
    for i in pedidos:
        if i.serial == ped:
            return pedidos.index(i)
    return -1
            
    

def seleccionar_producto(ped):
    index = buscar_pedido(ped)
    if  index == -1:
        print(f"Pedido no encontrado")
        return
    
    os.system("clear")
    eliminar =  False
    while True:
        
        print(f"1 - Ver Estado {ped} ")
        print(f"2 - Enviar Pedido {ped}  ")
        print(f"3 - Cancelar Pedido {ped} ")
        print(f"4 - ENtregar Pedido {ped} ")
        print(f"5 - Salir del Producto {ped} ")
        s = input("")
        match s:
            case "1":
                print("MOstrando Estado")
                print(pedidos[index].ID)
            case "2":
                print("Enviando Producto  ")
                pedidos[index].Enviar()
            case "3":
                print("Cancelando Producto  ")
                if pedidos[index].Cancelar():
                    eliminar = True

            case "4":
                print("Entregando Producto  ")
                pedidos[index].Entregar()
            case "5":
                print("Saliendo del Producto  ")
                if eliminar:
                    print(f"Pedido {pedidos.pop(index).serial} Eliminado")
                break
            case _:
                print("Opcion Invalida")

 
    







pedidos = []
serial = 100
while True:
    
    print("Seleccione opcion")
    print("1 - Crear Pedido ")
    print("2 - Mostrar todos Pedido")
    print("3 - Seleccionar Pedido")
    print("4 - Salir")
    op = input("")
    
    match op:
            case "1":
                serial +=1
                pedidos.append(Pedido(f"{serial}A"))

            case "2":
                print("Mostrando Todos los Pedidos")
                for i in pedidos:
                    print(f"Pedido: {i.serial} Estado: {i.ID}")
                 
            case "3":
                print("Indique serial del pedido")
                serial = input("")
                seleccionar_producto(serial)
            
            case "4":
                print("Saliendo...")
                for i in range (10,0,-1):
                    print(i,end=" ", flush=True)
                    time.sleep(1)
                print()
                print("Programa terminado")
                break
            case _:
                print("Opcion no valida, 1-6 ")



