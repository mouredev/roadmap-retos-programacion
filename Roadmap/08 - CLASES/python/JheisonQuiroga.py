""" 1. Clases 
Las clases son planos o modelos para la creacion de objetos
"""
# Syntaxys
class Person:
    pass

print(Person)

# Object Class
class Person:
    """ A simple example class"""
    name = "Duban" # class variable

    def greet(self): # class Method
        return f"Hi there, i`m {self.name}"
    
p = Person()
print(p.greet()) # Hi there, i`m Duban

# 1.1.Constructor Function

class Person:
    def __init__(self):
        # Automatically run
        print("Creando mi primer objeto de la clase persona")
    
p = Person() # Creando mi primer objeto de la clase persona

# 1.2. Atributtes and Methods
"""
Un atributo es una variable asociada a un objeto y un metodo es una funcion
dentro de una clase que realiza alguna accion. Es decir es una funcion que puede ejecutar un
objeto
"""

class Person:
    def __init__(self, firstname, lastname, age, country):
        self.fname = firstname
        self.lname = lastname
        self.age = age
        self.country = country
        self.skills = []

    def person_info(self):
        return f"I'm {self.fname} {self.lname}, im {self.age}, and live in {self.country}"
    
    def greet(self):
        return "Hello World"
    
    def add_skill(self, skill):
        self.skills.append(skill) 


p = Person("Duban", "Quiroga", 25, "Colombia")
print(p) # <__main__.Person object at 0x000001CB727E1910> id object
print(p.person_info())
print(p.greet()) # Hello World
p.add_skill("Python")
p.add_skill("Java")
print(p.skills) # ['Python', 'Java']

"""
Extra
"""

class Stack: # Pilas
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else 0
        
    def top(self): # Top of Stack (TOS)
        return self.stack[-1]
    
    def len_stack(self):
        return len(self.stack)
    
    def print_stack(self):
        for item in reversed(self.stack):
            print(item)

    

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
print(my_stack.stack) # [1, 2, 3, 4]
print(my_stack.top()) # 4
print(my_stack.len_stack()) # 4
my_stack.print_stack()

# Queue - FIFO (First in - First Out)

class Queue: 
    def __init__(self):
        self.deque = []

    def add(self, item):
        self.deque.append(item)

    def dequeue(self):
        return self.deque.pop(0)if self.deque else None
    
    def len_queue(self):
        return len(self.deque)
    
    def print_queue(self):
        for item in self.deque:
            if item:
                print(item)

queue = Queue()
queue.add("A")
queue.add("B")
queue.add("C")
queue.add("D")

queue.print_queue()

print(queue.dequeue()) # A
print(queue.len_queue()) # 3
queue.print_queue() # B, C, D