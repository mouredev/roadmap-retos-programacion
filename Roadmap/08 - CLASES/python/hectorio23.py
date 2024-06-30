# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

from typing import Optional

###########################################
# CLASE WebPage
###########################################

class WebPage:
    def __init__(self, title: str, index: int):
        self.title = title
        self.index = index

    def get_info(self):
        print(f"<Object WebPage - {self.title} at {hex(id(self))}>")

    def __str__(self):
        return f"<Object WebPage - {self.title} at {hex(id(self))}>"

###########################################
# CLASE Queue
###########################################

class Queue:
    def __init__(self):
        self.next: Optional[Queue] = None
        self.last: Optional[Queue] = None
        self.size = 0
        self.page: Optional[WebPage] = None

    def push(self, web_page: WebPage):
        tmp = Queue()
        tmp.page = web_page
        if self.size == 0:
            self.next = tmp
            self.last = tmp
        else:
            self.last.next = tmp
            self.last = tmp
        self.size += 1

    def pop(self) -> Optional[WebPage]:
        if self.size == 0:
            return None
        aux = self.next
        self.next = aux.next
        self.size -= 1
        if self.size == 0:
            self.last = None
        return aux.page

###########################################
# CLASE Stack
###########################################

class Stack:
    def __init__(self):
        self.next: Optional[Stack] = None
        self.garbage: Optional[Stack] = None  # experimental
        self.size = 0
        self.page: Optional[WebPage] = None

    def push(self, web_page: WebPage):
        tmp = Stack()
        tmp.page = web_page
        tmp.next = self.next
        self.next = tmp
        self.size += 1

    def pop(self) -> Optional[WebPage]:
        if self.size == 0:
            return None
        aux = self.next
        self.next = aux.next
        self.size -= 1
        return aux.page

###########################################
# CLASE Persona
###########################################

class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    def set_nombre(self, nuevo_nombre: str):
        self.nombre = nuevo_nombre

    def set_edad(self, nueva_edad: int):
        self.edad = nueva_edad

###########################################
# PROGRAMA PRINCIPAL
###########################################

if __name__ == "__main__":
    # Crear una instancia de Persona
    persona = Persona("Juan", 30)

    # Imprimir los atributos
    print("Datos de la persona:")
    persona.info()

    # Modificar los atributos
    persona.set_nombre("María")
    persona.set_edad(25)

    # Imprimir los atributos actualizados
    print("\nDatos de la persona actualizados:")
    persona.info()

    # Creando los objetos WebPage para utilizar en Stack y Queue
    p1 = WebPage("index", 1)
    p2 = WebPage("index", 2)
    p3 = WebPage("index", 3)

    # Crear una instancia de Queue
    queue = Queue()

    # Agregar elementos a Queue
    queue.push(p1)
    queue.push(p2)
    queue.push(p3)

    print(f"\nNúmero de elementos en Queue: {queue.size}")
    queue.pop()
    queue.pop()
    queue.pop()
    print(f"Número de elementos en Queue después de eliminar: {queue.size}")

    # Crear una instancia de Stack
    stack = Stack()

    # Agregar elementos a Stack
    stack.push(p1)
    stack.push(p2)
    stack.push(p3)

    print(f"\nNúmero de elementos en Stack: {stack.size}")
    stack.pop()
    stack.pop()
    stack.pop()
    print(f"Número de elementos en Stack después de eliminar: {stack.size}")
