'''
Exercise
'''

#Classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')
        
person1 = Person('Jake', 36)
person1.say_hello()

person2 = Person('Jane', 25)
person2.say_hello()

person1.age = 45
person1.say_hello()

'''
Extra
'''

#Stack class

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        return self.stack.append(item)
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
my_stack.push('Marvel')
my_stack.push('DC')
my_stack.push('Dark Horse')
print(my_stack.count())
print(my_stack.print())


#Queue class

class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        return self.queue.append(item)
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
my_queue.enqueue('Marvel')
my_queue.enqueue('DC')
my_queue.enqueue('Dark Horse')
print(my_queue.count())
print(my_queue.print())