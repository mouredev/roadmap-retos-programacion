"""
Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
"""

"""
Stack LIFO
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek()) # prints: 3
print(stack.pop())  # prints: 3
print(stack.size()) # prints: 2

"""
Queue (FIFO)
"""

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.peek()) # prints: 1
print(queue.dequeue()) # prints: 1
print(queue.size()) # prints: 2

"""
EXTRA
"""

class NavegadorWeb:
    def __init__(self):
        self.pila = []
        self.actual = None

    def navegar(self, sitio):
        if self.actual is not None:
            self.pila.append(self.actual)
        self.actual = sitio
        print("Navegando a:", sitio)

    def adelante(self):
        if self.pila:
            sitio = self.pila.pop()
            print("Avanzando hacia adelante a:", sitio)
            self.actual = sitio
        else:
            print("No hay páginas para avanzar")

    def atras(self):
        if self.actual is not None:
            print("Retrocediendo hacia atrás a:", self.actual)
            self.actual = None
        else:
            print("No hay página actual")

# Probando la implementación
navegador = NavegadorWeb()
navegador.navegar("www.ejemplo1.com")
navegador.navegar("www.ejemplo2.com")
navegador.adelante()
navegador.atras()
navegador.adelante()


from collections import deque

class ImpresoraCompartida:
    def __init__(self):
        self.cola_impresion = deque()

    def agregar_documento(self, documento):
        self.cola_impresion.append(documento)
        print("Documento agregado a la cola:", documento)

    def imprimir(self):
        if self.cola_impresion:
            documento = self.cola_impresion.popleft()
            print("Imprimiendo documento:", documento)
        else:
            print("No hay documentos para imprimir")

# Probando la implementación
impresora = ImpresoraCompartida()
impresora.agregar_documento("Documento1")
impresora.agregar_documento("Documento2")
impresora.imprimir()
impresora.imprimir()
