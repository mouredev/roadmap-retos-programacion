#Class
class User:

    surname: str = None

    def __init__(self, name: str, age: int, languages: list):
        self.name = name
        self.age = age
        self.languages = languages

    def profile(self):
        print(f"Name: {self.name} | Surname: {self.surname} | Age: {self.age} | Languages: {self.languages}")

my_user = User("Antonia", 45, ["English", "Spanish", "French"])
my_user.profile()
my_user.surname = "Sanchez"
my_user.languages = ["English", "Spanish", "French", "Hindi"]
my_user.profile()


#Extra Exercise
#LIFO

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.count() > 0:
            self.stack.pop()
        else:
            print("The list is empty, please add few items before delete it")
    
    def count(self):
        return len(self.stack)
    
    def print(self):
        for item in reversed(self.stack):
            print(item)

my_stack = Stack()
my_stack.push("The jungle book")
my_stack.push("The lion king")
my_stack.push("Coco")
print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())

#FIFO

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.count() > 0:
            self.queue.pop(0)
        else:
            print("The list is empty, please add few items before delete it")

    def count(self):
        return len(self.queue)
    
    def print(self):
        for item in self.queue:
            print(item)


my_queue = Queue()
my_queue.enqueue("The Godfather")
my_queue.enqueue("The Godfather 2")
my_queue.enqueue("The Godfather 3")
print(my_queue.count())
my_queue.print()
my_queue.dequeue()
print(my_queue.count())
my_queue.print()
