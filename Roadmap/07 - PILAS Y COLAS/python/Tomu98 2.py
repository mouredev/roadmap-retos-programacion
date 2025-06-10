""" Reto 07: Pilas y Colas """

# Pila/Stack (LIFO)
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


# Cola/Queue (FIFO)
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



""" Reto extra """

# Web
def web_navigation():
    stack = []

    while True:
        action = input("Añade una url o interactúa con palabras 'adelante'/'atrás'/'salir': ")
        if action.lower() == "salir":
            print("Saliendo del navegador web.")
            break
        elif action.lower() == "adelante":
            pass
        elif action.lower() == "atrás":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)

        if len(stack) > 0:
            print(f"Has navegado a la web: {stack[len(stack) - 1]}.")
        else:
            print("Estás en la página de inicio.")

web_navigation()


def shared_printed():
    queue = []

    while True:
        action = input("Añade un documento o selección 'imprimir'/'salir': ")
        if action.lower() == "salir":
            break
        elif action.lower() == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo: {queue.pop(0)}")
        else:
            queue.append(action)

        print(f"Cola de impresión: {queue}")

shared_printed()