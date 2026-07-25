'''
Clases
'''

class Programmer:

    surname: str = None

    def __init__(self, name : str, age : int, languages: list) -> None:
        self.name = name
        self.age = age
        self.languages = languages

    def print(self):
        print(f"Nombre: {self.name}")
        print(f"Apellidos: {self.surname}")
        print(f"Edad: {self.age}")
        print(f"Lenguajes: {self.languages}")

my_programmer = Programmer("Pedro", 35, ["Python", "C#"])
my_programmer.print()
my_programmer.surname = "García"
my_programmer.print()
my_programmer.age = 37
my_programmer.print()

'''
Ejercicio extra
'''
# Pila (LIFO)
class Stack:

    def __init__(self) -> None:
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()

    def count(self):
        return len(self.stack)
    
    def print(self):
        for item in reversed(self.stack):
            print(item)


print("\nEjercicio extra - LIFO!")
my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.stack)
my_stack.print()
my_stack.pop()
print(my_stack.stack)
print(my_stack.count())


# Cola (FIFO)
class Queue:

    def __init__(self) -> None:
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
        for item in self.queue:
            print(item)


print("\nEjercicio extra - FIFO!")
my_queue = Queue()
my_queue.equeue("A")
my_queue.equeue("B")
my_queue.equeue("C")
print(my_queue.queue)
my_queue.print()
my_queue.dequeue()
print(my_queue.queue)
print(my_queue.count())

