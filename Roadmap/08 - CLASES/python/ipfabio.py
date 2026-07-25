"""
Ejercicios
"""

class Programmer:

    surname: str = ""

    def __init__(self, name: str, age: int, lenguage: list) -> None:
        self.name = name
        self.age = age
        self.lenguage = lenguage

    
    def print(self):
        print(f"Nombre: {self.name} | Apellidos: {self.surname} | Edad: {self.age} | Lenguajes: {self.lenguage}")

my_progammer = Programmer("Marco", 39, ["Python", "Java", "C"])
my_progammer.print()
my_progammer.surname = "Polo"
my_progammer.print()
my_progammer.age = 35
my_progammer.print()

"""
Extra
"""

# LIFO

class Stack:

    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
        # Agregamos {item} al stack"
    
    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()
        # Eliminamos el último {item} del stack"
 
    def count(self):
        return len(self.stack)
    
    def print(self):
        for item in reversed(self.stack):
            print(item)
        # Estado del stack: {self.stack}"

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

    def __init__(self) -> None:
        self.queue = []

    def equeue(self, item):
        self.queue.append(item)
    
    def deequeue(self):
        if self.count() == 0:
            return None
        self.queue.pop(0)
    
    def count(self):
        return len(self.queue)
    
    def print(self):
        for item in self.queue:
            print(item)

my_queue = Queue()
my_queue.equeue("A")
my_queue.equeue("B")
my_queue.equeue("C")
print(my_queue.count())
my_queue.print()
my_queue.deequeue()
print(my_queue.count())
my_queue.print()
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.count())