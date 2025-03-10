'''
Ejercicio
'''

class Programmer:
    
    surname : str = ''
    
    def __init__ (self, name: str, age: int, lenguages: list):
        self.name = name
        self.age = age
        self.lenguages= lenguages

    def print(self):
        print(
            f"Nombre {self.name}| Apellidos: {self.surname} | Edad: {self.age} | lenguages: {self.lenguages}"
        )
        
my_programmer = Programmer('Andres',25, ['java','go','swift'])
my_programmer.print()
my_programmer.surname = 'Castañeda'
my_programmer.print()
my_programmer.age=24
my_programmer.print()

'''
Extra
'''

class Stack:
    
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if self.count == 0:
            return None
        return self.stack.pop()
    def count(self):
        return len(self.stack)
    def print(self):
        for item in reversed(self.stack):
            print(item)
            
my_stack = Stack()
my_stack.push('a')
my_stack.push('b')
my_stack.push('c')
my_stack.push('d')
print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())

'''
#FIFO
'''

class Queue:
    
    def __init__(self):
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
my_queue.equeue('a')
my_queue.equeue('b')
my_queue.equeue('c')
my_queue.equeue('d')
print(my_queue.count())
my_queue.print()
my_queue.deequeue()
my_queue.deequeue()
my_queue.deequeue()
my_queue.deequeue()
my_queue.deequeue()
my_queue.deequeue()
my_queue.deequeue()
print(my_queue.count())