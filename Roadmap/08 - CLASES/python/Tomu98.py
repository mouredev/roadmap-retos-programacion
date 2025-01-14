""" Reto 08: Clases """

class Programmer:
    surname: str = None
    
    def __init__(self, name: str, age: int, languages: list):
        self.name = name
        self.age = age
        self.languages = languages

    def print(self):
        print(f"Nombre: {self.name} | Apellidos: {self.surname} | Edad: {self.age} | Lenguajes: {self.languages}")

my_programmer = Programmer("Tomu", 25, ["Python", "SQLite", "FastAPI"])
my_programmer.print()
my_programmer.surname = "Arlert"
my_programmer.print()
my_programmer.age = 26
my_programmer.print()



""" Reto extra """

# LIFO
class Stack:
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

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.count())
my_stack.print()
my_stack.pop()
my_stack.print()


# FIFO
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
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

my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
print(my_queue.count())
my_queue.print()
my_queue.dequeue()
my_queue.print()
