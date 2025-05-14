# clases
class Programmer:

    nick: str = ""

    def __init__(self, name: str, age: int, languages: list):
        self.name = name
        self.age = age
        self.languages = languages

    def print(self):
        print(f"Nombre: {self.name} | Edad: {self.age} | Lenguajes: {self.languages} | Nick: {self.nick}")

my_programmer = Programmer("Victor", 41, ["Python", "Java", "JavaScript"])
my_programmer.print()
my_programmer.nick = "fishellVvv"
my_programmer.print()
my_programmer.age += 1
my_programmer.print()

# EXTRA
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
            print(item, end=" ")
        print()

print("\nExtra: class Stack")
my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(f"Recuento: {my_stack.count()}")
my_stack.print()
print(f"Desapilamos: {my_stack.pop()}")
print(f"Recuento: {my_stack.count()}")
my_stack.print()

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
            print(item, end=" ")
        print()

print("\nExtra: class Queue")
my_queue = Queue()
my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")
print(f"Recuento: {my_queue.count()}")
my_queue.print()
print(f"Desencolamos: {my_queue.dequeue()}")
print(f"Recuento: {my_queue.count()}")
my_queue.print()