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


def main():
    # Stack
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.stack)

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

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())


if __name__ == '__main__':
    main()
