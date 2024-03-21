class Vehicle:
    def __init__(self):
        self.state = "stopped"
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        self.state = "running"

    def brake(self):
        self.speed -= 10
        if self.speed < 0:
            self.speed = 0
        if self.speed == 0:
            self.state = "stopped"


# Stack (LIFO)
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            stack_item = self.stack[len(self.stack) - 1]
            del self.stack[len(self.stack) - 1]
            return stack_item

    def is_empty(self):
        return len(self.stack) == 0

    def count(self):
        return len(self.stack)


# Queue (FIFO)
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            queue_item = self.queue[0]
            del self.queue[0]
            return queue_item

    def is_empty(self):
        return len(self.queue) == 0

    def count(self):
        return len(self.queue)


def main():

    # Vehicle
    car = Vehicle()
    print(car.state)
    print(car.speed)
    car.accelerate()
    print(car.state)
    print(car.speed)

    # Stack
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.stack)

    print(f"stack elements count: {stack.count()}")
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    # Queue
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.queue)

    print(f"queue elements count: {queue.count()}")
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())


if __name__ == '__main__':
    main()
