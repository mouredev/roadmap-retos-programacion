# Reto #07 PILAS Y COLAS

""" Pilas o Stacks: principio LI-FO (Last in First Out) -> último en entrar,
primero en salir."""

stack = []

# Push
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

# Pop
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_item)

print(stack.pop())

print(stack)

""" Colas o Queue: principio FI-FO (First In-First Out) -> primero en entrar,
primero en salir."""

queue = []

# Enqueue
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# Dequeue
queue_item = queue[0]
del queue[0]
print(queue_item)

print(queue.pop(0))

print(queue)


# Extra

print("🧩 DIFICULTAD EXTRA - SIMULADOR DE NAVEGADOR WEB🧩")
def web_nav():
    stack = []

    while True:

        action = input(
            "Input your URL"
        )
        if action == "exit":
            print("Exit...")
            break
        elif action == "forward":
            pass
        elif action == "back":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)
        if len(stack) > 0:
            print(f"You're in the {stack[len(stack) - 1]} web.")
        else:
            print("You're in Home page.")
web_nav()

print("🧩 DIFICULTAD EXTRA - SIMULADOR DE IMPRESORA🧩")

def shared_printed():
    queue = []
    while True:

        action = input("Add a doc o select print/exit: ")

        if action == "exit":
            break
        elif action == "print":
            if len(queue) > 0:
                print(f"Printing: {queue.pop(0)}")
        else:
            queue.append(action)
        print(f"Print spooler: {queue}")

shared_printed()