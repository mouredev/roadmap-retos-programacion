# Problem 08 Classes

class Cat:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def meow(self):
        print("Meow!")

    def describe(self):
        print(f"My name is {self.name}")
        print(f"I'm {self.color}")
        print(f"And I'm {self.age}yo")


orange_cat = Cat("Mordisquitos", 1, "orange")
orange_cat.describe()


# Stack - LIFO
class Stack:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def delete(self):
        try:
            item = self.items.pop()
        except IndexError:
            item = None
        finally:
            return item

    def length(self):
        return len(self.items)

    def show(self):
        for item in reversed(self.items):
            print(item)


my_stack = Stack()
my_stack.insert(1)
my_stack.insert(2)
my_stack.insert(3)
my_stack.insert(4)
print(f"{my_stack.length() = }")
print(f"my_stack.show()")
my_stack.show()


# Queue - FIFO
class Queue:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def delete(self):
        try:
            item = self.items.pop(0)
        except IndexError:
            item = None
        finally:
            return item

    def length(self):
        return len(self.items)

    def show(self):
        for item in self.items:
            print(item)


my_queue = Queue()
my_queue.insert(1)
my_queue.insert(2)
my_queue.insert(3)
my_queue.insert(4)
print(f"{my_queue.length() = }")
print(f"my_queue.show()")
my_queue.show()
