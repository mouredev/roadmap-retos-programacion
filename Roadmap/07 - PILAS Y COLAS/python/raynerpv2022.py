# /*
#  * EJERCICIO:
#  * Implementa los mecanismos de introducción y recuperación de elementos propios de las
#  * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
#  * o lista (dependiendo de las posibilidades de tu lenguaje).
#  *


pila = []
def set_pila(items):
    pila.append(items)

def get_pila():
    return pila.pop(len(pila)-1)

cola = []

def set_cola(items):
    cola.append(items)

def get_cola():
    return cola.pop(0)

def pila_func():
             print(" PILA, Set (1) o Get (2)")
             op_pila = input(":")
             match op_pila:
                 case "1":
                     print("Items a introducir : ")
                     it = input(":")
                     set_pila(it)
                 case "2":
                     print("Sacando ultimo elemento pila")
                     print("Pila completa ",pila)
                     print(get_pila())
                     print("Pila actualizada ",pila)

def cola_func():
             print(" Cola, Set (1) o Get (2)")
             op_cola = input(":")
             match op_cola:
                 case "1":
                     print("Items a introducir : ")
                     it = input(":")
                     set_cola(it)
                 case "2":
                     print("Sacando ultimo elemento cola")
                     print("COla completa ",cola)
                     print(get_cola())
                     print("Cola actualizada ",cola)

while True:
    print(" Pila (1) o  Cola (2) Salir (3):")
    op = input(":")
    match op:
        case "1":
             pila_func()
        case "2":
              cola_func()
        case "3":
            break
        case _:
              print( "OPcion no valida")



    
    #  * DIFICULTAD EXTRA (opcional):
#  * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
#  *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
#  *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#  *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
#  *   el nombre de una nueva web.
#  * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#  *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
#  *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
#  *   interpretan como nombres de documentos.
#  */


 
def is_empty(list1: list,cad: str)   :
     if len(list1) == 0:
          print(cad)
          return True
     else :
          return False
     
# ?muetsra todas las web de la lista, y el ligar donde esta actualmente la lista
def mostrar_url(url_list :list, index : int):
     if not is_empty(url_list,"No hay direcciones web"):
          print(f"{url_list}, posiscion actual :{index}")

def TOR():
     url_list = []
     print("NAVEGADOR T O R")
     index = 0 # inicio con indice en posicion 0
     while True:
          len_list_url = len(url_list)
          print("adelante, atras, url, salir ?: ")
          op = input()
          match op:
               case "adelante":
                     
                    if not is_empty(url_list,"No hay direcciones web"):
                        if(len_list_url- 1) > index:
                            index+=1 # si no he llegado al final incremento 1 al indice, si llegue al final no incremento
                    print("Navegando en ",url_list[index]) #  muestro web en indice actual, 

               case  "atras":
                     
                    if not is_empty(url_list,"No hay direcciones web") :
                        if 0 < index: 
                            index-=1 # si no he llegado al inicio , decremento el indice actual, si llegue al inicio, muestro el primero
                    print("Navegando en ", url_list[index])

               case "url" :
                    mostrar_url(url_list,index)

               case "salir" :
                    break
               case _:
                    url_list.append(op)
                    index = len(url_list)-1
                    print("Navegando en ", url_list[index])
                    
                    
def Printer():
     printer_queue = []
     while True:
          print("imprimir o salir :")
          op = input()
          match op:
               case "imprimir":
                    if not is_empty(printer_queue,"No hay trabajos a imprimir") and len(printer_queue) > 0:
                        print(f"Imprimiendo {printer_queue.pop(0)}")
                        print(f"Tareas por imprimir {printer_queue }")
               case "salir":
                    break
               case _:
                    printer_queue.append(op)
          
               

TOR()   
Printer()        