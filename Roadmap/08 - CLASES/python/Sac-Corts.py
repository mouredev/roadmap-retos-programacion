"""
EJERCICIO
"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        self.saludar = print(f"Hola {self.nombre} ({self.edad}), ¿cómo estás?")

isaac = Persona("Isaac", 22)
isaac.saludar()

"""
EJERCICIO EXTRA
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else: 
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        size = len(self.items)
        items = self.items[::-1]
        print(f"{size} | {items}")
        return size, items  
    
pila = Stack()
pila.push(10)
pila.push(20)
pila.push(30)
print(pila.is_empty())
dimension, elementos = pila.size()
print(pila.pop())
print(pila.peek())

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        size = len(self.items)
        items = self.items
        print(f"{size} | {items}")
        return size, items
    
cola = Queue()
cola.enqueue(11)
cola.enqueue(12)
cola.enqueue(13)
print(pila.is_empty())
dimension, elementos = cola.size()
print(cola.dequeue())
print(cola.peek())

