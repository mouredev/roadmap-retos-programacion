"""
Ejercicio

"""

class Programer:

    surname : str = None

    def __init__(self, name : str, age : int, lenguage: list):
        self.name = name
        self.age = age
        self.lenguage = lenguage

    def print(self):
        print(f"Nombre: {self.name} Appellido {self.surname} Edad: {self.age} Lenguajes: {self.lenguage}")

programador_1 = Programer("Tomas", 20, ["Python"])
programador_1.print()
programador_1.surname = "Luna"
programador_1.print()
programador_1.age = 21
programador_1.print()

"""
Extraa

"""
#!Version Propia
class Stack :
    def __init__(self):
        self.stack = []
    def print(self):
        print(f"Esta es tu pila {self.stack}")
    def longe (self):
        return  len(self.stack)
    def push(self, item : int):
        self.stack.append(item)
        print(f"Has agregado el elemento {item} la pila es {self.stack}")
    def pop(self):
        if len(self.stack) > 0 :
            dele_element = self.stack[-1]
            self.stack.pop()
            print(f"Has eliminado el elemento {dele_element} tu pila ahora es {self.stack}")
        else:
            print("No hay elementos en tu pila")


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)   
my_stack.push(4) 
my_stack.print()
print(f"La longitud de tu pila es {my_stack.longe()}") 
my_stack.pop()

class Queue:
    def __init__(self):
        self.queue = []
    def pushq (self, item):
        self.queue.append(item)
    def deleted (self):
        if len(self.queue) == 0 :
            return 0
        else:
            dele_element = self.queue[0]
            print(f"Elemento elimado : {dele_element}")
            return self.queue.pop(0)
    def count (self):
        return len(self.queue)
    def printq (self):
        print(f"Esta es tu cola {self.queue}")


my_queue = Queue()
my_queue.pushq(1)
my_queue.pushq(2)
my_queue.pushq(3)
my_queue.pushq(4)
my_queue.printq()
print(f"Cantidad {my_queue.count()}")
my_queue.deleted()
my_queue.printq()

#!Version de Brais
class Stack:
    def __init__(self):
        self.stack = []

    def push (self, item):
        self.stack.append(item)

    def pop (self):
        if self.count() == 0:
            return None
        return self.stack.pop()

    def count (self):
        return len(self.stack)

    def print  (self):
        for item in reversed(self.stack):
            print(item)

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
print(my_stack.count())
my_stack.print()

#fifo
class Queue :
    def __init__(self):
        self.queue = []
    def equeue(self, item):
        self.queue.append(item)

    def dequeue (self):
        if self.count() -- 0:
            return None
        return self.queue.pop(0)

    def count (self):
            return len(self.queue)
    
    def print  (self):
        for item in self.queue:
            print(item)

my_queue = Queue()
my_queue.equeue(1)
my_queue.equeue(2)
my_queue.equeue(3)
my_queue.equeue(4)
print(my_queue.count())
my_queue.print()
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())

    

