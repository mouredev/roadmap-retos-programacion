class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


class Browser:
    def __init__(self):
        self.back_stack = Stack()
        self.forward_stack = Stack()
        self.current_page = None

    def navigate_to(self, page):
        if self.current_page:
            self.back_stack.push(self.current_page)
        self.current_page = page
        self.forward_stack = Stack()  # Clear forward stack

    def go_back(self):
        if not self.back_stack.is_empty():
            self.forward_stack.push(self.current_page)
            self.current_page = self.back_stack.pop()

    def go_forward(self):
        if not self.forward_stack.is_empty():
            self.back_stack.push(self.current_page)
            self.current_page = self.forward_stack.pop()

    def current(self):
        return self.current_page


# -- extra challenge
def browser_simulation():
    browser = Browser()
    while True:
        command = (
            input("Enter the name of a website, 'forward'|'back'|'exit|: ")
            .strip()
            .lower()
        )
        if command == "next":
            browser.go_forward()
        elif command == "back":
            browser.go_back()
        elif command == "exit":
            break
        else:
            browser.navigate_to(command)

        print(f"actual page: {browser.current()}")


if __name__ == "__main__":
    browser_simulation()


class Printer:
    def __init__(self):
        self.print_queue = Queue()

    def add_document(self, document):
        self.print_queue.enqueue(document)

    def print_document(self):
        if not self.print_queue.is_empty():
            document = self.print_queue.dequeue()
            print(f"printing document: {document}")
        else:
            print("there are no documents in the queue.")

    def queue_size(self):
        return self.print_queue.size()


def printer_simulation():
    printer = Printer()
    while True:
        command = (
            input("enter the name of a document or 'print' | 'exit': ").strip().lower()
        )
        if command == "print":
            printer.print_document()
        elif command == "exit":
            break
        else:
            printer.add_document(command)
            print(
                f"document '{command}' added to queue. Documents in queue: {printer.queue_size()}"
            )


if __name__ == "__main__":
    printer_simulation()
