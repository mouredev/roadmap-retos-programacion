""" EJERCICIO """


class People:
    last_name: str = None

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello I'm {self.name} {self.last_name} and my age {self.age}")


people = People("Marco", 17)
people.last_name = "Ferreto"
people.greet()
people.age = 18
people.greet()

""" DIFICULTAD EXTRA """

# LIFO


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty() == 0:
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items)

    def print(self):
        for item in reversed(self.items):
            print(item)


my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.is_empty())
my_stack.print()
my_stack.pop()
print(my_stack.is_empty())


print("----------------------------------------------------------------")
# FIFO


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty() == 0:
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items)

    def print(self):
        for item in self.items:
            print(item)


my_queue = Queue()

my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")
print(my_queue.is_empty())
my_queue.print()
my_queue.dequeue()
print("\n================================")
my_queue.print()
