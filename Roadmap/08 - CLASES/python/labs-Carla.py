"""Ejercicio 1"""

class Programmer:

    surname: str =None

    def __init__(self, name:str, age:int, languages:list)-> None:
        self.name = name
        self.age = age
        self.languages = languages

    def print(self):
        print(f"Nombre: {self.name} | Apellidos: {self.surname}| Edad: {self.age} | Lenguajes: {self.languages}")

my_programmer = Programmer("Carla", 25, "[Python, Java]")
my_programmer.print()
my_programmer.surname = "Valde"
my_programmer.print()
my_programmer.age = 26
my_programmer.print()

"""Ejercicio 2 Extra"""

#lifo

class Pila:

    def __init__(self):
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


my_stack=Pila()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
my_stack.push("D")
print(my_stack.count())
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
print(my_stack.count())

#fifo

class Queue:
    def __init__(self):
        self.queue = []

    def equeue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)
        

    def count (self):
        return len(self.queue)

    def print(self):
        for item in reversed(self.queue):
            print (item)

my_queue = Queue()
my_queue.equeue("A")
my_queue.equeue("B")
my_queue.equeue("C")
my_queue.equeue("D")
print(my_queue.count())
my_queue.print()
my_queue.dequeue()
print(my_queue.count())
my_queue.print()
print(my_queue.count())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.count())
