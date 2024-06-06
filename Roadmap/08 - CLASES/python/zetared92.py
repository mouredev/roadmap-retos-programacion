# Reto #08 CLASES

class Samurai:

    surname: str = None

    def __init__(self, name: str, age: int, affiliation: list):
        self.name = name
        self.age = age
        self.affiliation = affiliation

    def print(self):
        print(
            f"Name: {self.name} | Surname: {self.surname} | Age: {self.age} | Affiliation: {self.affiliation}"
        )

the_samurai = Samurai("Johnny", 34, ["U.S. Army", "Samurai", "Silverhand Studios"])
the_samurai.print()
the_samurai.surname = "Silverhand"
the_samurai.print()
the_samurai.age = 88
the_samurai.print()


# Extra

print("🧩 DIFICULTAD EXTRA - IMPLEMENTACIÓN DE DOS CLASES (STACK-QUEUE) 🧩")

# STACK

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
my_stack.push("X")
my_stack.push("Y")
my_stack.push("Z")
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


# QUEUE

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
my_queue.enqueue("X")
my_queue.enqueue("Y")
my_queue.enqueue("Z")
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