"""
    Ejercicio
"""

class Programador:
    
    apellido: str = None
    def __init__(self, nombre, edad, lenguaje):
        self.nombre = nombre
        self.edad = edad
        self.lenguaje = lenguaje
        
    def print(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, Lenguaje: {self.lenguaje}")
        
mi_programador = Programador("Misael", 35, ["Python", "JavaScript", "C++"])
mi_programador.apellido = "Fernandez"
mi_programador.print()
mi_programador.edad = 33
mi_programador.print()

"""
    Extra
"""

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None

        return self.stack.pop()

    def count(self):
        return len(self.stack)

    def print(self):
        for item in reversed(self.stack):
            print(item)
                
my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.count())

# FIFO
class Queue:
    def __init__(self):
        self.queue = []
        
    def equeue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)
    
        
    def count(self):
        return len(self.queue)
    
    def print(self):
        for item in reversed(self.queue):
            print(item)
            
my_queue = Queue()
my_queue.equeue("A")
my_queue.equeue("B")
my_queue.equeue("C")
print(my_queue.count())
my_queue.print()
my_queue.dequeue()
print(my_queue.count())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.count())
