"""
Ejercicio 
"""

# Pilas/Stack (LIFO)
stack = []
stack.append(1)  # push
stack.append(2)  # push
stack.append(3)  # push

print(stack)

# pop
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_item)

print(stack.pop())

print(stack)

# Cola/Queue (FIFO)

queue = []
queue.append(1)  # enqueue
queue.append(2)  # enqueue
queue.append(3)  # enqueue

# dequeue
queue_item = queue[0]
del queue[0]
print(queue_item)

print(queue.pop(0))

print(queue)

"""
DIFICULTAD EXTRA
"""


def web_navigation():
    stack = []

    while True:
        action = input("Añade una url o interactúa con palabras atrás/salir: ")

        if action == "salir":
            print("Saliendo del navegador web")
            break
        elif action == "atrás":
            if len(stack) > 0:
                print(stack.pop())
            else:
                print("No se pueden interactuar con palabras antes de añadir una ")
        else:
            stack.append(action)

        if len(stack) > 0:
            print(f"Has navegado a la web: {stack[len(stack) - 1]}")
        else:
            print("Estás en la página de inicio.")


# web_navigation()


def shared_printed():
    queue = []

    while True:
        action = input("Añade un documento o selecciona imprimir/salir: ")

        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo: {queue.pop(0)}")
            else:
                print(
                    "No se pueden interactuar con palabras antes de añadir una impresión"
                )
        else:
            queue.append(action)

        if len(queue) > 0:
            print(f"Cola de impresión: {queue}")
        else:
            print("Estás en la cola de inicio.")


shared_printed()
