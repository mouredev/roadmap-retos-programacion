# problem 07 Stacks & Queues

# Stack - LIFO
class Stack:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def pop(self):
        try:
            item = self.items.pop()
        except IndexError:
            item = None
        finally:
            return item


my_stack = Stack()
my_stack.insert(1)
my_stack.insert(2)
my_stack.insert(3)
my_stack.insert(4)

print(f"{my_stack.pop() = }")


class Queue:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def pop(self):
        try:
            item = self.items.pop(0)
        except IndexError:
            item = None
        finally:
            return item


my_queue = Queue()
my_queue.insert(1)
my_queue.insert(2)
my_queue.insert(3)
my_queue.insert(4)

print(f"{my_queue.pop() = }")


# Extra

def web_browser():
    stack = Stack()

    while True:
        option = input("Enter url or select Next / Previous / Exit: ")

        if option.lower() == "exit":
            print("Exiting...")
            break
        elif option.lower() == "previous":
            current_url = stack.pop()
            previous_url = stack.pop()
            stack.insert(previous_url)  # Insert to be current next loop
            if previous_url is None:
                print("Home page")
            else:
                print(f"URL: {previous_url}")
        elif option.lower() == "next":
            # due a stack deletes values when it pops, can't go next
            pass
        else:
            stack.insert(option)
            print(f"URL added {option}")


web_browser()


def printer():
    queue = Queue()

    while True:
        option = input("Enter document or select Print / Exit: ")

        if option.lower() == "exit":
            print("Exiting...")
            break
        elif option.lower() == "print":
            document = queue.pop()
            if document is None:
                print("Empty queue")
            else:
                print(f"Printing document {document}")
        else:
            queue.insert(option)
            print(f"Document added {option}")


printer()
