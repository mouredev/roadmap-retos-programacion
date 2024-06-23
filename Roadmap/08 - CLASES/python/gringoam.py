"""
Ejercicio
"""


class Programmer:

    surname: str = None

    def __init__(self, name: str, age: int, languages: list):
        self.name = name
        self.age = age
        self.languages = languages

    def print(self):
        print(
            f"Nombre: {self.name} | Apellidos: {self.surname} | Edad: {self.age} | Lenguajes: {self.languages}")


my_programmer = Programmer("Brais", 36, ["Python", "Kotlin", "Swift"])
my_programmer.print()
my_programmer.surname = "Moure"
my_programmer.print()
my_programmer.age = 37
my_programmer.print()

"""
Extra
"""

#Stack(pila)

class Stack:
    

    def __init__(self) -> None:
        self.stack=[]

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):

        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    
    def print(self):
        for item in reversed(self.stack):
            print(item)

    def count(self):
        return len(self.stack)

my_stack= Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
my_stack.print()
print(f"Cantidad: {my_stack.count()}")
print(f"Se elimino {my_stack.pop()}")
my_stack.print()
print(f"Cantidad: {my_stack.count()}")
print(f"Se elimino {my_stack.pop()}")
print(f"Se elimino {my_stack.pop()}")
print(f"Se elimino {my_stack.pop()}")
my_stack.print()
my_stack.count()
    
#Queue (Cola)

class Queue:
    

    def __init__(self) -> None:
        self.queue=[]

    def push(self, item):
        self.queue.append(item)
    
    def pop(self):

        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)
    
    def print(self):
        for item in self.queue:
            print(item)

    def count(self):
        return len(self.queue)

my_queue= Queue()
my_queue.push(1)
my_queue.push(2)
my_queue.push(3)
my_queue.print()
print(f"Cantidad: {my_queue.count()}")
print(f"elimi {my_queue.pop()}")
my_queue.print()
print(f"Cantidad: {my_queue.count()}")
print(f"elimi {my_queue.pop()}")
my_queue.print()
print(f"Cantidad: {my_queue.count()}")
    
