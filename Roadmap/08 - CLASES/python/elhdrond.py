"""
    CLASSES
"""

class Developer:

    alias:str = None

    def __init__(self, name: str, age:int, languages:list):
        self.name = name
        self.age = age
        self.languages = languages

    # __str__ is the pythonic way to define string representation of an object
    def __str__(self): 
        return f"Name: {self.name} | Alias: {self.alias} | Age: {self.age} | Languages: {self.languages}"



dev_1 = Developer("Sergio", 35, ["Python", "C#", "PHP"])
dev_1.alias = "Elhdrond"
dev_1.age = 36
print(dev_1)

"""
    EXTRA EXERCISE
"""

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

    def __str__(self):
        return "\n".join(str(item) for item in reversed(self.stack))

print("STACK")
my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.count())
print(my_stack)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.count())
print(my_stack)




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

    def __str__(self):
        return "\n".join(str(item) for item in self.queue)

print("QUEUE")
my_queue = Queue()
my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")
print(my_queue.count())
print(my_queue)
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.count())
print(my_queue)
