"""
* EJERCICIO:
* Implementa los mecanismos de introducción y recuperación de elementos propios de las
* pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
* o lista (dependiendo de las posibilidades de tu lenguaje).
*
* DIFICULTAD EXTRA (opcional):

* - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
*   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
*   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
*   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
*   el nombre de una nueva web.

* - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
*   impresora compartida que recibe documentos y los imprime cuando así se le indica.
*   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
*   interpretan como nombres de documentos.
"""

####### ---------------------- Stack ------------------------- ######

""" Un "stack" es una estructura de datos que sigue el principio de Last In, First Out (LIFO). 
Esto significa que el último elemento agregado a la pila es el primero en ser eliminado."""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):       # funcion para agregar un elemento a la parte superior de la pila
        self.items.append(item)

    def pop(self):              # funcion para eliminar y devolver el elemento superior de la pila
        if not self.is_empty():
            return self.items.pop()
        else:
            print("La pila está vacía")

    def peek(self):             # funcion para mostrar el ultimo elemento que se agrego a la pila sin borrarlo
        if not self.is_empty():
            return self.items[-1]
        else:
            print("La pila está vacía")

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.items)

print(stack.pop())  
print(stack.pop()) 
print(stack.peek())

print(stack.items)


###### ----------------------- Queue ------------------------ ########

"""Una "queue" es una estructura de datos que sigue el principio de First In, First Out (FIFO). 
Esto significa que el primer elemento agregado a la cola es el primero en ser eliminado.
Es similar a una fila en un supermercado. La primera persona que llega es la primera en ser atendida."""

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):                # funcion para agregar un elemento al final de la cola
        self.items.append(item)

    def dequeue(self):                      # funcion para eliminar y devolver el elemento del principio de la cola
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("La cola está vacía")

    def peek(self):                        # funcion que devuelve el elemento que esta en el frente de la cola es
        if not self.is_empty():            # decir el primer elemento que se agrego a la cola, el elemento no se elimina
            return self.items[0]
        else:
            print("La cola está vacía")

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.items)

print(queue.dequeue())  
print(queue.dequeue()) 
print(queue.peek())


######## -------------------------------DIFICULTAD EXTRA----------------------------- ############

"""Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
*   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
*   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
*   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
*   el nombre de una nueva web.
"""

class NavegadorWeb:
    def __init__(self):
        self.historial = []
        self.actual = None

    def navegar(self, sitio_web):
        if self.actual:
            self.historial.append(self.actual)
        self.actual = sitio_web
        print(f"Has navegado a: {sitio_web}")
        self.mostrar_historial()

    def adelante(self):
        if self.historial:
            sitio_web = self.historial.pop()
            self.actual = sitio_web
            print(f"Avanzando hacia adelante a: {sitio_web}")
        else:
            print("No hay más páginas para avanzar.")

    def atras(self):
        if self.actual:
            self.historial.append(self.actual)
            sitio_web = self.historial.pop(-2)
            self.actual = sitio_web
            print(f"Retrocediendo hacia atrás a: {sitio_web}")
        else:
            print("No hay historial para retroceder.")
    def mostrar_historial(self):
        print("Historial de navegacion:", self.historial)

navegador = NavegadorWeb()

while True:
    print("\nIngresa una accion")
    accion = input("""
        adelante,
        atras,
        nombre de la página web
        salir
        opcion: """)
    try:
        if accion == "adelante":
            navegador.adelante()
        elif accion == "atras":
            navegador.atras()
        elif accion == "salir":
            print("Saliendo del navegador.")
            break
        else:
            navegador.navegar(accion)
    except ValueError:
        print("Por favor, ingresa una opcion válida.")


""" Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
*   impresora compartida que recibe documentos y los imprime cuando así se le indica.
*   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
*   interpretan como nombres de documentos.
"""

from collections import deque

class ImpresoraCompartida:
    def __init__(self):
        self.cola_impresion = deque()

    def agregar_documento(self, document_name):
        self.cola_impresion.append(document_name)
        print(f"El documento '{document_name}' ha sido agregado a la cola de impresión.")        

    def imprimir_documento(self):
        if self.cola_impresion:
            document_to_print = self.cola_impresion.popleft()
            print(f"Imprimiendo el documento: '{document_to_print}'")
        else:
            print("La cola de impresión está vacía. No hay documentos para imprimir.")

    def mostrar_cola(self):
        print("Cola actual de impresión:", self.cola_impresion)

printer = ImpresoraCompartida()

while True:
    print("\n¿Qué deseas hacer?")
    opcion = input("""
        1.- Agregar documento
        2.- Imprimir documento
        3.- Mostrar cola de impresión
        4.- Salir
        Opción: """)
    
    try:
        opcion = int(opcion)
        if opcion == 1:
            documento = input("Introduce el nombre del documento que deseas agregar: ")
            printer.agregar_documento(documento)
        elif opcion == 2:
            printer.imprimir_documento()
        elif opcion == 3:
            printer.mostrar_cola()           
        elif opcion == 4:
            print("Programa de impresión cerrado. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingresa un número del 1 al 4.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

