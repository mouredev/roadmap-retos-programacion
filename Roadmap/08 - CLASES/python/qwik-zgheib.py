# -- exercise
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def printPerson(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")


person: Person = Person("Qwik", 22)
person.printPerson()


# -- extra challenge
class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, element: any) -> any:
        self.stack.append(element)
        return self.stack

    def pop(self) -> any:
        return self.stack.pop()

    def size(self) -> int:
        return len(self.stack)

    def printStack(self) -> None:
        print("stack elements:")
        for i, element in enumerate(self.stack):
            print(f"element {i + 1} -> {element}")


class Queue:
    def __init__(self) -> None:
        self.queue = []

    def push(self, element):
        self.queue.append(element)

    def pop(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def printQueue(self):
        for index, element in enumerate(self.queue):
            print(f"element {index + 1} -> {element}")


print("extra cchallenge ------------------")
print("----- stack ------------------")
stack: Stack = Stack()
print(f"stack added 1: {stack.push(1)}")
print(f"stack added 2: {stack.push(2)}")
print(f"stack size: {stack.size()}")
print(f"stack pop element: {stack.pop()}")
print(f"stack added 4: {stack.push(4)}")
print(f"stack size: {stack.size()}")
stack.printStack()


print("----- queue ------------------")
queue: Queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
print(f"queue size: {queue.size()}")
print(f"queue pop element: {queue.pop()}")
print(f"queue size: {queue.size()}")
queue.printQueue()
