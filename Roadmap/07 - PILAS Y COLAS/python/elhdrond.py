"""
    STACKS AND QUEUES
"""

# --- Stack LIFO - manual array (no list methods) ---

stack = []
stack = stack + ["first"]
stack = stack + ["second"]
stack = stack + ["third"]
print(stack)

while len(stack) > 0:
    stack_item = stack[len(stack) - 1]
    stack = stack[:len(stack) - 1]
    print(f"Popped: {stack_item}")
print(stack)

# --- Queue FIFO - manual array (no list methods) ---

queue = []
queue = queue + ["first"]
queue = queue + ["second"]
queue = queue + ["third"]
print(queue)

while len(queue) > 0:
    queue_item = queue[0]
    queue = queue[1:]
    print(f"Dequeued: {queue_item}")
print(queue)

# --- Stack LIFO - using list methods ---
# Stacks LIFO (Last in First out)
stack = []

# Push 
stack.append("first")
stack.append("second")
stack.append("third")

print(stack)

# Pop
print(stack.pop())
print(stack.pop())
print(stack.pop())

# QUEUES FIFO (First in First Out)

queue = []

# Enqueue
queue.append("first")
queue.append("second")
queue.append("third")

print(queue)

# Dequeue
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))


"""
    EXTRA EXERCISE
"""


# --- Web browser navigation (Stack) ---

def web_browser():
    history = []
    forward_stack = []

    running = True
    while running:
        action = input("Enter a URL or type 'back', 'forward', 'quit': ").strip()

        match action:
            case "quit":
                print("Closing browser.")
                running = False
            case "back":
                if len(history) > 1:
                    forward_stack.append(history.pop())
                    print(f"Back to: {history[-1]}")
                else:
                    print("No previous page.")
            case "forward":
                if len(forward_stack) > 0:
                    history.append(forward_stack.pop())
                    print(f"Forward to: {history[-1]}")
                else:
                    print("No next page.")
            case _:
                history.append(action)
                forward_stack.clear()
                print(f"Navigated to: {history[-1]}")


web_browser()


# --- Shared printer (Queue) ---

def shared_printer():
    queue = []

    running = True
    while running:
        action = input("Add a document or type 'print', 'quit': ").strip()

        match action:
            case "quit":
                print("Printer off.")
                running = False
            case "print":
                if len(queue) > 0:
                    print(f"Printing: {queue.pop(0)}")
                else:
                    print("Queue is empty.")
            case _:
                queue.append(action)
                print(f"Document '{action}' added to queue.")

        if running:
            print(f"Print queue: {queue}")


shared_printer()